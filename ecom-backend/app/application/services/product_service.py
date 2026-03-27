from app.infrastructure.logging.logger import get_logger
from app.domain.ports.product_repository import ProductRepository
from app.domain.entities.product import Product
from app.domain.exceptions import NotFoundError, ConflictError
from app.interfaces.api.v1.schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse

logger = get_logger(__name__)

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    # =========================
    # GET ALL
    # =========================
    def get_products(self, skip: int = 0, limit: int = 100) -> list[ProductResponse]:
        logger.info('Retrieving product list.')
        return self.product_repository.get_all(skip=skip, limit=limit)

    # =========================
    # GET BY ID
    # =========================
    def get_product(self, product_id: int) -> ProductResponse:
        logger.info(f'Searching for product with ID: {product_id}.')
        product = self.product_repository.get_by_id(product_id)
        if not product:
            logger.warning(f'Product with ID: {product_id} not found.')
            raise NotFoundError(f'Product with ID: {product_id} not found.')
        return product

    # =========================
    # CREATE
    # =========================
    def create_product(self, product_data: ProductCreate):
        logger.info(f'Creating product with sku: {product_data.sku}.')
        product = Product(
            id=None,
            sku=product_data.sku,
            slug=product_data.slug,
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            currency=product_data.currency,
            cost_price=product_data.cost_price,
            discount=product_data.discount,
            stock=product_data.stock,
            barcode=product_data.barcode,
            installments=product_data.installments,
            special=product_data.special,
            is_featured=product_data.is_featured,
            status=product_data.status,
            licence_id=product_data.licence_id,
            category_id=product_data.category_id,
            images=product_data.images or [],
            specifications=product_data.specifications or []
        )
        logger.info(f'New product created with SKU: {product_data.sku}')
        return self.product_repository.create(product)

    # =========================
    # UPDATE
    # =========================
    def update_product(self, product_id: int, product_data: ProductUpdate):
        logger.info(f'Updating product with ID: {product_id}.')
        existing = self.product_repository.get_by_id(product_id)
        if not existing:
            logger.warning(f'Product with ID: {product_id} not found.')
            raise NotFoundError(f'Product with ID: {product_id} not found.')
        updated_product = Product(
            id=existing.id,
            sku=product_data.sku or existing.sku,
            slug=product_data.slug or existing.slug,
            name=product_data.name or existing.name,
            description=product_data.description or existing.description,
            price=product_data.price if product_data.price is not None else existing.price,
            currency=product_data.currency or existing.currency,
            cost_price=product_data.cost_price if product_data.cost_price is not None else existing.cost_price,
            discount=product_data.discount if product_data.discount is not None else existing.discount,
            stock=product_data.stock if product_data.stock is not None else existing.stock,
            barcode=product_data.barcode or existing.barcode,
            installments=product_data.installments if product_data.installments is not None else existing.installments,
            special=product_data.special if product_data.special is not None else existing.special,
            is_featured=product_data.is_featured if product_data.is_featured is not None else existing.is_featured,
            status=product_data.status or existing.status,
            licence_id=product_data.licence_id if product_data.licence_id is not None else existing.licence_id,
            category_id=product_data.category_id if product_data.category_id is not None else existing.category_id,
            images=product_data.images if product_data.images is not None else existing.images,
            specifications=product_data.specifications if product_data.specifications is not None else existing.specifications,
            created_at=existing.created_at,
            updated_at=existing.updated_at
        )
        return self.product_repository.update(updated_product)

    # =========================
    # DELETE
    # =========================
    def delete_product(self, product_id: int) -> bool:
        logger.info(f'Deleting product with ID: {product_id}.')
        existing = self.product_repository.get_by_id(product_id)
        if not existing:
            logger.warning(f'Product with ID: {product_id} not found.')
            raise NotFoundError(f'Product with ID: {product_id} not found.')
        return self.product_repository.delete(product_id)