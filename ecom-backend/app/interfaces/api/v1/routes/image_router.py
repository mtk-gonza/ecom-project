from fastapi import APIRouter, UploadFile, File, Depends
from typing import List, Annotated
from app.domain.enums import EntityType, ImageType
from app.interfaces.api.v1.dependencies.services import get_image_service
from app.application.services.image_service import ImageService

router = APIRouter(prefix='/images', tags=['Images'])

CategoryServiceDep = Annotated[ImageService, Depends(get_image_service)]


@router.post("/upload")
async def upload_image(
    service: CategoryServiceDep,
    file: UploadFile = File(...),
    entity_type: EntityType = None,
    entity_id: int = None,
    image_type: ImageType = ImageType.FRONT,
):
    content = await file.read()

    image = await service.create_image(
        filename=file.filename,
        image_data=content,
        entity_type=entity_type,
        entity_id=entity_id,
        image_type=image_type
    )

    return image