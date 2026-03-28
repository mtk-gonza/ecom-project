from fastapi import APIRouter, Depends, Query, status
from typing import List, Annotated
from app.application.services.product_service import ProductService
from app.interfaces.api.v1.dependencies.services import get_product_service
from app.interfaces.api.v1.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductDeleteResponse
)

product_router = APIRouter(prefix='/products', tags=['products'])

ProductServiceDep = Annotated[ProductService, Depends(get_product_service)]

# =========================
# GET ALL
# =========================
@product_router.get('/', response_model=List[ProductResponse])
def get_products(service: ProductServiceDep, skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100)) -> List[ProductResponse]:
    return service.get_products(skip=skip, limit=limit)

# =========================
# GET BY ID
# =========================
@product_router.get('/{product_id}', response_model=ProductResponse)
def get_product(product_id: int, service: ProductServiceDep) -> ProductResponse:
    return service.get_product(product_id)

# =========================
# CREATE
# =========================
@product_router.post('/', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, service: ProductServiceDep) -> ProductResponse:
    return service.create_product(product_data)

# =========================
# UPDATE
# =========================
@product_router.put('/{product_id}', response_model=ProductResponse)
def update_product(product_id: int, product_data: ProductUpdate, service: ProductServiceDep) -> ProductResponse:
    return service.update_product(product_id, product_data)

# =========================
# DELETE
# =========================
@product_router.delete('/{product_id}', response_model=ProductDeleteResponse)
def delete_product(product_id: int, service: ProductServiceDep):
    service.delete_product(product_id)
    return {
        'success': True,
        'detail': f'Product with ID: {product_id} successfully removed.'
    }