from pydantic import BaseModel
from datetime import datetime
from src.domain.enums.entity_type import EntityType

class SpecificationBase(BaseModel):
    entity_id: int
    entity_type: EntityType
    name: str
    value: str 

class SpecificationCreate(SpecificationBase):
    created_at: datetime

class SpecificationUpdate(SpecificationBase):
    updated_at: datetime

class SpecificationResponse(SpecificationBase):
    id: int
    created_at: datetime
    updated_at: datetime
    product_id: int
    class Config:
        from_attributes = True

class SpecificationDelete(BaseModel):
    message: str