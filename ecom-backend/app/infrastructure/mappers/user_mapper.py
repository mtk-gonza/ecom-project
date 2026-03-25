from src.infrastructure.mappers.base_mapper import BaseMapper
from src.domain.entities.user_entity import User
from src.infrastructure.database.models.user_model import UserModel

class UserMapper(BaseMapper):
    @staticmethod
    def to_domain(model: UserModel) -> User:
        return BaseMapper.to_domain(model, User)

    @staticmethod
    def from_domain(domain: User) -> UserModel:
        return BaseMapper.from_domain(domain, UserModel)

    @staticmethod
    def update_model_from_domain(model: UserModel, domain: User):
        BaseMapper.update_model_from_domain(model, domain)