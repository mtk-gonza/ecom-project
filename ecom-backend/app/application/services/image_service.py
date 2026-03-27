import logging
from app.domain.enums.image_type import ImageType
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
        license_repository: LicenseRepository
    ):
        self.image_repository = image_repository
        self.product_repository = product_repository
        self.license_repository = license_repository


    async def create_image(
        self,
        filename: str,
        image_data,
        entity_type: str,
        entity_id: int,
        image_type: ImageType
    ) -> dict:
        allowed = {"jpg", "jpeg", "png", "webp"}
        ext = filename.split(".")[-1].lower()
        if ext not in allowed:
            raise ValidationError("Unsupported image format")
        
        try:
            match entity_type.lower():
                case "product":
                    product = await self.product_repository.get_by_id(entity_id)
                    if not product:
                        raise NotFoundError("Product not found")
                    license_name = product.licence.name.replace(" ", "-").lower()
                    category_name = product.category.name.replace(" ", "-").lower()
                    product_name = product.name.replace(" ", "-").lower()
                    path_segments = [
                        license_name,
                        category_name,
                        f"{product_name}_{image_type.value.lower()}.{ext}"
                    ]

                case "license":
                    license = await self.license_repository.get_by_id(entity_id)
                    if not license:
                        raise NotFoundError("License not found")
                    license_name = license.name.replace(" ", "-").lower()
                    path_segments = [
                        license_name,
                        "license",
                        f"{license_name}_{image_type.value.lower()}.{ext}"
                    ]

                case _:
                    raise ValidationError(f"{entity_type} not supported")

            is_primary = image_type.value in ["front", "logo"]

            await self.image_repository.save_image(
                image_data=image_data,
                entity_type=entity_type,
                entity_id=entity_id,
                image_type=image_type,
                is_primary=is_primary,
                path_segments=path_segments
            )
            return {"message": "Image uploaded successfully"}

        except Exception as e:
            logger.error(f"Error creating image: {e}")
            raise