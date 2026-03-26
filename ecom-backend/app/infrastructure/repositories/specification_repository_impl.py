import logging
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.domain.ports.specification_repository import ProductSpecRepositoryPort
from app.domain.entities.specification import Specification
from app.domain.exceptions import NotFoundError
from app.infrastructure.db.models.specification_model import SpecificationModel
from app.infrastructure.mappers.specification_mapper import SpecificationMapper

logger = logging.getLogger(__name__)

class SpecificationRepositoryImpl(ProductSpecRepositoryPort):
    def __init__(self, db_session: Session):
        self.db = db_session


    def get_by_id(self, product_specification_id: int) -> Specification:
        try:
            stmt = select(SpecificationModel).where(SpecificationModel.id == product_specification_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"Product Specification {product_specification_id} not found")
            return SpecificationMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Error reading product specification: {e}')
            raise


    def get_all(self) -> list[Specification]:
        try:
            stmt = select(SpecificationModel)
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [
                SpecificationMapper.to_domain(model) 
                for model in models
            ]
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting specifications: {e}')
            raise


    def create(self, specification_data: Specification) -> Specification:
        try:
            model = SpecificationMapper.from_domain(specification_data)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return SpecificationMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Error creating product specification: {e}')
            self.db.rollback()
            raise


    def update(self, specification_id: int, specification_data: Specification) -> Specification:
        try:
            stmt = select(SpecificationModel).where(SpecificationModel.id == specification_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"Product Specification {specification_id} not found")
            SpecificationMapper.update_model_from_domain(model, specification_data)
            self.db.commit()
            self.db.refresh(model)
            return SpecificationMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Error updating product specification: {e}')
            self.db.rollback()
            raise


    def delete(self, product_spec_id: int) -> bool:
        try:
            stmt = select(SpecificationModel).where(SpecificationModel.id == product_spec_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f"Product Specification {product_spec_id} not found")
            self.db.delete(model)
            self.db.commit()
            return True
        
        except SQLAlchemyError as e:
            logger.error(f'Error deleting product specification: {e}')
            self.db.rollback()
            raise