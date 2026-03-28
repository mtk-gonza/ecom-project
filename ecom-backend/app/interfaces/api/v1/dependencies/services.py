from fastapi import Depends

from app.application.services.category_service import CategoryService
from app.application.services.product_service import ProductService
from app.application.services.license_service import LicenseService
from app.application.services.image_service import ImageService
from app.application.services.role_service import RoleService
from app.application.services.specification_service import SpecificationService
from app.application.services.user_service import UserService
from app.application.services.auth_service import AuthService

from .repositories import (
    get_category_repository,
    get_product_repository,
    get_license_repository,
    get_image_repository,
    get_role_repository,
    get_specification_repository,
    get_user_repository
)

def get_category_service(repo = Depends(get_category_repository)) -> CategoryService:
    return CategoryService(repo)

def get_product_service(repo = Depends(get_product_repository)) -> ProductService:
    return ProductService(repo)

def get_license_service(repo = Depends(get_license_repository)) -> LicenseService:
    return LicenseService(repo)

def get_role_service(repo = Depends(get_role_repository)) -> RoleService:
    return RoleService(repo)

def get_specification_service(repo = Depends(get_specification_repository)) -> SpecificationService:
    return SpecificationService(repo)

def get_user_service(repo = Depends(get_user_repository)) -> UserService:
    return UserService(repo)

def get_auth_service(user_repo = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repo)

def get_image_service(
    image_repo = Depends(get_image_repository),
    product_repo = Depends(get_product_repository),
    license_repo = Depends(get_license_repository)
):
    return ImageService(
        image_repository=image_repo,
        product_repository=product_repo,
        license_repository=license_repo
    )