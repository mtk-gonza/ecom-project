from src.infrastructure.mappers.base_mapper import BaseMapper
from src.domain.entities.user_roles_entity import UserRoles
from src.infrastructure.database.models.user_roles_model import UserRolesModel

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