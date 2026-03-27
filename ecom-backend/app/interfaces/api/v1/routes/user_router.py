from fastapi import APIRouter, Depends, Query, status
from typing import List, Annotated
from app.application.services.user_service import UserService
from app.interfaces.api.v1.dependencies.services import get_user_service
from app.interfaces.api.v1.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse,
    UserDeleteResponse
)

user_router = APIRouter(prefix='/users', tags=['users'])

UserServiceDep = Annotated[UserService, Depends(get_user_service)]

# =========================
# GET ALL
# =========================
@user_router.get('/', response_model=List[UserResponse])
def get_users(service: UserServiceDep, skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=100)) -> List[UserResponse]:
    return service.get_users(skip=skip, limit=limit)

# =========================
# GET BY ID
# =========================
@user_router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, service: UserServiceDep) -> UserResponse:
    return service.get_user(user_id)

# =========================
# CREATE
# =========================
@user_router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, service: UserServiceDep) -> UserResponse:
    return service.create_user(user_data)

# =========================
# UPDATE
# =========================
@user_router.put('/{user_id}', response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, service: UserServiceDep) -> UserResponse:
    return service.update_user(user_id, user_data)

# =========================
# DELETE
# =========================
@user_router.delete('/{user_id}', response_model=UserDeleteResponse, status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, service: UserServiceDep):
    service.delete_user(user_id)
    return {
        'success': True,
        'detail': f'user with ID: {user_id} successfully removed.'
    }