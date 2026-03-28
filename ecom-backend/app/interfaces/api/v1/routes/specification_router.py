from fastapi import APIRouter, Depends, Query, status
from typing import List, Annotated
from app.application.services.specification_service import SpecificationService
from app.interfaces.api.v1.dependencies.services import get_specification_service
from app.interfaces.api.v1.schemas.specification_schema import (
    SpecificationCreate,
    SpecificationUpdate,
    SpecificationResponse,
    SpecificationDeleteResponse
)

specification_router = APIRouter(prefix='/specifications', tags=['specifications'])

SpecificationServiceDep = Annotated[SpecificationService, Depends(get_specification_service)]

# =========================
# GET ALL
# =========================
@specification_router.get('/', response_model=List[SpecificationResponse])
def get_specifications(service: SpecificationServiceDep, skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100)) -> List[SpecificationResponse]:
    return service.get_specifications(skip=skip, limit=limit)

# =========================
# GET BY ID
# =========================
@specification_router.get('/{specification_id}', response_model=SpecificationResponse)
def get_specification(specification_id: int, service: SpecificationServiceDep) -> SpecificationResponse:
    return service.get_specification(specification_id)

# =========================
# CREATE
# =========================
@specification_router.post('/', response_model=SpecificationResponse, status_code=status.HTTP_201_CREATED)
def create_specification(specification_data: SpecificationCreate, service: SpecificationServiceDep) -> SpecificationResponse:
    return service.create_specification(specification_data)

# =========================
# UPDATE
# =========================
@specification_router.put('/{product_id}', response_model=SpecificationResponse)
def update_specification(specification_id: int, specification_data: SpecificationUpdate, service: SpecificationServiceDep) -> SpecificationResponse:
    return service.update_specification(specification_id, specification_data)

# =========================
# DELETE
# =========================
@specification_router.delete('/{specification_id}', response_model=SpecificationDeleteResponse)
def delete_specification(specification_id: int, service: SpecificationServiceDep):
    service.delete_specification(specification_id)
    return {
        'success': True,
        'detail': f'Specification with ID: {specification_id} successfully removed.'
    }