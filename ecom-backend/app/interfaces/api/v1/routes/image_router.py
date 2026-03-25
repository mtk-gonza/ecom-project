from fastapi import APIRouter, UploadFile, Depends
from app.core.enums.image_type import ImageType
from app.core.use_cases.image_use_cases import CreateImageUseCase
from app.adapters.persistence.repositories.image_repository_impl import ImageRepositoryImpl
from app.adapters.persistence.repositories.product_repository_impl import ProductRepositoryImpl
from app.adapters.persistence.repositories.licence_repository_impl import LicenceRepositoryImpl
from app.adapters.api.dependency import db_dependency, user_dependency

router = APIRouter(prefix='/images', tags=['IMAGES'])

@router.post('/upload')
async def upload_image(image_data: UploadFile, entity_type: str, entity_id: int, image_type: ImageType, db: db_dependency, user: user_dependency):
    use_case = CreateImageUseCase(
        image_repository=ImageRepositoryImpl(db),
        product_repository=ProductRepositoryImpl(db),
        licence_repository=LicenceRepositoryImpl(db)
    )
    return await use_case.execute(
        image_data=image_data,
        entity_type=entity_type,
        entity_id=entity_id,
        image_type=image_type
    )
