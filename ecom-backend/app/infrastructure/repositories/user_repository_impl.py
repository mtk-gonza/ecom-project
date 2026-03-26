import logging
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.domain.ports.user_repository import UserRepository
from app.domain.entities.user import User
from app.domain.exceptions import NotFoundError
from app.infrastructure.db.models.user_model import UserModel
from app.infrastructure.db.models.role_model import RoleModel
from app.infrastructure.mappers.user_mapper import UserMapper

logger = logging.getLogger(__name__)

class UserRepositoryImpl(UserRepository):
    def __init__(self, db_session: Session):
        self.db = db_session


    def get_by_id(self, user_id: int) -> User:
        try:
            stmt = select(UserModel).where(UserModel.id == user_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"User {user_id} not found")
            return UserMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f"Error reading user by id: {e}")
            raise


    def get_by_username(self, username: str) -> User:
        try:
            stmt = select(UserModel).where(UserModel.username == username)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"User {username} not found")
            return UserMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f"Error reading user by username: {e}")
            raise


    def get_all(self) -> list[User]:
        try:
            stmt = select(UserModel)
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [
                UserMapper.to_domain(model) 
                for model in models
            ]

        except SQLAlchemyError as e:
            logger.error(f"Error reading users: {e}")
            raise


    def create(self, user_data: User) -> User:
        try:
            model = UserMapper.from_domain(user_data)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return UserMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f"Error creating user: {e}")
            self.db.rollback()
            raise


    def update(self, user_id: int, user_data: User) -> User:
        try:
            stmt = select(UserModel).where(UserModel.id == user_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"User {user_id} not found")
            UserMapper.update_model_from_domain(model, user_data)
            self.db.commit()
            self.db.refresh(model)
            return UserMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f"Error updating user: {e}")
            self.db.rollback()
            raise


    def delete(self, user_id: int) -> bool:
        try:
            stmt = select(UserModel).where(UserModel.id == user_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"User {user_id} not found")
            self.db.delete(model)
            self.db.commit()
            return True

        except SQLAlchemyError as e:
            logger.error(f"Error deleting user: {e}")
            self.db.rollback()
            raise


    
    def add_role_to_user(self, user_id: int, role_id: int):
        user = self.db.get(UserModel, user_id)
        role = self.db.get(RoleModel, role_id)

        if not user or not role:
            raise NotFoundError("User o Role no encontrado")

        user.roles.append(role)
        self.db.commit()

    def remove_role_from_user(self, user_id: int, role_id: int):
        user = self.db.get(UserModel, user_id)
        role = self.db.get(RoleModel, role_id)

        if not user or not role:
            raise NotFoundError("User o Role no encontrado")

        user.roles.remove(role)
        self.db.commit()