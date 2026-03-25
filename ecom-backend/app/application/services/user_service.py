from app.core.ports.user_repository import UserRepository
from app.core.entities.user_entity import User
from typing import List, Optional

class RegisterUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user: User) -> User:
        return await self.repository.create(user)

class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user: User) -> User:
        # Ejemplo de validación del dominio
        if not user.name:
            raise ValueError("El producto debe tener nombre")
        return await self.repository.create(user)

class GetUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user_id: int) -> Optional[User]:
        return await self.repository.get_by_id(user_id)

class ListUsersUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self) -> List[User]:
        return await self.repository.list()

class UpdateUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user: User) -> User:
        return await self.repository.update(user)

class DeleteUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user_id: int) -> None:
        await self.repository.delete(user_id)