from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
from app.domain.exceptions import ValidationError
from app.domain.entities.product import Product


@dataclass
class Category:
    id: Optional[int]
    name: str
    description: Optional[str] = None
    products: List[Product]  = field(default_factory=list)
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.name:
            raise ValidationError("El nombre de la categoría es obligatorio")