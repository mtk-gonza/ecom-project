from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, List, Dict
from datetime import datetime
from app.domain.enums import Currency, ProductStatus


# =========================
# 📥 CREATE
# =========================
@dataclass
class CreateProductDTO:
    sku: str
    slug: str
    name: str
    price: Decimal

    # opcionales
    description: Optional[str] = None
    currency: Currency = Currency.ARS
    cost_price: Optional[Decimal] = None
    discount: Decimal = Decimal("0")
    stock: int = 0
    barcode: Optional[str] = None
    installments: Optional[int] = None
    special: bool = False
    is_featured: bool = False
    status: ProductStatus = ProductStatus.ACTIVE
    licence_id: Optional[int] = None
    category_id: Optional[int] = None

    specifications: List[Dict[str, str]] = field(default_factory=list)
    images: List[str] = field(default_factory=list)


# =========================
# 📤 UPDATE (PATCH)
# =========================
@dataclass
class UpdateProductDTO:
    id: int

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    currency: Optional[Currency] = None
    cost_price: Optional[Decimal] = None
    discount: Optional[Decimal] = None
    stock: Optional[int] = None
    barcode: Optional[str] = None
    installments: Optional[int] = None
    special: Optional[bool] = None
    is_featured: Optional[bool] = None
    status: Optional[ProductStatus] = None
    licence_id: Optional[int] = None
    category_id: Optional[int] = None
    
    # ⚠️ relaciones complejas (opcional manejarlas aparte)
    specifications: Optional[List[Dict[str, str]]] = None
    images: Optional[List[str]] = None


# =========================
# 📦 RESPONSE
# =========================
@dataclass
class ProductResponseDTO:
    id: int
    sku: str
    slug: str
    name: str
    description: Optional[str]
    price: Decimal
    currency: Currency
    cost_price: Optional[Decimal]
    discount: Decimal
    stock: int
    barcode: Optional[str]
    installments: Optional[int]
    special: bool
    is_featured: bool
    status: ProductStatus
    licence_id: Optional[int]
    category_id: Optional[int]

    specifications: List[Dict[str, str]]
    images: List[str]

    created_at: datetime
    updated_at: datetime