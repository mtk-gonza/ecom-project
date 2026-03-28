from sqlalchemy import Column, Integer, String, DateTime, func, and_
from sqlalchemy.orm import relationship, foreign
from sqlalchemy.sql import and_
from app.infrastructure.db.base import Base
from app.infrastructure.db.models.image_model import ImageModel
from app.domain.enums import EntityType

class LicenseModel(Base):
    __tablename__ = 'licenses'    
    # 🔹 Identidad
    id = Column(Integer, primary_key=True, autoincrement=True)
    slug = Column(String(100), nullable=False, unique=True)

    # 🔹 Información básica
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)
    
    # 🔹 Relaciones
    products = relationship('ProductModel', back_populates='license')
    images = relationship(
        "ImageModel",
        primaryjoin=and_(
            id == ImageModel.entity_id,
            ImageModel.entity_type == EntityType.LICENSE.value
        ),
        foreign_keys=[ImageModel.entity_id],
        viewonly=True
    )

    # 🔹 Auditoría
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)