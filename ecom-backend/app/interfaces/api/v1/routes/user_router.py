from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any
import logging as logger

from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.adapters.persistence.repositories.user_repository_impl import UserRepositoryImpl
from app.core.use_cases.user_use_cases import (
    CreateUserUseCase,
    GetUserUseCase,
    ListUsersUseCase,
    UpdateUserUseCase,
    DeleteUserUseCase
)
from app.core.entities.user_entity import User as UserEntity
from app.adapters.api.dependency import db_dependency, user_dependency

router = APIRouter(prefix='/users', tags=['USERS'], responses={404: {'description': 'Not found'}})

def get_user_use_cases(db: db_dependency) -> Dict[str, Any]:
    repository = UserRepositoryImpl(db)
    return {
        'create': CreateUserUseCase(repository),
        'get': GetUserUseCase(repository),
        'list': ListUsersUseCase(repository),
        'update': UpdateUserUseCase(repository),
        'delete': DeleteUserUseCase(repository)
    }

@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED, summary='Create a new user')
async def create_user(user_in: UserCreate, user: user_dependency, use_cases: Dict[str, Any] = Depends(get_user_use_cases)):
    user_entity = UserEntity(
        id=None,
        username=user_in.username,
        email=user_in.email,
        password=user_in.password,
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        telefono=user_in.telefono,
        is_active=user_in.is_active
    )
    created_user = await use_cases['create'].execute(user_entity)
    return created_user

@router.get('/', response_model=List[UserResponse], summary='LIST ALL Users')
async def list_users(user: user_dependency, use_cases: Dict[str, Any] = Depends(get_user_use_cases)):
    users = await use_cases['list'].execute()
    return users

@router.get('/{user_id}', response_model=UserResponse, summary='Get a single product by ID')
async def get_user(user_id: int, user: user_dependency, use_cases: Dict[str, Any] = Depends(get_user_use_cases)):
    product = await use_cases['get'].execute(user_id)
    if not product:
        raise HTTPException(status_code=404, detail='User not found')
    return product

@router.put('/{user_id}', response_model=UserResponse, summary='Update a user')
async def update_user(user_id: int, user_in: UserUpdate, user: user_dependency, use_cases: Dict[str, Any] = Depends(get_user_use_cases)):
    existing = await use_cases['get'].execute(user_id)
    if not existing:
        raise HTTPException(status_code=404, detail='User not found')
    
    updated_entity = UserEntity(
        id=user_id,
        username=user_in.username if user_in.username is not None else existing.username,
        email=user_in.email if user_in.email is not None else existing.email,
        password=user_in.password if user_in.password is not None else existing.password,
        first_name=user_in.first_name if user_in.first_name is not None else existing.first_name,
        last_name=user_in.last_name if user_in.last_name is not None else existing.last_name,
        telefono=user_in.telefono if user_in.telefono is not None else existing.telefono,
        is_active=user_in.is_active if user_in.is_active is not None else existing.is_active
    )

    updated_user = await use_cases['update'].execute(updated_entity)
    return updated_user

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, summary='Delete a user')
async def delete_user(user_id: int, user: user_dependency, use_cases: Dict[str, Any] = Depends(get_user_use_cases)):
    existing = await use_cases['get'].execute(user_id)
    if not existing:
        raise HTTPException(status_code=404, detail='User not found')

    try:
        await use_cases['delete'].execute(user_id)
        logger.info(f'User deleted: {user_id}')
    except Exception as e:
        logger.error(f'Error deleting user {user_id}: {e}')
        raise HTTPException(status_code=500, detail='Failed to delete user')