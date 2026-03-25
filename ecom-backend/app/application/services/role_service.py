from app.core.ports.role_repository import RoleRepository
from app.core.entities.role_entity import Role
from typing import List, Optional

class CreateRoleUseCase:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    async def execute(self, role: Role) -> Role:
        # Ejemplo de validación del dominio
        if not role.name:
            raise ValueError("El producto debe tener nombre")
        return await self.repository.create(role)

class GetRoleUseCase:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    async def execute(self, role_id: int) -> Optional[Role]:
        return await self.repository.get_by_id(role_id)

class ListRolesUseCase:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    async def execute(self) -> List[Role]:
        return await self.repository.list()

class UpdateRoleUseCase:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    async def execute(self, role: Role) -> Role:
        return await self.repository.update(role)

class DeleteRoleUseCase:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    async def execute(self, role_id: int) -> None:
        await self.repository.delete(role_id)
