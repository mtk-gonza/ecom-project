from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.user_roles import UserRoles
from app.infrastructure.db.models.user_roles_model import UserRolesModel

class UserRolesMapper(BaseMapper):
    @staticmethod
    def to_domain(model: UserRolesModel) -> UserRoles:
        return BaseMapper.to_domain(model, UserRoles)

    @staticmethod
    def from_domain(domain: UserRoles) -> UserRolesModel:
        return BaseMapper.from_domain(domain, UserRolesModel)

    @staticmethod
    def update_model_from_domain(model: UserRolesModel, domain: UserRoles):
        BaseMapper.update_model_from_domain(model, domain)