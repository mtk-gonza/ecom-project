from pydantic import BaseModel
from typing import Optional, List
from app.interfaces.api.v1.schemas.image_schema import ImageResponse, ImageCreate
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema

# =========================
# BASE
# =========================
class LicenseBase(BaseModel):
    name: str
    description: Optional[str]
    images: Optional[List[ImageResponse]] = []

# =========================
# CREATE
# =========================
class LicenseCreate(LicenseBase):
    pass

# =========================
# UPDATE
# =========================
class LicenseUpdate(LicenseBase):
    pass

# =========================
# RESPONSE
# =========================
class LicenseResponse(LicenseBase, IDSchema, TimestampSchema):
    pass

# =========================
# DELETE
# =========================
class LicenseDeleteResponse(BaseModel):
    success: bool
    detail: str