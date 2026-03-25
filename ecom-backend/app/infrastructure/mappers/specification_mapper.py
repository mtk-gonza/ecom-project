from src.infrastructure.mappers.base_mapper import BaseMapper
from src.domain.entities.specification_entity import Specification
from src.infrastructure.database.models.specification_model import SpecificationModel

class SpecificationMapper(BaseMapper):
    @staticmethod
    def to_domain(model: SpecificationModel) -> Specification:
        return BaseMapper.to_domain(model, Specification)

    @staticmethod
    def from_domain(domain: Specification) -> SpecificationModel:
        return BaseMapper.from_domain(domain, SpecificationModel)

    @staticmethod
    def update_model_from_domain(model: SpecificationModel, domain: Specification):
        BaseMapper.update_model_from_domain(model, domain)