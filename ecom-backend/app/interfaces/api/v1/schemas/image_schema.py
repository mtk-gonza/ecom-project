from pydantic import BaseModel
from datetime import datetime
from src.domain.enums.entity_type import EntityType
from src.domain.enums.image_type import ImageType

class ImageBase(BaseModel):
    path: str
    entity_id: int
    entity_type: EntityType
    image_type: ImageType
    is_primary: bool = True

class ImageCreate(ImageBase):
    assigned_at: datetime

class ImageResponse(ImageBase):    
    id: int
    assigned_at: datetime

    class Config:
        from_attributes = True