from app.infrastructure.logging.logger import get_logger
from app.domain.ports.license_repository import LicenseRepository
from app.domain.entities.license import License
from app.domain.exceptions import NotFoundError, ConflictError
from app.interfaces.api.v1.schemas.license_schema import LicenseCreate, LicenseUpdate, LicenseResponse

logger = get_logger(__name__)

class LicenseService:
    def __init__(self, license_repository: LicenseRepository):
        self.license_repository = license_repository

    # =========================
    # GET ALL
    # =========================
    def get_licenses(self, skip: int = 0, limit: int = 100) -> list[LicenseResponse]:
        logger.info('Retrieving license list.')
        return self.license_repository.get_all(skip=skip, limit=limit)

    # =========================
    # GET BY ID
    # =========================
    def get_license(self, license_id: int) -> LicenseResponse:
        logger.info(f'Searching for license with ID: {license_id}.')
        license = self.license_repository.get_by_id(license_id)
        if not license:
            logger.warning(f'License with ID: {license_id} not found.')
            raise NotFoundError(f'License with ID: {license_id} not found.')
        return license

    # =========================
    # CREATE
    # =========================
    def create_license(self, license_data: License) -> LicenseResponse:
        logger.info(f'Creating license with name: {license_data.name}.')
        existing = self.license_repository.get_by_name(license_data.name)
        if existing:
            logger.error(f'License with name: {license_data.name} already exists.')
            raise ConflictError('License already exists.')
        license = License(
            id=None,
            name=license_data.name,
            description=license_data.description,
            slug=license_data.slug,
            products=license_data.products,
            images=license_data.images
        )
        return self.license_repository.create(license)

    # =========================
    # UPDATE
    # =========================
    def update_license(self, license_id: int, license_data: License) -> LicenseResponse:
        logger.info(f'Updating license with ID: {license_id}.')
        existing = self.license_repository.get_by_id(license_id)
        if not existing:
            logger.warning(f'License with ID: {license_id} not found.')
            raise NotFoundError(f'License with ID: {license_id} not found.')
        updated_license = License(
            name=license_data.name,
            description=license_data.description,
            slug=license_data.slug,
            products=license_data.products,
            images=license_data.images
        )
        return self.license_repository.update(license_id, updated_license)

    # =========================
    # DELETE
    # =========================
    def delete_license(self, license_id: int) -> bool:
        logger.info(f'Deleting license with ID: {license_id}.')
        existing = self.license_repository.get_by_id(license_id)
        if not existing:
            logger.warning(f'License with ID: {license_id} not found.')
            raise NotFoundError(f'License with ID: {license_id} not found.')
        return self.license_repository.delete(license_id)