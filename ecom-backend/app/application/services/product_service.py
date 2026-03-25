from app.domain.entities.product import Product
from app.domain.ports.product_repository import ProductRepository
from app.application.exceptions import (
    ProductNotFoundError,
    ValidationError
)
from app.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    # 🔹 GET ALL
    def get_products(self):
        logger.info("Obteniendo lista de productos")

        products = self.repository.get_all()

        logger.debug(f"Cantidad de productos obtenidos: {len(products)}")

        return products

    # 🔹 GET BY ID
    def get_product(self, product_id: int):
        logger.info(f"Buscando producto id={product_id}")

        product = self.repository.get_by_id(product_id)

        if not product:
            logger.warning(f"Producto no encontrado id={product_id}")
            raise ProductNotFoundError(product_id)

        return product

    # 🔹 CREATE
    def create_product(self, name: str, price: float):
        logger.info(f"Intentando crear producto: name={name}, price={price}")

        # Validación de negocio
        if price <= 0:
            logger.warning(f"Precio inválido para producto: price={price}")
            raise ValidationError("El precio debe ser mayor a 0")

        product = Product(id=None, name=name, price=price)

        created_product = self.repository.create(product)

        logger.info(f"Producto creado con id={created_product.id}")

        return created_product

    # 🔹 UPDATE
    def update_product(self, product_id: int, name: str, price: float):
        logger.info(f"Actualizando producto id={product_id}")

        existing_product = self.repository.get_by_id(product_id)

        if not existing_product:
            logger.warning(f"No se puede actualizar, producto no existe id={product_id}")
            raise ProductNotFoundError(product_id)

        if price <= 0:
            logger.warning(f"Precio inválido en actualización: price={price}")
            raise ValidationError("El precio debe ser mayor a 0")

        updated_product = Product(id=product_id, name=name, price=price)

        result = self.repository.update(updated_product)

        logger.info(f"Producto actualizado id={product_id}")

        return result

    # 🔹 DELETE
    def delete_product(self, product_id: int):
        logger.info(f"Eliminando producto id={product_id}")

        existing_product = self.repository.get_by_id(product_id)

        if not existing_product:
            logger.warning(f"No se puede eliminar, producto no existe id={product_id}")
            raise ProductNotFoundError(product_id)

        self.repository.delete(product_id)

        logger.info(f"Producto eliminado id={product_id}")