from abc import ABC, abstractmethod
from app.domain.entities.specification import Specification

class SpecificationRepository(ABC):

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> list[Specification]: ...

    @abstractmethod
    def get_by_id(self, specification_id: int) -> Specification | None: ...

    @abstractmethod
    def create(self, specification: Specification) -> Specification: ...

    @abstractmethod
    def update(self, specicication: Specification) -> Specification: ...

    @abstractmethod
    def delete(self, specification_id: int) -> bool: ...