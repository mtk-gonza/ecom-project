from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship, foreign
from sqlalchemy.sql import and_
from app.infrastructure.db.base import Base

class LicenseModel(Base):
    __tablename__ = 'licenses'    

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    images = relationship(
        "Image",
        primaryjoin="and_(License.id == Image.entity_id, Image.entity_type == 'license')",
        foreign_keys="[Image.entity_id]",
        overlaps="product_images",
        viewonly=True
    )
    products = relationship('ProductModel', back_populates='license')