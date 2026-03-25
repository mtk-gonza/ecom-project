import logging
from src.domain.ports.license_repository import LicenseRepositoryPort
from src.domain.entities.license_entity import License
from src.domain.exceptions import NotFoundException, AlreadyExistsException

logger = logging.getLogger(__name__)

class LicenseService:
    def __init__(self, license_repository: LicenseRepositoryPort):
        self.license_repository = license_repository

    def get_license(self, license_id: int) -> License:
        license = self.license_repository.get_by_id(license_id)
        if not license:
            logger.warning(f'License with ID: {license_id} not found.')
            raise NotFoundException(f'License with ID: {license_id} not found.')
        return license

    def get_licenses(self, skip: int = 0, limit: int = 100) -> list[License]:
        return self.license_repository.get_all(skip=skip, limit=limit)

    def create_license(self, license_data: License) -> License:
        existing = self.license_repository.get_by_name(license_data.name)
        if existing:
            logger.error(f'License with name: {license_data.name} already exists.')
            raise AlreadyExistsException('License already exists.')
        license = License(
            name=license_data.name,
            description=license_data.description,
            slug=license_data.slug,
            products=license_data.products,
            images=license_data.images
        )
        return self.license_repository.create(license)

    def update_license(self, license_id: int, license_data: License) -> License:
        license_data = self.license_repository.get_by_id(license_id)
        if not license_data:
            logger.warning(f'License with ID: {license_id} not found.')
            raise NotFoundException(f'License with ID: {license_id} not found.')
        updated_license = License(
            name=license_data.name,
            description=license_data.description,
            slug=license_data.slug,
            products=license_data.products,
            images=license_data.images
        )
        return self.license_repository.update(license_id, updated_license)

    def delete_license(self, license_id: int) -> bool:
        license = self.license_repository.get_by_id(license_id)
        if not license:
            logger.warning(f'License with ID: {license_id} not found.')
            raise NotFoundException(f'License with ID: {license_id} not found.')
        return self.license_repository.delete(license_id)