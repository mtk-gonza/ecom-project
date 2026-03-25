from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from app.application.exceptions import ValidationError


@dataclass
class Role:
    id: Optional[int]
    name: str
    description: Optional[str] = None
    # 🔹 Relaciones (solo IDs)
    user_ids: List[int] = field(default_factory=list)
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.name:
            raise ValidationError("El nombre del rol es obligatorio")

        if not isinstance(self.user_ids, list):
            raise ValidationError("user_ids debe ser una lista")

        for uid in self.user_ids:
            if not isinstance(uid, int):
                raise ValidationError("Todos los user_ids deben ser enteros")