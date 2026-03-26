from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.db.session import get_db
from app.infrastructure.repositories.category_repository_impl import CategoryRepositoryImpl
from app.infrastructure.repositories.product_repository_impl import ProductRepositoryImpl
from app.infrastructure.repositories.license_repository_impl import LicenseRepositoryImpl
from app.infrastructure.repositories.image_repository_impl import ImageRepositoryImpl
from app.infrastructure.repositories.role_repository_impl import RoleRepositoryImpl
from app.infrastructure.repositories.specification_repository_impl import SpecificationRepositoryImpl
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl


def get_category_repository(db: Session = Depends(get_db)):
    return CategoryRepositoryImpl(db)

def get_product_repository(db: Session = Depends(get_db)):
    return ProductRepositoryImpl(db)

def get_license_repository(db: Session = Depends(get_db)):
    return LicenseRepositoryImpl(db)

def get_image_repository(db: Session = Depends(get_db)):
    return ImageRepositoryImpl(db)

def get_role_repository(db: Session = Depends(get_db)):
    return RoleRepositoryImpl(db)

def get_specification_repository(db: Session = Depends(get_db)):
    return SpecificationRepositoryImpl(db)

def get_user_repository(db: Session = Depends(get_db)):
    return UserRepositoryImpl(db)