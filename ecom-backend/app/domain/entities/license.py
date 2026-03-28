from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from app.domain.exceptions import ValidationError
from app.domain.entities.image import Image
from app.domain.entities.product import Product

@dataclass
class License:
    id: Optional[int]
    name: str
    description: Optional[str] = None
    slug: Optional[str] = None
    # 🔹 Relaciones
    images: List[Image] = field(default_factory=list)
    products: List[Product]  = field(default_factory=list)
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if len(self.name.strip()) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres")

        if self.slug is not None and not self.slug:
            raise ValidationError("El slug no puede ser vacío")
