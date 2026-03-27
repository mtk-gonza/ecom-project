from fastapi import APIRouter, Depends, Query, status
from typing import List
from app.application.services.role_service import RoleService
from app.interfaces.api.v1.dependencies.services import get_role_service
from app.interfaces.api.v1.schemas.role_schema import (
    RoleCreate,
    RoleResponse,
    RoleUpdate
)

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=List[RoleResponse])
def get_roless(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service: RoleService = Depends(get_role_service)
):
    return service.get_roles(skip=skip, limit=limit)


@router.get("/{role_id}", response_model=RoleResponse)
def get_role(
    role_id: int,
    service: RoleService = Depends(get_role_service)
):
    return service.get_role(role_id)


@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(
    role: RoleCreate,
    service: RoleService = Depends(get_role_service)
):
    return service.create_role(role)


@router.put("/{role_id}", response_model=RoleResponse)
def update_role(
    role_id: int,
    role: RoleUpdate,
    service: RoleService = Depends(get_role_service)
):
    return service.update_role(role_id, role)


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
    role_id: int,
    service: RoleService = Depends(get_role_service)
):
    service.delete_role(role_id)
    return None