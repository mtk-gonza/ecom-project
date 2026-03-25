from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from app.application.exceptions import ValidationError


@dataclass
class License:
    # 🔹 Identidad
    id: Optional[int]

    # 🔹 Información básica
    name: str
    description: Optional[str] = None
    slug: Optional[str] = None

    # 🔹 Relaciones (solo IDs en dominio)
    product_ids: List[int] = field(default_factory=list)
    image_ids: List[int] = field(default_factory=list)

    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.name:
            raise ValidationError("El nombre de la licencia es obligatorio")

        if self.slug is not None and not self.slug:
            raise ValidationError("El slug no puede ser vacío")

        if not isinstance(self.product_ids, list):
            raise ValidationError("product_ids debe ser una lista")

        if not isinstance(self.image_ids, list):
            raise ValidationError("image_ids debe ser una lista")

        for pid in self.product_ids:
            if not isinstance(pid, int):
                raise ValidationError("Todos los product_ids deben ser enteros")

        for iid in self.image_ids:
            if not isinstance(iid, int):
                raise ValidationError("Todos los image_ids deben ser enteros")