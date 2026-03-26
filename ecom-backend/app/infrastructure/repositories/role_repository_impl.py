import logging
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.domain.ports.role_repository import RoleRepository
from app.domain.entities.role import Role
from app.domain.exceptions import NotFoundError
from app.infrastructure.db.models.role_model import RoleModel
from app.infrastructure.mappers.category_mapper import CategoryMapper

logger = logging.getLogger(__name__)

class RoleRepositoryImpl(RoleRepository):
    def __init__(self, db_session: Session):
        self.db = db_session


    def get_by_id(self, role_id: int) -> Role:
        try:
            stmt = select(RoleModel).where(RoleModel.id == role_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"Role {role_id} not found")
            return CategoryMapper.to_domain(model)
        except SQLAlchemyError as e:
            logger.error(f'Database error getting role: {e}')
            raise


    def get_all(self) -> list[Role]:
        try:
            stmt = select(RoleModel)
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [
                CategoryMapper.to_domain(model) 
                for model in models
            ]
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting roles: {e}')
            raise


    def create(self, role_data: Role) -> Role:
        try:
            model = RoleModel.from_domain(role_data)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return CategoryMapper.to_domain(model)
        except SQLAlchemyError as e:
            logger.error(f'Error creating role: {e}')
            self.db.rollback()
            raise


    def update(self, role_id: int, role_data: Role) -> Role:
        try:
            stmt = select(RoleModel).where(RoleModel.id == role_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"Role {role_id} not found")
            CategoryMapper.update_model_from_domain(model, role_data)
            self.db.commit()
            self.db.refresh(model)
            return CategoryMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Error updating role: {e}')
            self.rollback()
            raise    


    def delete(self, role_id: int) -> bool:
        try:
            stmt = select(RoleModel).where(RoleModel.id == role_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"Role {role_id} not found")
            self.db.delete(model)
            self.db.commit()
            return True
        
        except SQLAlchemyError as e:
            logger.error(f'Error deleting role: {e}')
            self.db.rollback()
            raise
