import logging
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from src.domain.ports.user_roles_repository import UserRolesRepositoryPort
from src.domain.entities.user_roles_entity import UserRoles
from src.domain.exceptions import NotFoundException
from src.infrastructure.database.models.user_roles_model import UserRolesModel
from src.infrastructure.mappers.user_roles_mapper import UserRolesMapper

logger = logging.getLogger(__name__)

class UserRolesRepositoryImpl(UserRolesRepositoryPort):
    def __init__(self, db_session: Session):
        self.db = db_session


    def get_by_id(self, user_roles_id: int) -> UserRoles:
        try:
            stmt = select(UserRolesModel).where(UserRolesModel.id == user_roles_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"User Roles {user_roles_id} not found")
            return UserRolesMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f"Database error getting User Roles {user_roles_id}: {e}")
            raise


    def get_all(self) -> list[UserRoles]:
        try:
            stmt = select(UserRolesModel)
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [
                UserRolesMapper.to_domain(model)    
                for model in models
            ]
        
        except SQLAlchemyError as e:
            logger.error(f"Database error getting User Roles: {e}")
            raise

       
    def create(self, user_roles_data: UserRoles) -> UserRoles:
        try:
            model = UserRolesMapper.from_domain(user_roles_data)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return UserRolesMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logging.error(f'Error creating User Roles: {e}')
            self.db.rollback()
            raise


    def update(self, user_roles_id: int, user_roles_data: UserRoles) -> UserRoles:
        try:
            stmt = select(UserRolesModel).where(UserRolesModel.id == user_roles_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"User Roles {user_roles_id} not found")
            UserRolesMapper.update_model_from_domain(model, user_roles_data)
            self.db.commit()
            self.db.refresh(model)
            return UserRolesMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f"Error updating category {user_roles_id}: {e}")
            self.db.rollback()
            raise   


    def delete(self, user_roles_id: int) -> bool:
        try:
            stmt = select(UserRolesModel).where(UserRolesModel.id == user_roles_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"Category {user_roles_id} not found")
            self.db.delete(model)
            self.db.commit()
            return True
        
        except SQLAlchemyError as e:
            logging.error(f'Error deleting User Roles: {e}')
            self.db.rollback()
            raise    