from app.core.ports.product_spec_repository import ProductSpecRepository
from app.core.entities.product_specification_entity import ProductSpecification
from typing import List, Optional

class CreateProductSpecificationUseCase:
    def __init__(self, repository: ProductSpecRepository):
        self.repository = repository

    async def execute(self, product_specification: ProductSpecification) -> ProductSpecification:
        # Ejemplo de validación del dominio
        if not product_specification.name:
            raise ValueError("El producto debe tener nombre")
        return await self.repository.create(product_specification)

class GetProductSpecificationUseCase:
    def __init__(self, repository: ProductSpecRepository):
        self.repository = repository

    async def execute(self, product_specification_id: int) -> Optional[ProductSpecification]:
        return await self.repository.get_by_id(product_specification_id)

class ListProductSpecificationsUseCase:
    def __init__(self, repository: ProductSpecRepository):
        self.repository = repository

    async def execute(self) -> List[ProductSpecification]:
        return await self.repository.list()

class UpdateProductSpecificationUseCase:
    def __init__(self, repository: ProductSpecRepository):
        self.repository = repository

    async def execute(self, product: ProductSpecification) -> ProductSpecification:
        return await self.repository.update(product)

class DeleteProductSpecificationUseCase:
    def __init__(self, repository: ProductSpecRepository):
        self.repository = repository

    async def execute(self, product_specification_id: int) -> None:
        await self.repository.delete(product_specification_id)
