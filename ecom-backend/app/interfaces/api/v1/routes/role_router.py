from fastapi import APIRouter, Depends, Query, status
from typing import List, Annotated
from app.application.services.role_service import RoleService
from app.interfaces.api.v1.dependencies.services import get_role_service
from app.interfaces.api.v1.schemas.role_schema import (
    RoleCreate,
    RoleResponse,
    RoleUpdate,
    RoleDeleteResponse
)

role_router = APIRouter(prefix='/roles', tags=['roles'])

RoleServiceDep = Annotated[RoleService, Depends(get_role_service)]

# =========================
# GET ALL
# =========================
@role_router.get('/', response_model=List[RoleResponse])
def get_roles(service: RoleServiceDep, skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100)) -> List[RoleResponse]:
    return service.get_roles(skip=skip, limit=limit)

# =========================
# GET BY ID
# =========================
@role_router.get('/{role_id}', response_model=RoleResponse)
def get_role(role_id: int, service: RoleServiceDep) -> RoleResponse:
    return service.get_role(role_id)

# =========================
# CREATE
# =========================
@role_router.post('/', response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(role_data: RoleCreate, service: RoleServiceDep) -> RoleResponse:
    return service.create_role(role_data)

# =========================
# UPDATE
# =========================
@role_router.put('/{role_id}', response_model=RoleResponse)
def update_role(role_id: int, role_data: RoleUpdate, service: RoleServiceDep) -> RoleResponse:
    return service.update_role(role_id, role_data)

# =========================
# DELETE
# =========================
@role_router.delete('/{role_id}', response_model=RoleDeleteResponse)
def delete_role(role_id: int, service: RoleServiceDep):
    service.delete_role(role_id)
    return {
        'success': True,
        'detail': f'Role with ID: {role_id} successfully removed.'
    }