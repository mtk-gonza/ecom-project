from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any

from app.core.config.database import get_db
from app.adapters.persistence.repositories.licence_repository_impl import LicenceRepositoryImpl
from app.core.use_cases.licence_use_cases import (
    CreateLicenceUseCase,
    GetLicenceUseCase,
    ListLicencesUseCase,
    UpdateLicenceUseCase,
    DeleteLicenceUseCase
)
from app.schemas.licence_schema import LicenceCreate, LicenceUpdate, LicenceResponse
from app.core.entities.licence_entity import Licence as LicenceEntity
from app.core.exceptions.licence_exceptions import (
    LicenceNotFoundError,
    LicenceCreationError,
    LicenceUpdateError,
    LicenceDeleteError
)

router = APIRouter(prefix='/licences', tags=['LICENCES'], responses={404: {'description': 'Not found'}})

async def get_licence_repository(db=Depends(get_db)) -> LicenceRepositoryImpl:
    return LicenceRepositoryImpl(db)

def get_licence_use_cases(repository=Depends(get_licence_repository)) -> Dict[str, Any]:
    return {
        'create': CreateLicenceUseCase(repository),
        'get': GetLicenceUseCase(repository),
        'list': ListLicencesUseCase(repository),
        'update': UpdateLicenceUseCase(repository),
        'delete': DeleteLicenceUseCase(repository)
    }

@router.post('/', response_model=LicenceResponse, status_code=status.HTTP_201_CREATED, summary='CREATE new Licence')
async def create_licence(licence_in: LicenceCreate, use_cases=Depends(get_licence_use_cases)):
    licence_entity = LicenceEntity(
        id=None,
        name=licence_in.name,
        description=licence_in.description
    )
    try:
        licence = await use_cases['create'].execute(licence_entity)
        return licence
    except LicenceCreationError:
        raise HTTPException(status_code=400, detail='Failed to create licence')

@router.get('/', response_model=List[LicenceResponse], summary='LIST ALL Licences')
async def list_licences(use_cases=Depends(get_licence_use_cases)):
    categories = await use_cases['list'].execute()
    return categories

@router.get('/{licence_id}', response_model=LicenceResponse, summary='GET Licence by ID')
async def get_licence(licence_id: int, use_cases=Depends(get_licence_use_cases)):
    try:
        licence = await use_cases['get'].execute(licence_id)
        return licence
    except LicenceNotFoundError:
        raise HTTPException(status_code=404, detail='Licence not found')

@router.put('/{licence_id}', response_model=LicenceResponse, summary='UPDATE Licence by ID')
async def update_licence(licence_id: int, licence_in: LicenceUpdate, use_cases=Depends(get_licence_use_cases)):
    try:
        existing = await use_cases['get'].execute(licence_id)
    except LicenceNotFoundError:    
        raise HTTPException(status_code=404, detail='Licence not found')
    updated_entity = LicenceEntity(
        id=licence_id,
        name=licence_in.name if licence_in.name is not None else existing.name,
        description=licence_in.description if licence_in.name is not None else existing.description,
    )
    try:
        updated_licence = await use_cases['update'].execute(updated_entity)
        return updated_licence
    except LicenceUpdateError:
        raise HTTPException(status_code=500, detail='Failed to update licence')

@router.delete('/{licence_id}', status_code=status.HTTP_204_NO_CONTENT, summary='Delete a licence')
async def delete_licence(licence_id: int, use_cases=Depends(get_licence_use_cases)):
    try:
        await use_cases['get'].execute(licence_id)
    except LicenceNotFoundError:
        raise HTTPException(status_code=404, detail='Licence not found')
    except LicenceDeleteError:
        raise HTTPException(status_code=500, detail='Failed to delete licence')