from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from app.application.exceptions import ValidationError


@dataclass
class Image:
    # 🔹 Identidad
    id: Optional[int]

    # 🔹 Información básica
    path: str

    # 🔹 Asociación genérica (polimórfica)
    entity_type: str
    entity_id: int

    # 🔹 Metadata
    image_type: Optional[str] = None
    is_primary: bool = False

    # 🔹 Auditoría
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.path:
            raise ValidationError("La ruta de la imagen es obligatoria")

        if not self.entity_type:
            raise ValidationError("El tipo de entidad es obligatorio")

        if not isinstance(self.entity_id, int) or self.entity_id <= 0:
            raise ValidationError("entity_id debe ser un entero positivo")

        if not isinstance(self.is_primary, bool):
            raise ValidationError("is_primary debe ser booleano")