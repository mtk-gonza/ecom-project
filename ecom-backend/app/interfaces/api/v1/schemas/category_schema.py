from pydantic import BaseModel
from typing import Optional
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
    pass

# =========================
# DELETE
# =========================
class CategoryDeleteResponse(BaseModel):
    success: bool
    detail: str