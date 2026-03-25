from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from app.application.exceptions import ValidationError


@dataclass
class Category:
    # 🔹 Identidad
    id: Optional[int]

    # 🔹 Información básica
    name: str
    description: Optional[str] = None

    # 🔹 Relaciones (solo IDs en dominio idealmente)
    product_ids: List[int] = field(default_factory=list)

    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.name:
            raise ValidationError("El nombre de la categoría es obligatorio")

        if not isinstance(self.product_ids, list):
            raise ValidationError("product_ids debe ser una lista")

        for pid in self.product_ids:
            if not isinstance(pid, int):
                raise ValidationError("Todos los product_ids deben ser enteros")