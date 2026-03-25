from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional, Dict
from app.domain.enums import Currency, ProductStatus
from app.application.exceptions import ValidationError


@dataclass
class Product:
    # 🔹 Identidad
    id: Optional[int]
    sku: str
    slug: str
    # 🔹 Información básica
    name: str
    description: Optional[str]
    # 🔹 Pricing
    price: Decimal
    currency: Currency.ARS
    cost_price: Optional[Decimal] = None
    discount: Decimal = Decimal("0")
    # 🔹 Stock
    stock: int = 0
    # 🔹 Identificadores externos
    barcode: Optional[str] = None
    # 🔹 Comercial
    installments: Optional[int] = None
    special: bool = False
    is_featured: bool = False
    # 🔹 Estado
    status: ProductStatus.ACTIVE  # active, inactive, draft, archived
    # 🔹 Relaciones (IDs)
    licence_id: Optional[int] = None
    category_id: Optional[int] = None
    # 🔹 Datos flexibles
    specifications: List[Dict[str, str]] = field(default_factory=list)
    images: List[str] = field(default_factory=list)
    # 🔹 Auditoría
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # =========================
    # 🔒 VALIDACIONES DE DOMINIO
    # =========================
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

        if self.status not in {"active", "inactive", "draft", "archived"}:
            raise ValidationError("Estado inválido")
        
    # =========================
    # 💰 MÉTODOS DE NEGOCIO
    # =========================
    def price_with_discount(self) -> Decimal:
        return self.price - (self.price * self.discount / Decimal("100"))

    def profit_margin(self) -> Optional[Decimal]:
        if self.cost_price is None:
            return None
        return self.price - self.cost_price
    
    # =========================
    # 📦 STOCK
    # =========================
    def is_in_stock(self) -> bool:
        return self.stock > 0

    def increase_stock(self, amount: int):
        if amount <= 0:
            raise ValidationError("Cantidad inválida")
        self.stock += amount

    def decrease_stock(self, amount: int):
        if amount <= 0:
            raise ValidationError("Cantidad inválida")

        if self.stock < amount:
            raise ValidationError("Stock insuficiente")
        self.stock -= amount

    # =========================
    # 🏷️ DESCUENTOS
    # =========================
    def apply_discount(self, percentage: Decimal):
        if percentage < 0 or percentage > 100:
            raise ValidationError("Descuento inválido")
        self.discount = percentage

    def remove_discount(self):
        self.discount = Decimal("0")

    # =========================
    # 🔄 ESTADO
    # =========================
    def activate(self):
        self.status = "active"

    def deactivate(self):
        self.status = "inactive"

    def archive(self):
        self.status = "archived"

    # =========================
    # 🧠 HELPERS
    # =========================
    def is_active(self) -> bool:
        return self.status == "active"

    def is_discounted(self) -> bool:
        return self.discount > 0