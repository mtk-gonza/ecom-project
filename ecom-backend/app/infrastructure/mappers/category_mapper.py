from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.category import Category
from app.infrastructure.db.models.category_model import CategoryModel

class CategoryMapper(BaseMapper):
    @staticmethod
    def to_domain(model: CategoryModel) -> Category:
        return BaseMapper.to_domain(model, Category)

    @staticmethod
    def from_domain(domain: Category) -> CategoryModel:
        return BaseMapper.from_domain(domain, CategoryModel)

    @staticmethod
    def update_model_from_domain(model: CategoryModel, domain: Category):
        BaseMapper.update_model_from_domain(model, domain)