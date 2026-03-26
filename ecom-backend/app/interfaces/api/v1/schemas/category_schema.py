from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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
class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

# =========================
# DELETE
# =========================
class CategoryDeleteResponse(BaseModel):
    success: bool
    detail: str