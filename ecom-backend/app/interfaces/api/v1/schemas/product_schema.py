from app.interfaces.api.v1.schemas.base_schema import BaseResponseSchema
from pydantic import BaseModel, field_validator
from typing import List, Optional, Dict
from decimal import Decimal
from datetime import datetime
from app.domain.enums import Currency, ProductStatus

class ProductBaseSchema(BaseModel):
    name: str
    description: Optional[str] = None

    price: Decimal
    currency: Currency = Currency.ARS
    cost_price: Optional[Decimal] = None

    stock: int = 0
    sku: str
    barcode: Optional[str] = None

    discount: Decimal = Decimal("0")
    installments: Optional[int] = None

    special: bool = False
    is_featured: bool = False
    status: ProductStatus = ProductStatus.ACTIVE

    licence_id: Optional[int] = None
    category_id: Optional[int] = None

class ProductCreateSchema(ProductBaseSchema):
    slug: str
    images: Optional[List[str]] = []
    specifications: Optional[List[Dict[str, str]]] = []

    @field_validator("price")
    def validate_price(cls, v):
        if v < 0:
            raise ValueError("Precio inválido")
        return v

    @field_validator("discount")
    def validate_discount(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Descuento inválido")
        return v

    @field_validator("stock")
    def validate_stock(cls, v):
        if v < 0:
            raise ValueError("Stock inválido")
        return v

class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    currency: Optional[Currency] = None
    cost_price: Optional[Decimal] = None
    stock: Optional[int] = None
    sku: Optional[str] = None
    barcode: Optional[str] = None
    discount: Optional[Decimal] = None
    installments: Optional[int] = None
    special: Optional[bool] = None
    is_featured: Optional[bool] = None
    status: Optional[ProductStatus] = None
    licence_id: Optional[int] = None
    category_id: Optional[int] = None
    slug: Optional[str] = None
    images: Optional[List[str]] = None
    specifications: Optional[List[Dict[str, str]]] = None

class ProductResponseSchema(BaseResponseSchema):
    id: int
    slug: str
    name: str
    description: str
    price: Decimal
    currency: Currency
    cost_price: Decimal
    stock: int
    sku: str
    barcode: str
    discount: Decimal
    installments: int
    special: bool
    is_featured: bool
    status: ProductStatus
    licence_id: int
    category_id: int
    images: List[str] = []
    specifications: List[Dict[str, str]] = []

class ProductDeleteResponseSchema(BaseModel):
    success: bool
    detail: str