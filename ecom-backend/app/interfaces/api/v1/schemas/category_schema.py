from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.interfaces.api.v1.schemas.product_schema import ProductResponseSchema

class CategoryBaseSchema(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreateSchema(CategoryBaseSchema):
    pass

class CategoryUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryResponseSchema(CategoryBaseSchema):
    id: int
    products: Optional[List[ProductResponseSchema]] = []
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}