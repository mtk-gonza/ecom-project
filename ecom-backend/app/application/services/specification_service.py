from app.infrastructure.logging.logger import get_logger
from app.domain.ports.specification_repository import SpecificationRepository
from app.domain.entities.specification import Specification
from app.domain.exceptions import NotFoundError, ValidationError, ConflictError
from app.interfaces.api.v1.schemas.specification_schema import SpecificationCreate, SpecificationUpdate, SpecificationResponse

logger = get_logger(__name__)

class SpecificationService:
    def __init__(self, specification_repository: SpecificationRepository):
        self.specification_repository = specification_repository

    # =========================
    # GET ALL
    # =========================
    def get_specifications(self, skip: int = 0, limit: int = 100) -> list[SpecificationResponse]:
        logger.info('Retrieving specifications list.')
        return self.specification_repository.get_all(skip=skip, limit=limit)

    # =========================
    # GET BY ID
    # =========================
    def get_specification(self, specification_id: int) -> SpecificationResponse:
        logger.info(f'Searching for specification with ID: {specification_id}.')
        specification = self.specification_repository.get_by_id(specification_id)
        if not specification:
            logger.warning(f'Specification with ID: {specification_id} not found.')
            raise NotFoundError(f'Specification with ID: {specification_id} not found.')
        return specification

    # =========================
    # CREATE
    # =========================
    def create_specification(self, spec_data: SpecificationCreate) -> SpecificationResponse:
        logger.info(f'Creating specification with entity type: {spec_data.entity_type} and entity ID: {spec_data.entity_id}.')
        specification = Specification(
            id=None,
            entity_type=spec_data.entity_type,
            entity_id=spec_data.entity_id,
            key=spec_data.key,
            value=spec_data.value
        )
        logger.info(f'New specification created with entity type: {spec_data.entity_type} and entity ID: {spec_data.entity_id}.')
        return specification

    # =========================
    # UPDATE
    # =========================
    def update_specification(self, spec_id: int, spec_data: SpecificationUpdate) -> SpecificationResponse:
        logger.info(f"Actualizando producto id={spec_id}")
        existing = self.specification_repository.get_by_id(spec_id)
        if not existing:
            logger.warning(f'Specification with ID: {spec_id} not found.')
            raise NotFoundError(f'Specification with ID: {spec_id} not found.')
        updated_spec = Specification(
            id=existing.id, 
            entity_type=spec_data.entity_type or existing.entity_type,
            entity_id=spec_data.entity_id or existing.entity_id,
            key=spec_data.key or existing.key,
            value=spec_data.value or existing.value
        )
        return self.specification_repository.update(updated_spec)

    # =========================
    # DELETE
    # =========================
    def delete_specification(self, spec_id: int) -> bool:
        logger.info(f'Deleting specification with ID: {spec_id}.')
        existing = self.specification_repository.get_by_id(spec_id)
        if not existing:
            logger.warning(f'Specification with ID: {spec_id} not found.')
            raise NotFoundError(f'Specification with ID: {spec_id} not found.')
        return self.specification_repository.delete(spec_id)