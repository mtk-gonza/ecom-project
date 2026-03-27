from abc import ABC, abstractmethod
from app.domain.entities.product import Product

class ProductRepository(ABC):

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> list[Product]: ...
    
    @abstractmethod
    def get_featured(self, limit: int = 10) -> list[Product]: ...
    
    @abstractmethod
    def get_by_id(self, product_id: int) -> Product | None: ...
    
    @abstractmethod
    def get_by_sku(self, sku: str) -> Product | None: ...
    
    @abstractmethod
    def get_by_slug(self, slug: str) -> Product | None: ...
    
    @abstractmethod
    def create(self, product: Product) -> Product: ...
    
    @abstractmethod
    def update(self, product: Product) -> Product: ...
    
    @abstractmethod
    def delete(self, product_id: int) -> bool: ...