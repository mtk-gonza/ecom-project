from app.infrastructure.logging.logger import get_logger
from app.domain.ports.role_repository import RoleRepository
from app.domain.entities.role import Role
from app.domain.exceptions import NotFoundError, ConflictError
from app.interfaces.api.v1.schemas.role_schema import RoleCreate, RoleUpdate, RoleResponse

logger = get_logger(__name__)

class RoleService:
    def __init__(self, role_repository: RoleRepository):
        self.role_repository = role_repository

    # =========================
    # GET ALL
    # =========================
    def get_roles(self, skip: int = 0, limit: int = 100) -> list[RoleResponse]:
        logger.info('Retrieving role list.')
        return self.role_repository.get_all(skip=skip, limit=limit)
    
    # =========================
    # GET BY ID
    # =========================    
    def get_role(self, role_id: int) -> RoleResponse:
        logger.info(f'Searching for role with ID: {role_id}.')
        role = self.role_repository.get_by_id(role_id)
        if not role:
            logger.warning(f'Role with ID: {role_id} not found.')
            raise NotFoundError(f'Category with ID: {role_id} not found.')
        return role

    # =========================
    # CREATE
    # =========================
    def create_role(self, role_data: RoleCreate) -> RoleResponse:
        logger.info(f'Creating role with name: {role_data.name}.')
        existing = self.role_repository.get_by_name(role_data.name)
        if existing:
            logger.error(f'Role with name: {role_data.name} already exists.')
            raise ConflictError(f'Role with name: {role_data.name} already exists.')
        role = Role(
            name=role_data.name,
            description=role_data.description
        )
        return self.role_repository.create(role)

    # =========================
    # UPDATE
    # =========================
    def update_role(self, role_id: int, role_data: RoleUpdate) -> RoleResponse:
        logger.info(f'Updating role with ID: {role_id}.')
        existing = self.role_repository.get_by_id(role_id)
        if not existing:
            logger.warning(f'Category with ID: {role_id} not found.')
            raise NotFoundError(f'Category with ID: {role_id} not found.')
        updated_role = Role(
            id=role_id,
            name=role_data.name or existing.name,
            description=role_data.description or existing.description
        )
        return self.role_repository.update(role_id, updated_role)
    
    # =========================
    # DELETE
    # =========================
    def delete_role(self, role_id: int) -> bool:
        logger.info(f'Deleting role with ID: {role_id}.')
        role = self.role_repository.get_by_id(role_id)
        if not role:
            logger.warning(f'Role with ID: {role_id} not found.')
            raise NotFoundError(f'Category with ID: {role_id} not found.')
        return self.role_repository.delete(role_id)