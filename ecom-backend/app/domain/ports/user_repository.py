from abc import ABC, abstractmethod
from app.domain.entities.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> list[User]: ...

    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None: ...

    @abstractmethod
    def get_by_username(self, username: str) -> User | None: ...

    @abstractmethod
    def create(self, user: User) -> User: ...

    @abstractmethod
    def update(self, user_id: int, user: User) -> User: ...
    
    @abstractmethod
    def delete(self, user_id: int) -> None: ...