from src.infrastructure.mappers.base_mapper import BaseMapper
from src.domain.entities.role_entity import Role
from src.infrastructure.database.models.role_model import RoleModel

class LicenceMapper(BaseMapper):
    @staticmethod
    def to_domain(model: RoleModel) -> Role:
        return BaseMapper.to_domain(model, Role)

    @staticmethod
    def from_domain(domain: Role) -> RoleModel:
        return BaseMapper.from_domain(domain, RoleModel)

    @staticmethod
    def update_model_from_domain(model: RoleModel, domain: Role):
        BaseMapper.update_model_from_domain(model, domain)