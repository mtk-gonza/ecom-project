from app.infrastructure.logging.logger import get_logger
from app.domain.ports.user_repository import UserRepository
from app.domain.entities.user import User
from app.domain.exceptions import NotFoundError, ConflictError
from app.interfaces.api.v1.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.infrastructure.security.password_handler import hash_password

logger = get_logger(__name__)

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    # =========================
    # GET ALL
    # =========================
    def get_users(self, skip: int = 0, limit: int = 100) -> list[UserResponse]:
        logger.info('Retrieving user list.')
        return self.user_repository.get_all(skip=skip, limit=limit)

    # =========================
    # GET BY ID
    # =========================
    def get_user(self, user_id: int) -> UserResponse:
        logger.info(f'Searching for user with ID: {user_id}.')
        user = self.user_repository.get_by_id(user_id)
        if not user:
            logger.warning(f'User with ID: {user_id} not found.')
            raise NotFoundError(f'User with ID: {user_id} not found.')
        return user

    # =========================
    # CREATE
    # =========================
    def create_user(self, user_data: UserCreate) -> UserResponse:
        logger.info(f'Creating user with username: {user_data.username}.')
        password_hash = hash_password(user_data.password)
        user = User(
            id=None,
            username=user_data.username,
            email=user_data.email,
            password_hash=password_hash,
            first_name=user_data.first_name,
            last_name=user_data.last_name
        )
        logger.info(f'New product created with SKU: {user_data.sku}')
        return self.user_repository.create(user)

    # =========================
    # UPDATE
    # =========================
    def update_user(self, user_id: int, user_data: UserUpdate):
        logger.info(f'Updating user with ID: {user_id}.')
        existing = self.user_repository.get_by_id(user_id)
        if not existing:
            logger.warning(f'Product with ID: {user_id} not found.')
            raise NotFoundError(f'Product with ID: {user_id} not found.')
        password_hash = hash_password(user_data.password)
        updated_user = User(
            id=existing.id,
            username=user_data.username or existing.username,
            email=user_data.email or existing.email,
            password_hash=password_hash or existing.password_hash,
            first_name=user_data.first_name or existing.first_name,
            last_name=user_data.last_name or existing.last_name,
            created_at=existing.created_at,
            updated_at=existing.updated_at
        )
        return self.user_repository.update(updated_user)

    # =========================
    # DELETE
    # =========================
    def delete_user(self, user_id: int) -> bool:
        logger.info(f'Deleting user with ID: {user_id}.')
        existing = self.user_repository.get_by_id(user_id)
        if not existing:
            logger.warning(f'User with ID: {user_id} not found.')
            raise NotFoundError(f'User with ID: {user_id} not found.')
        return self.user_repository.delete(user_id)