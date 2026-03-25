from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.image import Image
from app.infrastructure.db.models.image_model import ImageModel

class ImageMapper(BaseMapper):
    @staticmethod
    def to_domain(model: ImageModel) -> Image:
        return BaseMapper.to_domain(model, Image)

    @staticmethod
    def from_domain(domain: Image) -> ImageModel:
        return BaseMapper.from_domain(domain, ImageModel)

    @staticmethod
    def update_model_from_domain(model: ImageModel, domain: Image):
        BaseMapper.update_model_from_domain(model, domain)