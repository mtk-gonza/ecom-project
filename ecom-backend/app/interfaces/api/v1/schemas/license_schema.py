from pydantic import BaseModel, Field
from typing import Optional, List
from app.interfaces.api.v1.schemas.image_schema import ImageResponse, ImageCreate
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema


# =========================
# BASE
# =========================
class LicenseBase(BaseModel):
    name: str
    description: Optional[str] = None

# =========================
# CREATE
# =========================
class LicenseCreate(LicenseBase):
    pass

# =========================
# UPDATE
# =========================
class LicenseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

# =========================
# RESPONSE
# =========================
class LicenseResponse(LicenseBase, IDSchema, TimestampSchema):
    images: List[ImageResponse] = []
    products: List["ProductResponseSummary"] = [] # type: ignore
    model_config = {"from_attributes": True}


class LicenseResponseSummary(BaseModel):
    name: str
    description: Optional[str] = None
    model_config = {"from_attributes": True}


# =========================
# DELETE
# =========================
class LicenseDeleteResponse(BaseModel):
    success: bool
    detail: str