from app.domain.ports.product_repository import ProductRepository
from app.application.dtos.product_dto import UpdateProductDTO
from app.application.exceptions import NotFoundError


class UpdateProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, dto: UpdateProductDTO):
        product = self.repository.get_by_id(dto.id)

        if not product:
            raise NotFoundError("Producto no encontrado")

        if dto.name is not None:
            product.name = dto.name

        if dto.price is not None:
            product.price = dto.price

        if dto.discount is not None:
            product.apply_discount(dto.discount)

        if dto.stock is not None:
            product.stock = dto.stock

        return self.repository.update(product)