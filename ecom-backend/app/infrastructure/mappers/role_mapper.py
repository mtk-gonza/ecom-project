from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.role import Role
from app.infrastructure.db.models.role_model import RoleModel

class RoleMapper(BaseMapper):
    RELATION_MAPPERS = {}

    @classmethod
    def to_domain(cls, model: RoleModel) -> Role:
        return BaseMapper.to_domain(model, Role)

    @staticmethod
    def from_domain(domain: Role) -> RoleModel:
        return BaseMapper.from_domain(domain, RoleModel)

    @staticmethod
    def update_model_from_domain(model: RoleModel, domain: Role):
        BaseMapper.update_model_from_domain(model, domain)