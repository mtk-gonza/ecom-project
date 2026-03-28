import logging
from app.domain.enums import EntityType, ImageType
from app.domain.entities.image import Image
from app.domain.ports.image_repository import ImageRepository
from app.domain.ports.product_repository import ProductRepository
from app.domain.ports.license_repository import LicenseRepository
from app.domain.exceptions import NotFoundError, ValidationError

logger = logging.getLogger(__name__)

class ImageService:
    def __init__(
        self,
        image_repository: ImageRepository,
        product_repository: ProductRepository,
        license_repository: LicenseRepository,
        storage
    ):
        self.image_repository = image_repository
        self.product_repository = product_repository
        self.license_repository = license_repository
        self.storage = storage

    async def create_image(
        self,
        filename: str,
        image_data: bytes,
        entity_type: EntityType,
        entity_id: int,
        image_type: ImageType
    ) -> Image:

        # 🔹 Validar extensión
        allowed = {"jpg", "jpeg", "png", "webp"}
        ext = filename.split(".")[-1].lower()

        if ext not in allowed:
            raise ValidationError("Unsupported image format")

        # 🔹 Construir path según entidad
        path_segments = await self._build_path(
            entity_type,
            entity_id,
            image_type,
            ext
        )

        # 🔹 Guardar archivo (infraestructura)
        path = self.storage.save(image_data, path_segments)

        # 🔹 Lógica de negocio
        is_primary = image_type in [ImageType.FRONT, ImageType.LOGO]

        image = Image(
            id=None,
            path=path,
            entity_id=entity_id,
            entity_type=entity_type,
            image_type=image_type,
            is_primary=is_primary
        )

        # 🔹 Persistir
        return self.image_repository.create(image)

    async def _build_path(
        self,
        entity_type: EntityType,
        entity_id: int,
        image_type: ImageType,
        ext: str
    ) -> list[str]:

        match entity_type:

            case EntityType.PRODUCT:
                product = await self.product_repository.get_by_id(entity_id)
                if not product:
                    raise NotFoundError("Product not found")

                return [
                    product.licence.name.replace(" ", "-").lower(),
                    product.category.name.replace(" ", "-").lower(),
                    f"{product.name.replace(' ', '-').lower()}_{image_type.value}.{ext}"
                ]

            case EntityType.LICENSE:
                license = await self.license_repository.get_by_id(entity_id)
                if not license:
                    raise NotFoundError("License not found")

                name = license.name.replace(" ", "-").lower()

                return [
                    name,
                    "license",
                    f"{name}_{image_type.value}.{ext}"
                ]

            case _:
                raise ValidationError(f"{entity_type} not supported")