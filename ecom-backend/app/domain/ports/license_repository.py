from abc import ABC, abstractmethod
from app.domain.entities.license import License

class LicenseRepository(ABC):

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> list[License]: ...

    @abstractmethod
    def get_by_id(self, license_id: int) -> License | None: ...
    
    @abstractmethod
    def get_by_name(self, name: str) -> License | None: ...

    @abstractmethod
    def create(self, license: License) -> License: ...

    @abstractmethod
    def update(self, license_id: int, license: License) ->  License: ...

    @abstractmethod
    def delete(self, license_id: int) -> None: ...
