from abc import ABC, abstractmethod
from app.domain.entities.role import Role

class RoleRepository(ABC):

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> list[Role]: ...

    @abstractmethod
    async def get_by_id(self, role_id: int) -> Role | None: ...

    @abstractmethod
    async def create(self, role: Role) -> Role: ...

    @abstractmethod
    async def update(self, role: Role) -> Role: ...

    @abstractmethod
    async def delete(self, role_id: int) -> None: ...
