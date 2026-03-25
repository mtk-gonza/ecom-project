from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.product import Product
from app.infrastructure.db.models.product_model import ProductModel

class ProductMapper(BaseMapper):
    @staticmethod
    def to_domain(model: ProductModel) -> Product:
        product = BaseMapper.to_domain(model, Product)
        product.specifications = [
            {
                'key': s.key, 
                'value': s.value
            } 
            for s in model.specifications
        ]
        product.images = [
            {
                'path': i.path, 
                'image_type': i.image_type, 
                'is_primary': i.is_primary
            }
            for i in model.images
        ]
        return product

    @staticmethod
    def from_domain(domain: Product) -> ProductModel:
        model = BaseMapper.from_domain(domain, ProductModel)
        return model
    
    @staticmethod
    def update_model_from_domain(model: ProductModel, domain: Product):
        BaseMapper.update_model_from_domain(model, domain)