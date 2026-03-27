from fastapi import APIRouter, Depends, Query, status
from typing import List, Annotated
from app.application.services.license_service import LicenseService
from app.interfaces.api.v1.dependencies.services import get_product_service
from app.interfaces.api.v1.schemas.license_schema import (
    LicenseCreate,
    LicenseUpdate,
    LicenseResponse,
    LicenseDeleteResponse
)

license_router = APIRouter(prefix='/licenses', tags=['licenses'])

LicenseServiceDep = Annotated[LicenseService, Depends(get_product_service)]

# =========================
# GET ALL
# =========================
@license_router.get('/', response_model=List[LicenseResponse])
def get_licenses(service: LicenseServiceDep, skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100)) -> List[LicenseResponse]:
    return service.get_licenses(skip=skip, limit=limit)

# =========================
# GET BY ID
# =========================
@license_router.get('/{license_id}', response_model=LicenseResponse)
def get_license(license_id: int, service: LicenseServiceDep) -> LicenseResponse:
    return service.get_license(license_id)

# =========================
# CREATE
# =========================
@license_router.post('/', response_model=LicenseResponse, status_code=status.HTTP_201_CREATED)
def create_product(license_data: LicenseCreate, service: LicenseServiceDep) -> LicenseResponse:
    return service.create_license(license_data)

# =========================
# UPDATE
# =========================
@license_router.put('/{license_id}', response_model=LicenseResponse)
def update_license(license_id: int, license_data: LicenseUpdate, service: LicenseServiceDep) -> LicenseResponse:
    return service.update_license(license_id, license_data)

# =========================
# DELETE
# =========================
@license_router.delete('/{product_id}', response_model=LicenseDeleteResponse, status_code=status.HTTP_204_NO_CONTENT)
def deletelicense(license_id: int, service: LicenseServiceDep):
    service.delete_license(license_id)
    return {
        'success': True,
        'detail': f'License with ID: {license_id} successfully removed.'
    }