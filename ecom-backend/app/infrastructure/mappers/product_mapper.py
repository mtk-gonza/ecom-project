from typing import TYPE_CHECKING
from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.product import Product
from app.infrastructure.db.models.product_model import ProductModel
from .image_mapper import ImageMapper
from .specification_mapper import SpecificationMapper

if TYPE_CHECKING:
    from .license_mapper import LicenseMapper
    from .category_mapper import CategoryMapper

class ProductMapper(BaseMapper):
    RELATION_MAPPERS = {
        'images': ImageMapper,                  # ← Sin círculo, import directo OK
        'specifications': SpecificationMapper,  # ← Sin círculo, import directo OK
        'license': 'LicenseMapper',             # ← String para lazy import
        'category': 'CategoryMapper',           # ← String para lazy import
    }

    @classmethod
    def to_domain(cls, model: ProductModel) -> Product:
        return BaseMapper.to_domain(model, Product)

    @staticmethod
    def from_domain(domain: Product) -> ProductModel:
        return BaseMapper.from_domain(domain, ProductModel)
    
    @staticmethod
    def update_model_from_domain(model: ProductModel, domain: Product):
        BaseMapper.update_model_from_domain(model, domain)