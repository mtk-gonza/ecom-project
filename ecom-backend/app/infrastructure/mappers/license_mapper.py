from typing import TYPE_CHECKING
from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.license import License
from app.infrastructure.db.models.license_model import LicenseModel
from .image_mapper import ImageMapper

if TYPE_CHECKING:
    from .product_mapper import ProductMapper

class LicenseMapper(BaseMapper):
    RELATION_MAPPERS = {
        'products': 'ProductMapper',
        'images': ImageMapper,
    }

    @classmethod
    def to_domain(cls, model: LicenseModel) -> License:
        return BaseMapper.to_domain(model, License)

    @staticmethod
    def from_domain(domain: License) -> LicenseModel:
        return BaseMapper.from_domain(domain, LicenseModel)
    
    @staticmethod
    def update_model_from_domain(model: LicenseModel, domain: License):
        BaseMapper.update_model_from_domain(model, domain)