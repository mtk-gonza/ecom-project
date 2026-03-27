from datetime import timedelta
from app.infrastructure.logging.logger import get_logger
from app.infrastructure.security.jwt_handler import create_access_token
from app.infrastructure.security.password_handler import verify_password
from app.domain.ports.user_repository import UserRepository
from app.domain.exceptions import ValidationError
from app.config.settings import settings

logger = get_logger(__name__)

class AuthService:
    def __init__(self, repository: UserRepository):
        self.user_repository = repository

    def login(self, username: str, password: str) -> str:
        logger.info(f"Login attempt for user: {username}")

        user = self.user_repository.get_by_username(username)

        if not user:
            logger.warning(f"User not found: {username}")
            raise ValidationError("Invalid credentials")

        if not verify_password(password, user.password):
            logger.warning(f"Incorrect password for user: {username}")
            raise ValidationError("Invalid credentials")

        roles = [role.name for role in user.roles]

        expires = timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS)

        token = create_access_token(
            user.id,
            user.username,
            roles,
            expires
        )

        logger.info(f"User authenticated successfully: {username}")
        return token