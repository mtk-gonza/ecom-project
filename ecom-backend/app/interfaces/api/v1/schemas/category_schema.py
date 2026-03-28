from pydantic import BaseModel
from typing import Optional, List
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema

# =========================
# BASE
# =========================
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

# =========================
# CREATE
# =========================
class CategoryCreate(CategoryBase):
    pass

# =========================
# UPDATE
# =========================
class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

# =========================
# RESPONSE
# =========================
class CategoryResponse(CategoryBase, IDSchema, TimestampSchema):
    id: int
    products: List["ProductResponseSummary"] = [] # type: ignore
    model_config = {"from_attributes": True}

class CategoryResponseSummary(BaseModel):
    name: str
    description: Optional[str] = None
    model_config = {"from_attributes": True}


# =========================
# DELETE
# =========================
class CategoryDeleteResponse(BaseModel):
    success: bool
    detail: str