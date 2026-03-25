from fastapi import APIRouter, Depends, Query
from typing import List
from src.application.services.category_service import CategoryService
from src.config.dependencies.services import get_category_service
from src.interfaces.api.schemas.category_schema import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate
)

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[CategoryResponse])
def get_categories(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service: CategoryService = Depends(get_category_service)
):
    return service.get_categories(skip=skip, limit=limit)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service)
):
    return service.get_category(category_id)

@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    service: CategoryService = Depends(get_category_service)
):
    return service.create_category(category)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    service: CategoryService = Depends(get_category_service)
):
    return service.update_category(category_id, category)

@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service)
):
    service.delete_category(category_id)