from fastapi import APIRouter, Depends, Query, status
from typing import List, Annotated
from app.application.services.category_service import CategoryService
from app.interfaces.api.v1.dependencies.services import get_category_service
from app.interfaces.api.v1.schemas.category_schema import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
    CategoryDeleteResponse
)

category_router = APIRouter(prefix='/categories', tags=['categories'])

CategoryServiceDep = Annotated[CategoryService, Depends(get_category_service)]

# =========================
# GET ALL
# =========================
@category_router.get('/', response_model=List[CategoryResponse])
def get_categories(service: CategoryServiceDep, skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100)) -> List[CategoryService]:
    return service.get_categories(skip=skip, limit=limit)

# =========================
# GET BY ID
# =========================
@category_router.get('/{category_id}', response_model=CategoryResponse)
def get_category(category_id: int, service: CategoryServiceDep) -> CategoryResponse:
    return service.get_category(category_id)

# =========================
# CREATE
# =========================
@category_router.post('/', response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, service: CategoryServiceDep) -> CategoryResponse:
    return service.create_category(category)

# =========================
# UPDATE
# =========================
@category_router.put('/{category_id}', response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryUpdate, service: CategoryServiceDep) -> CategoryResponse:
    return service.update_category(category_id, category)

# =========================
# DELETE
# =========================
@category_router.delete('/{category_id}', response_model=CategoryDeleteResponse)
def delete_category(category_id: int, service: CategoryServiceDep):
    service.delete_category(category_id)
    return {
        'success': True,
        'detail': f'Category with ID: {category_id} successfully removed.'
    }