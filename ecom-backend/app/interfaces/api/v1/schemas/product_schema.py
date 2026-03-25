from pydantic import BaseModel, field_validator
from typing import List, Optional
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

    @field_validator("price")
    def validate_price(cls, v):
        if v < 0:
            raise ValueError("Precio inválido")
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
    specifications: Optional[List[dict]] = None


class ProductResponseSchema(ProductBaseSchema):
    id: int
    slug: str

    images: List[str]
    specifications: List[dict]

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class ProductDeleteResponseSchema(BaseModel):
    success: bool
    detail: str