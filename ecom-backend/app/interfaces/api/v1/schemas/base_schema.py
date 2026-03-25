from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BaseResponseSchema(BaseModel):
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}