from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.role_schema import RoleResponse

class UserBase(BaseModel):
    username: str
    email: str    
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    telefono: Optional[str] = None
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    telefono: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    roles: List[RoleResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserDeleteResponse(BaseModel):
    detail: str
