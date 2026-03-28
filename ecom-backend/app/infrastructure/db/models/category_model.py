from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.infrastructure.db.base import Base

class CategoryModel(Base):
    __tablename__ = 'categories'  

    # 🔹 Identidad
    id = Column(Integer, primary_key=True, autoincrement=True)

    # 🔹 Información básica
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)

    # 🔹 Relaciones
    products = relationship('ProductModel', back_populates='category')

    # 🔹 Auditoría
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)