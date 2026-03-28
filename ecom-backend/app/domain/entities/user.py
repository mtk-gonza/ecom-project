from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from app.domain.exceptions import ValidationError


@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    password_hash: str
    first_name: str
    last_name: str
    is_active: bool = True
    is_verified: bool = False
    # 🔹 Relaciones
    roles: List[str] = field(default_factory=list)
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.username:
            raise ValidationError("El username es obligatorio")

        if not self.email:
            raise ValidationError("El email es obligatorio")

        if not self.password_hash:
            raise ValidationError("El password_hash es obligatorio")

        if not self.first_name:
            raise ValidationError("El first_name es obligatorio")

        if not self.last_name:
            raise ValidationError("El last_name es obligatorio")

        if not isinstance(self.is_active, bool):
            raise ValidationError("is_active debe ser booleano")

        if not isinstance(self.is_verified, bool):
            raise ValidationError("is_verified debe ser booleano")

    # 🔹 Método de conveniencia
    def full_name(self) -> str:
        return f"{self.first_name or ''} {self.last_name or ''}".strip()