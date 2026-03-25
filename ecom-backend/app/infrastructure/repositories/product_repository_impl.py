from sqlalchemy.orm import Session
from app.domain.entities.product import Product
from app.domain.ports.product_repository import ProductRepository
from app.infrastructure.db.models.product_model import ProductModel
from app.infrastructure.mappers.product_mapper import to_domain, to_model


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        models = self.db.query(ProductModel).all()
        return [to_domain(m) for m in models]

    def get_by_id(self, product_id: int):
        model = (
            self.db.query(ProductModel)
            .filter(ProductModel.id == product_id)
            .first()
        )
        return to_domain(model) if model else None

    def create(self, product: Product):
        model = to_model(product)

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return to_domain(model)

    def update(self, product: Product):
        model = self.db.query(ProductModel).filter(ProductModel.id == product.id).first()

        if not model:
            return None

        updated_model = to_model(product)

        for attr in vars(updated_model):
            if attr != "id":
                setattr(model, attr, getattr(updated_model, attr))

        self.db.commit()
        self.db.refresh(model)

        return to_domain(model)

    def delete(self, product_id: int):
        model = (
            self.db.query(ProductModel)
            .filter(ProductModel.id == product_id)
            .first()
        )

        if model:
            self.db.delete(model)
            self.db.commit()