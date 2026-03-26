from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.interfaces.api.v1.schemas.image_schema import ImageResponse, ImageCreate

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
class LicenseResponse(LicenseBase):
    id: int 
    created_at: datetime 
    updated_at: datetime

    model_config = {"from_attributes": True}

# =========================
# DELETE
# =========================
class LicenseDeleteResponse(BaseModel):
    success: bool
    detail: str