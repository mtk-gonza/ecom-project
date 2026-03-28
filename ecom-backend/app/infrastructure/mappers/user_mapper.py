from app.infrastructure.mappers.base_mapper import BaseMapper
from app.domain.entities.user import User
from app.infrastructure.db.models.user_model import UserModel

class UserMapper(BaseMapper):

    @staticmethod
    def to_domain(model: UserModel) -> User:
        domain = BaseMapper.to_domain(model, User)
        domain.roles = [role.name for role in model.roles]
        return domain

    @staticmethod
    def from_domain(domain: User) -> UserModel:
        return BaseMapper.from_domain(domain, UserModel)

    @staticmethod
    def update_model_from_domain(model: UserModel, domain: User):
        BaseMapper.update_model_from_domain(model, domain)