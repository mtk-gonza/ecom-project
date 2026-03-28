from pydantic import BaseModel
from app.domain.enums.entity_type import EntityType
from app.domain.enums.image_type import ImageType
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema

# =========================
# BASE
# =========================
class ImageBase(BaseModel):
    path: str
    entity_id: int
    entity_type: EntityType 
    image_type: ImageType = ImageType.FRONT
    is_primary: bool = True

# =========================
# CREATE
# =========================
class ImageCreate(ImageBase):
    pass

# =========================
# UPDATE
# =========================
class ImageUpdate(ImageBase):
    pass

# =========================
# RESPONSE
# =========================
class ImageResponse(ImageBase, IDSchema, TimestampSchema):
    pass
    
# =========================
# DELETE
# =========================
class ImageDeleteResponse(BaseModel):
    success: bool
    detail: str