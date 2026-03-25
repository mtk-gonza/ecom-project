from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any
import logging

from app.core.config.database import get_db
from app.adapters.persistence.repositories.product_spec_repository_impl import ProductSpecRepositoryImpl
from app.core.use_cases.product_spec_use_cases import (
    CreateProductSpecificationUseCase,
    GetProductSpecificationUseCase,
    ListProductSpecificationsUseCase,
    UpdateProductSpecificationUseCase,
    DeleteProductSpecificationUseCase
)
from app.schemas.product_spec_schema import ProductSpecificationCreate, ProductSpecificationResponse, ProductSpecificationUpdate
from app.core.entities.product_specification_entity import ProductSpecification as SpecificationEntity
from app.core.exceptions.product_spec_exceptions import (
    ProductSpecNotFoundError,
    ProductSpecCreationError,
    ProductSpecUpdateError,
    ProductSpecDeleteError
)

router = APIRouter(prefix='/specifications', tags=['SPECIFICATIONS'], responses={404: {'description': 'Not found'}})

async def get_specification_repository(db=Depends(get_db)) -> ProductSpecRepositoryImpl:
    return ProductSpecRepositoryImpl(db)

def get_specification_use_cases(repository=Depends(get_specification_repository)) -> Dict[str, Any]:
    return {
        'create': CreateProductSpecificationUseCase(repository),
        'get': GetProductSpecificationUseCase(repository),
        'list': ListProductSpecificationsUseCase(repository),
        'update': UpdateProductSpecificationUseCase(repository),
        'delete': DeleteProductSpecificationUseCase(repository)
    }

@router.post('/', response_model=ProductSpecificationResponse, status_code=status.HTTP_201_CREATED, summary='Create a new product specification')
async def create_specification(specification_in: ProductSpecificationCreate, use_cases=Depends(get_specification_use_cases)):
    specificatin_entity = SpecificationEntity(
        id=None,
        key=specification_in.key,
        value=specification_in.value
    )
    try:        
        created_product = await use_cases['create'].execute(specificatin_entity)
        return created_product
    except ProductSpecCreationError:
        raise HTTPException(status_code=400, detail='Failed to create product specification')

@router.get('/', response_model=List[ProductSpecificationResponse], summary='LIST ALL Specifications')
async def list_specifications(use_cases=Depends(get_specification_use_cases)):
    return await use_cases['list'].execute()

@router.get('/{specification_id}', response_model=ProductSpecificationResponse, summary='Get a single specification by ID')
async def get_specification(specification_id: int, use_cases=Depends(get_specification_use_cases)):
    try:
        return await use_cases['get'].execute(specification_id)
    except ProductSpecNotFoundError:
        raise HTTPException(status_code=404, detail='Specification not found')

@router.put('/{specification_id}', response_model=ProductSpecificationResponse, summary='Update a specification')
async def update_specification(specification_id: int, specification_in: ProductSpecificationUpdate, use_cases=Depends(get_specification_use_cases)):
    try:
        existing = await use_cases['get'].execute(specification_id)
    except ProductSpecNotFoundError:
        raise HTTPException(status_code=404, detail='Specification not found')    
    updated_entity = SpecificationEntity(
        id=specification_id,
        key=specification_in.key if specification_in.key is not None else existing.key,
        value=specification_in.value if specification_in.value is not None else existing.value
    )
    try:
        updated_product = await use_cases['update'].execute(updated_entity)
        return updated_product
    except ProductSpecUpdateError:
        raise HTTPException(status_code=500, detail='Failed to update specification')

@router.delete('/{specification_id}', status_code=status.HTTP_204_NO_CONTENT, summary='Delete a product')
async def delete_specification(specification_id: int, use_cases=Depends(get_specification_use_cases)):
    try:
        await use_cases['get'].execute(specification_id)
        logging.info(f'Specification deleted: {specification_id}')
    except ProductSpecNotFoundError:
        raise HTTPException(status_code=404, detail='Specification not found')
    except ProductSpecDeleteError:
        logging.error(f'Error deleting specification {specification_id}')
        raise HTTPException(status_code=500, detail='Failed to delete specification')
