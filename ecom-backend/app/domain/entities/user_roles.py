from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from app.application.exceptions import ValidationError


@dataclass
class UserRoles:
    id: Optional[int]
    # 🔹 Relación
    user_id: int
    role_id: int
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not isinstance(self.user_id, int) or self.user_id <= 0:
            raise ValidationError("user_id debe ser un entero positivo")

        if not isinstance(self.role_id, int) or self.role_id <= 0:
            raise ValidationError("role_id debe ser un entero positivo")