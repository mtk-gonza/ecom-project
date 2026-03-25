from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.image_schema import ImageResponse, ImageCreate
class LicenceBase(BaseModel):
    name: str
    description: Optional[str]
    images: Optional[List[ImageResponse]] = []

class LicenceCreate(BaseModel):
    name: str
    description: Optional[str]

class LicenceUpdate(LicenceBase):
    pass

class LicenceResponse(LicenceBase):
    id: int 
    created_at: datetime 
    updated_at: datetime 
    class Config:
        from_attributes = True