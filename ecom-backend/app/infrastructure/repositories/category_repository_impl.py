from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.infrastructure.logging.logger import get_logger
from app.domain.ports.category_repository import CategoryRepository
from app.domain.entities.category import Category
from app.domain.exceptions import NotFoundError
from app.infrastructure.db.models.category_model import CategoryModel
from app.infrastructure.mappers.category_mapper import CategoryMapper

logger = get_logger(__name__)

class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, db: Session):
        self.db = db


    def get_all(self) -> list[Category]:
        try:
            stmt = select(CategoryModel)
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [
                CategoryMapper.to_domain(model)    
                for model in models
            ]
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting categories: {e}')
            raise


    def get_by_id(self, category_id: int) -> Category:
        try:
            stmt = select(CategoryModel).where(CategoryModel.id == category_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Category with ID: {category_id} not found.')
            return CategoryMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting category with ID: {category_id} : {e}')
            raise

       
    def create(self, category_data: Category) -> Category:
        try:
            model = CategoryMapper.from_domain(category_data)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return CategoryMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Error creating category: {e}')
            self.db.rollback()
            raise


    def update(self, category_id: int, category_data: Category) -> Category:
        try:
            stmt = select(CategoryModel).where(CategoryModel.id == category_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Category with ID: {category_id} not found.')
            CategoryMapper.update_model_from_domain(model, category_data)
            self.db.commit()
            self.db.refresh(model)
            return CategoryMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Error updating category with ID: {category_id} : {e}')
            self.db.rollback()
            raise   


    def delete(self, category_id: int) -> bool:
        try:
            stmt = select(CategoryModel).where(CategoryModel.id == category_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Category with ID: {category_id} not found.')
            self.db.delete(model)
            self.db.commit()
            return True
        
        except SQLAlchemyError as e:
            logger.error(f'Error deleting category with ID: {category_id}: {e}')
            self.db.rollback()
            raise