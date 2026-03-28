from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional, TYPE_CHECKING
from app.domain.enums import Currency, ProductStatus
from app.domain.exceptions import ValidationError
from app.domain.entities.specification import Specification
from app.domain.entities.image import Image

if TYPE_CHECKING:
    from app.domain.entities.license import License
    from app.domain.entities.category import Category

@dataclass
class Product:
    id: Optional[int]
    sku: str
    slug: str
    name: str
    description: Optional[str]
    price: Decimal
    currency: Currency = Currency.ARS
    cost_price: Optional[Decimal] = None
    discount: Decimal = Decimal("0")
    stock: int = 0
    barcode: Optional[str] = None
    installments: Optional[int] = None
    special: bool = False
    is_featured: bool = False
    status: ProductStatus = ProductStatus.ACTIVE
    # 🔹 Relaciones (IDs)
    license_id: Optional[int] = None
    category_id: Optional[int] = None
    license: Optional['License'] = None
    category: Optional['Category'] = None
    # 🔹 Datos flexibles
    specifications: List[Specification] = field(default_factory=list)
    images: List[Image] = field(default_factory=list)
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.name:
            raise ValidationError("El nombre es obligatorio")

        if not self.sku:
            raise ValidationError("El SKU es obligatorio")

        if not self.slug:
            raise ValidationError("El slug es obligatorio")

        if self.price < 0:
            raise ValidationError("El precio no puede ser negativo")

        if self.cost_price is not None and self.cost_price < 0:
            raise ValidationError("El costo no puede ser negativo")

        if self.discount < 0 or self.discount > 100:
            raise ValidationError("El descuento debe estar entre 0 y 100")

        if self.stock < 0:
            raise ValidationError("El stock no puede ser negativo")

        if not isinstance(self.status, ProductStatus):
            raise ValidationError("Estado inválido")

        if not isinstance(self.currency, Currency):
            raise ValidationError("Moneda inválida")