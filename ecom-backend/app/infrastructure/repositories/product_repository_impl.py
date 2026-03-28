from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.infrastructure.logging.logger import get_logger
from app.domain.entities.product import Product
from app.domain.ports.product_repository import ProductRepository
from app.domain.exceptions import NotFoundError
from app.infrastructure.db.models.product_model import ProductModel
from app.infrastructure.mappers.product_mapper import ProductMapper

logger = get_logger(__name__)

class ProductRepositoryImpl(ProductRepository):
    def __init__(self, db: Session):
        self.db = db


    def get_all(self, skip: int = 0, limit: int = 100) -> list[Product]:
        try:
            stmt = select(ProductModel).offset(skip).limit(limit)
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [ProductMapper.to_domain(m) for m in models]
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting products: {e}')
            raise
    

    def get_featured(self, limit: int = 10) -> list[Product]:
        try:
            stmt = (
                select(ProductModel)
                .where(ProductModel.is_featured.is_(True))
                .order_by(ProductModel.created_at.desc())
                .limit(limit)
            )
            result = self.db.execute(stmt)
            models = result.scalars().all()
            return [ProductMapper.to_domain(m) for m in models]

        except SQLAlchemyError as e:
            logger.error(f'Database error getting featured products: {e}')
            raise


    def get_by_id(self, product_id: int) -> Product:
        try:
            stmt = select(ProductModel).where(ProductModel.id == product_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Product with ID: {product_id} not found.')
            return ProductMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting product with ID: {product_id} : {e}')
            raise


    def get_by_sku(self, product_sku: str):
        try:
            stmt = select(ProductModel).where(ProductModel.sku == product_sku)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Product with SKU: {product_sku} not found.')
            return ProductMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting product with SKU: {product_sku} : {e}')
            raise
    

    def get_by_slug(self, product_slug: str):
        try:
            stmt = select(ProductModel).where(ProductModel.slug == product_slug)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Product with SLUG: {product_slug} not found.')
            return ProductMapper.to_domain(model)
        
        except SQLAlchemyError as e:
            logger.error(f'Database error getting product with SLUG: {product_slug} : {e}')
            raise


    def create(self, product: Product) -> Product:
        try:
            model = ProductMapper.to_model(product)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return ProductMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f'Error creating product: {e}')
            self.db.rollback()
            raise


    def update(self, product_id: int, product_data: Product) -> Product:
        try:
            stmt = select(ProductModel).where(ProductModel.id == product_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Product with ID: {product_id} not found.')
            ProductMapper.update_model_from_domain(model, product_data)
            self.db.commit()
            self.db.refresh(model)
            return ProductMapper.to_domain(model)

        except SQLAlchemyError as e:
            logger.error(f'Error updating product with ID: {product_id} : {e}')
            self.db.rollback()
            raise


    def delete(self, product_id: int) -> bool:
        try:
            stmt = select(ProductModel).where(ProductModel.id == product_id)
            result = self.db.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise NotFoundError(f'Product with ID: {product_id} not found.')
            self.db.delete(model)
            self.db.commit()
            return True

        except SQLAlchemyError as e:
            logger.error(f'Error deleting product with ID: {product_id} : {e}')
            self.db.rollback()
            raise