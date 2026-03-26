from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from app.domain.enums import EntityType, ImageType
from app.domain.exceptions import ValidationError


@dataclass
class Image:
    id: Optional[int]
    path: str
    entity_id: int
    entity_type: EntityType
    image_type: ImageType = ImageType.FRONT
    is_primary: bool = False
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.path:
            raise ValidationError("La ruta de la imagen es obligatoria")

        if not isinstance(self.entity_type, EntityType):
            raise ValidationError("entity_type inválido")

        if not isinstance(self.entity_id, int) or self.entity_id <= 0:
            raise ValidationError("entity_id debe ser un entero positivo")

        if not isinstance(self.is_primary, bool):
            raise ValidationError("is_primary debe ser booleano")