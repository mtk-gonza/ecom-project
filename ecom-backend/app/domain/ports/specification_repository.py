from abc import ABC, abstractmethod
from app.domain.entities.specification import Specification

class SpecificationRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[Specification]: ...

    @abstractmethod
    async def get_by_id(self, specification_id: int) -> Specification | None: ...

    @abstractmethod
    async def create(self, specification: Specification) -> Specification: ...

    @abstractmethod
    async def update(self, specicication: Specification) -> Specification: ...

    @abstractmethod
    async def delete(self, specification_id: int) -> None: ...