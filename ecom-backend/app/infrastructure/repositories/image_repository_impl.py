import logging
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from src.domain.ports.image_repository import ImageRepositoryPort
from src.domain.entities.image_entity import Image
from src.domain.exceptions import NotFoundException
from src.infrastructure.database.models.image_model import ImageModel
from src.infrastructure.mappers.image_mapper import ImageMapper

logger = logging.getLogger(__name__)

class ImageRepositoryImpl(ImageRepositoryPort):
    def __init__(self, db_session: Session):
        self.db = db_session


    def get_by_id(self, image_id: int) -> Image:
        try:
            stmt = select(ImageModel).where(ImageModel.id == image_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"Image {image_id} not found")
            return ImageMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f"Error reading image: {e}")
            raise


    def get_by_entity(self, entity_type: str, entity_id: int) -> list[Image]:
        try:
            stmt = select(ImageModel).where(
                ImageModel.entity_type == entity_type,
                ImageModel.entity_id == entity_id
            )
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [
                ImageMapper.to_domain(model) 
                for model in models
            ]

        except SQLAlchemyError as e:
            logger.error(f"Error reading images: {e}")
            raise


    def create(self, image: Image) -> Image:
        try:
            model = ImageModel.from_domain(image)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return ImageMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f"Error creating image: {e}")
            self.db.rollback()
            raise


    def delete(self, image_id: int) -> bool:
        try:
            stmt = select(ImageModel).where(ImageModel.id == image_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"Image {image_id} not found")
            self.db.delete(model)
            self.db.commit()
            return True

        except SQLAlchemyError as e:
            logger.error(f"Error deleting image: {e}")
            self.db.rollback()
            raise