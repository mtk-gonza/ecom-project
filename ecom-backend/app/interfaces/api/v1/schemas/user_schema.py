from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.interfaces.api.v1.schemas.role_schema import RoleResponse
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema

# =========================
# BASE
# =========================
class UserBase(BaseModel):
    username: str
    email: str    
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    telefono: Optional[str] = None
    is_active: Optional[bool] = True

# =========================
# CREATE
# =========================
class UserCreate(UserBase):
    password: str

# =========================
# UPDATE
# =========================
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    telefono: Optional[str] = None
    is_active: Optional[bool] = None

# =========================
# RESPONSE
# =========================
class UserResponse(UserBase, IDSchema, TimestampSchema):
    pass

# =========================
# DELETE
# =========================
class UserDeleteResponse(BaseModel):
    success: bool
    detail: str