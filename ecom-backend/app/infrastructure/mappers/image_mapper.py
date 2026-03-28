from app.infrastructure.mappers.base_mapper import BaseMapper
from app.infrastructure.db.models.image_model import ImageModel
from app.domain.entities.image import Image
from app.domain.enums import EntityType, ImageType

class ImageMapper(BaseMapper):
    @staticmethod
    def to_domain(model: ImageModel) -> Image:
        return Image(
            id=model.id,
            path=model.path,
            entity_id=model.entity_id,
            entity_type=EntityType(model.entity_type),  # 🔥 clave
            image_type=ImageType(model.image_type) if model.image_type else None,
            is_primary=model.is_primary,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    @staticmethod
    def from_domain(domain: Image) -> ImageModel:
        return BaseMapper.from_domain(domain, ImageModel)

    @staticmethod
    def update_model_from_domain(model: ImageModel, domain: Image):
        BaseMapper.update_model_from_domain(model, domain)