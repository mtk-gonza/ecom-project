from sqlalchemy.orm import Session
from app.domain.entities.product import Product
from app.domain.ports.product_repository import ProductRepository
from app.infrastructure.db.models.product_model import ProductModel

class ProductRepositoryImpl(ProductRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        products = self.db.query(ProductModel).all()
        return [Product(p.id, p.name, p.price) for p in products]

    def get_by_id(self, product_id: int):
        p = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        return Product(p.id, p.name, p.price) if p else None

    def create(self, product: Product):
        db_product = ProductModel(name=product.name, price=product.price)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return Product(db_product.id, db_product.name, db_product.price)

    def update(self, product: Product):
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product.id).first()
        db_product.name = product.name
        db_product.price = product.price
        self.db.commit()
        return product

    def delete(self, product_id: int):
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if db_product:
            self.db.delete(db_product)
            self.db.commit()