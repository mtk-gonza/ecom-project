import logging
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.exc import SQLAlchemyError
from app.domain.ports.license_repository import LicenseRepository
from app.domain.entities.license import License
from app.domain.exceptions import NotFoundException
from app.infrastructure.db.models.license_model import LicenseModel
from app.infrastructure.mappers.license_mapper import LicenseMapper

logger = logging.getLogger(__name__)

class LicenseRepositoryImpl(LicenseRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def create(self, licence: License) -> License:
        try:
            model = LicenseModel.from_domain(licence)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return LicenseMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f'Error creating licence: {e}')
            self.db.rollback()
            raise


    def get_by_id(self, licence_id: int) -> License:
        try:
            stmt = (select(LicenseModel).options(selectinload(LicenseModel.images)).where(LicenseModel.id == licence_id))
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"Licence {licence_id} not found")
            return LicenseMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f'Error reading licence: {e}')
            raise


    def get_all(self) -> list[License]:
        try:
            stmt = select(LicenseModel).options(selectinload(LicenseModel.images))
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [
                LicenseMapper.to_domain(model) 
                for model in models
            ]

        except SQLAlchemyError as e:
            logger.error(f'Error reading licences: {e}')
            raise


    def update(self, licence_id: int, licence_data: License) -> License:
        try:
            stmt = select(LicenseModel).where(LicenseModel.id == licence_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"Licence {licence_id} not found")
            LicenseMapper.update_model_from_domain(model, licence_data)
            self.db.commit()
            self.db.refresh(model)
            return LicenseMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f'Error updating licence: {e}')
            self.db.rollback()
            raise


    def delete(self, licence_id: int) -> bool:
        try:
            stmt = select(LicenseModel).where(LicenseModel.id == licence_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundException(f"Licence {licence_id} not found")
            self.db.delete(model)
            self.db.commit()
            return True

        except SQLAlchemyError as e:
            logger.error(f'Error deleting licence: {e}')
            self.db.rollback()
            raise