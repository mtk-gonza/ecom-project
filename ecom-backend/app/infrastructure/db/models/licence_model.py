from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship, foreign
from sqlalchemy.sql import and_
from app.infrastructure.db.base import Base

class Licence(Base):
    __tablename__ = 'licences'    

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    images = relationship(
        "Image",
        primaryjoin="and_(Licence.id == Image.entity_id, Image.entity_type == 'licence')",
        foreign_keys="[Image.entity_id]",
        overlaps="product_images",
        viewonly=True
    )
    products = relationship('Product', back_populates='licence')