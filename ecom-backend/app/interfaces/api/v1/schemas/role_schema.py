from pydantic import BaseModel
from typing import Optional
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema

# =========================
# BASE
# =========================
class RoleBase(BaseModel):
    name: str
    description: Optional[str]

# =========================
# CREATE
# =========================
class RoleCreate(RoleBase):
    pass

# =========================
# UPDATE
# =========================
class RoleUpdate(RoleBase):
    pass

# =========================
# RESPONSE
# =========================
class RoleResponse(RoleBase, IDSchema, TimestampSchema):
    pass

# =========================
# DELETE
# =========================
class RoleDelete(BaseModel):
    success: bool
    detail: str