from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.interfaces.api.v1.dependencies.services import get_auth_service
from app.interfaces.api.v1.dependencies.auth import get_current_user

from app.application.services.auth_service import AuthService
from app.interfaces.api.v1.schemas.auth_schema import Token, TokenData
from app.domain.exceptions import ValidationError

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"description": "Unauthorized"}}
)


@auth_router.post(
    "/token",
    summary="Get Access Token",
    response_model=Token,
    status_code=status.HTTP_200_OK
)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    try:
        token = auth_service.login(form_data.username, form_data.password)
        return {"access_token": token, "token_type": "bearer"}

    except ValidationError as e:
        raise HTTPException(status_code=401, detail=e.message)

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@auth_router.get(
    "/me",
    summary="Get current logged-in user",
    response_model=TokenData,
    status_code=status.HTTP_200_OK
)
def get_current_user_info(
    user = Depends(get_current_user)
):
    return user