from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from decimal import Decimal
from app.domain.enums import Currency, ProductStatus
from app.interfaces.api.v1.schemas.category_schema import CategoryResponse
from app.interfaces.api.v1.schemas.license_schema import LicenseResponse
from app.interfaces.api.v1.schemas.image_schema import ImageResponse
from app.interfaces.api.v1.schemas.specification_schema import SpecificationResponse
from app.interfaces.api.v1.schemas.base import IDSchema, TimestampSchema

# =========================
# BASE
# =========================
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(..., ge=0)
    currency: Currency = Currency.ARS
    cost_price: Optional[Decimal] = None
    stock: int = Field(0, ge=0)
    sku: str
    barcode: Optional[str] = None
    discount: Decimal = Field(0, ge=0, le=100)
    installments: Optional[int] = None
    special: bool = False
    is_featured: bool = False
    status: ProductStatus = ProductStatus.ACTIVE
    licence_id: Optional[int] = None
    category_id: Optional[int] = None


# =========================
# CREATE
# =========================
class ProductCreate(ProductBase):
    slug: str
    images: Optional[List[str]] = None
    specifications: Optional[List[Dict[str, str]]] = None


# =========================
# UPDATE
# =========================
class ProductUpdate(BaseModel):
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


# =========================
# RESPONSE
# =========================
class ProductResponse(ProductBase, IDSchema, TimestampSchema):
    slug: str
    category: Optional[CategoryResponse] = None
    license: Optional[LicenseResponse] = None
    images: List[ImageResponse] = Field(default_factory=list)
    specifications: List[SpecificationResponse] = Field(default_factory=list)


# =========================
# DELETE
# =========================
class ProductDeleteResponse(BaseModel):
    success: bool
    detail: str