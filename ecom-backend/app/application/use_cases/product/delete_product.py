from app.domain.ports.product_repository import ProductRepository
from app.application.exceptions import NotFoundError


class DeleteProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: int) -> None:
        # 🔹 1. Verificar existencia
        product = self.repository.get_by_id(product_id)

        if not product:
            raise NotFoundError("Producto no encontrado")

        # 🔹 2. Eliminar
        self.repository.delete(product_id)