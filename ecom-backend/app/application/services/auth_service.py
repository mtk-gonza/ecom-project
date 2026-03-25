import logging
from datetime import timedelta
from fastapi import HTTPException, status
from app.utils.jwt_handler import create_access_token
from app.utils.password_utils import verify_password
from app.domain.ports.user_repository import UserRepositoryPort
from app.config.settings import settings

logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self, repository: UserRepositoryPort):
        self.user_repository = repository

    async def login(self, username: str, password: str):
        logger.info(f"Login attempt for user: {username}")
        user = await self.user_repository.get_by_username(username)
        if not user:
            logger.warning(f"Login failed - user not found: {username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User could not be validated."
            )
        if not verify_password(password, user.password):
            logger.warning(f"Login failed - incorrect password for user: {username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password."
            )
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