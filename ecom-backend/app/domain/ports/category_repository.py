from abc import ABC, abstractmethod
from app.domain.entities.category import Category

class CategoryRepository(ABC):
    
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> list[Category]: ...
    
    @abstractmethod
    def get_by_id(self, category_id: int) -> Category | None: ...
    
    @abstractmethod
    def get_by_name(self, name: str) ->  Category | None: ...
    
    @abstractmethod
    def create(self, category: Category) -> Category: ...
    
    @abstractmethod
    def update(self, category: Category) ->  Category | None: ...
    
    @abstractmethod
    def delete(self, category_id: int) -> bool: ...