from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from src.config.dependencies import db_dependency, user_dependency
from src.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from src.application.use_cases.auth_use_cases import LoginUseCase
from src.interfaces.api.schemas.auth_schema import Token, TokenData
from src.domain.exceptions import InvalidCredentialsError

router = APIRouter(prefix='/auth', tags=['AUTH'], responses={401: {'description': 'Unauthorized'}})

@router.post('/token', summary='Get Access Token', response_model=Token, status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user_repo = UserRepositoryImpl(db)
    login_use_case = LoginUseCase(user_repo)
    try:
        token = await login_use_case.execute(form_data.username, form_data.password)
        # Si NO es async, quita el 'await': token = login_use_case.execute(...)
    except InvalidCredentialsError:
        raise HTTPException(status_code=401, detail='Incorrect username or password')
    except Exception:
        raise HTTPException(status_code=500, detail='Internal server error')
    return {'access_token': token, 'token_type': 'bearer'}

@router.get('/me', summary='Get current logged-in user', response_model=TokenData, status_code=status.HTTP_200_OK)
async def get_current_user_info(user: user_dependency):
    return user
