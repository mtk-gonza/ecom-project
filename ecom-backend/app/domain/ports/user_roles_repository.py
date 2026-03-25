from abc import ABC, abstractmethod
from app.domain.entities.user_roles import UserRoles

class UserRolesRepository(ABC):

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> list[UserRoles]: ...

    @abstractmethod
    def get_by_id(self, user_roles_id: int) -> UserRoles | None: ...

    @abstractmethod
    def create(self, user_roles: UserRoles) -> UserRoles: ...

    @abstractmethod
    def update(self, user_roles_id: int, user: UserRoles) -> UserRoles: ...
    
    @abstractmethod
    def delete(self, user_roles_id: int) -> None: ...