from pydantic import BaseModel
from datetime import datetime
from app.domain.enums.entity_type import EntityType
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema

# =========================
# BASE
# =========================
class SpecificationBase(BaseModel):
    entity_id: int
    entity_type: EntityType
    name: str
    value: str 

# =========================
# CREATE
# =========================
class SpecificationCreate(SpecificationBase):
    pass

# =========================
# UPDATE
# =========================
class SpecificationUpdate(SpecificationBase):
    pass

# =========================
# RESPONSE
# =========================
class SpecificationResponse(SpecificationBase, IDSchema, TimestampSchema):
    pass

# =========================
# DELETE
# =========================
class SpecificationDeleteResponse(BaseModel):
    success: bool
    detail: str