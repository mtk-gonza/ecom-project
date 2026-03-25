from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import relationship
from app.infrastructure.db.base import Base
from app.domain.enums import Currency, ProductStatus

class ProductModel(Base):
    __tablename__ = 'products'

    # 🔹 Identidad
    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String(50), nullable=False, unique=True)
    slug = Column(String(100), nullable=False, unique=True)

    # 🔹 Información básica
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=True)

    # 🔹 Pricing
    price = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    currency = Column(Enum(Currency), nullable=False, default=Currency.ARS)
    cost_price = Column(DECIMAL(10, 2), nullable=True)
    discount = Column(DECIMAL(5, 2), default=0.00)

    # 🔹 Stock
    stock = Column(Integer, nullable=False, default=0)

    # 🔹 Identificadores externos
    barcode = Column(String(100), nullable=True)

    # 🔹 Comercial
    installments = Column(Integer, nullable=True)
    special = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)

    # 🔹 Estado
    status = Column(Enum(ProductStatus), nullable=False, default=ProductStatus.ACTIVE)

    # 🔹 Relaciones
    licence_id = Column(Integer, ForeignKey('licences.id'), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    licence = relationship('Licence', back_populates='products')
    category = relationship('Category', back_populates='products')
    specifications = relationship('ProductSpecification', back_populates='product')
    images = relationship(
        "Image",
        primaryjoin="and_(Product.id == Image.entity_id, Image.entity_type == 'product')",
        foreign_keys="[Image.entity_id]",
        overlaps="licence_images",
        viewonly=True
    )

    # 🔹 Auditoría
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)