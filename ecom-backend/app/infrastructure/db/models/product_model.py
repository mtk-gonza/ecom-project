from sqlalchemy import Column, Integer, String, Float
from app.infrastructure.db.base import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    price = Column(Float)