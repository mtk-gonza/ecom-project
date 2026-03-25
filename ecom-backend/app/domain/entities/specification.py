from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from app.application.exceptions import ValidationError


@dataclass
class Specification:
    # 🔹 Identidad
    id: Optional[int]

    # 🔹 Asociación polimórfica
    entity_type: str
    entity_id: int

    # 🔹 Datos
    key: str
    value: str

    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.entity_type:
            raise ValidationError("El tipo de entidad es obligatorio")

        if not isinstance(self.entity_id, int) or self.entity_id <= 0:
            raise ValidationError("entity_id debe ser un entero positivo")

        if not self.key:
            raise ValidationError("La clave de la especificación es obligatoria")

        if not self.value:
            raise ValidationError("El valor de la especificación es obligatorio")