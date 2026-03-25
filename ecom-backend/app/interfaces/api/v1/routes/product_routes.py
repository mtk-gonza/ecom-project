from fastapi import APIRouter, Depends
from app.interfaces.api.v1.schemas.product_schema import (
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductResponseSchema,
    ProductDeleteResponseSchema
)
from app.application.services.product_service import ProductService

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post("/", response_model=ProductResponseSchema)
def create_product(data: ProductCreateSchema):
    product = ProductService.create_product(
        name=data.name,
        price=data.price,
        sku=data.sku,
        stock=data.stock,
        slug=data.slug
    )
    return product


@product_router.get("/", response_model=list[ProductResponseSchema])
def get_products():
    return ProductService.get_products()

@product_router.get("/{product_id}", response_model=ProductResponseSchema)
def get_product(product_id: int):
    return ProductService.get_product(product_id)

@product_router.put("/{product_id}", response_model=ProductResponseSchema)
def update_product(product_id: int, data: ProductUpdateSchema):
    return ProductService.update_product(
        product_id=product_id,
        name=data.name,
        price=data.price,
    )

@product_router.delete("/{product_id}", response_model=ProductDeleteResponseSchema)
def delete_product(product_id: int):
    ProductService.delete_product(product_id)

    return {
        "success": True,
        "detail": "Producto eliminado"
    }