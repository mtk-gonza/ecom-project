from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.user import User
from app.infrastructure.db.models.user_model import UserModel
from .role_mapper import RoleMapper

class UserMapper(BaseMapper):
    RELATION_MAPPERS = {'roles': RoleMapper}

    @classmethod
    def to_domain(cls, model: UserModel) -> User:
        domain = BaseMapper.to_domain(model, User)
        domain.roles = [role.name for role in model.roles]
        return domain

    @staticmethod
    def from_domain(domain: User) -> UserModel:
        return BaseMapper.from_domain(domain, UserModel)

    @staticmethod
    def update_model_from_domain(model: UserModel, domain: User):
        BaseMapper.update_model_from_domain(model, domain)