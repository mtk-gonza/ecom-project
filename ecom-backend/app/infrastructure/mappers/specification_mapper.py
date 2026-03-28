from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.specification import Specification
from app.infrastructure.db.models.specification_model import SpecificationModel

class SpecificationMapper(BaseMapper):
    RELATION_MAPPERS = {}

    @classmethod
    def to_domain(cls, model: SpecificationModel) -> Specification:
        return BaseMapper.to_domain(model, Specification)

    @staticmethod
    def from_domain(domain: Specification) -> SpecificationModel:
        return BaseMapper.from_domain(domain, SpecificationModel)

    @staticmethod
    def update_model_from_domain(model: SpecificationModel, domain: Specification):
        BaseMapper.update_model_from_domain(model, domain)