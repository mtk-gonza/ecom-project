from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.infrastructure.db.session import get_db

from app.interfaces.api.v1.schemas.product_schema import (
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductResponseSchema,
    ProductDeleteResponseSchema,
)

from app.application.dtos.product_dto import (
    CreateProductDTO,
    UpdateProductDTO,
)

from app.application.use_cases.product.create_product import CreateProductUseCase
from app.application.use_cases.product.update_product import UpdateProductUseCase
from app.application.use_cases.product.delete_product import DeleteProductUseCase

from app.infrastructure.repositories.product_repository_impl import ProductRepositoryImpl


product_router = APIRouter(prefix="/products", tags=["Products"])


# =========================
# 🔹 DEPENDENCY
# =========================
def get_product_repository(db: Session = Depends(get_db)):
    return ProductRepositoryImpl(db)

# =========================
# 🚀 GET
# =========================
@product_router.get("/", response_model=List[ProductResponseSchema])
def get_products(repo=Depends(get_product_repository)):
    return repo.get_all()

@product_router.get("/{product_id}", response_model=ProductResponseSchema)
def get_product(product_id: int, repo=Depends(get_product_repository)):
    product = repo.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# =========================
# 📥 CREATE
# =========================
@product_router.post("/", response_model=ProductResponseSchema)
def create_product(
    body: ProductCreateSchema,
    repo=Depends(get_product_repository),
):
    use_case = CreateProductUseCase(repo)

    dto = CreateProductDTO(**body.model_dump())

    product = use_case.execute(dto)

    return product


# =========================
# 🔄 UPDATE
# =========================
@product_router.put("/{product_id}", response_model=ProductResponseSchema)
def update_product(
    product_id: int,
    body: ProductUpdateSchema,
    repo=Depends(get_product_repository),
):
    use_case = UpdateProductUseCase(repo)

    dto = UpdateProductDTO(
        id=product_id,
        **body.model_dump(exclude_unset=True)
    )

    try:
        product = use_case.execute(dto)
        return product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# =========================
# 🗑️ DELETE
# =========================
@product_router.delete("/{product_id}", response_model=ProductDeleteResponseSchema)
def delete_product(
    product_id: int,
    repo=Depends(get_product_repository),
):
    use_case = DeleteProductUseCase(repo)

    try:
        use_case.execute(product_id)
        return {
            "success": True,
            "detail": "Producto eliminado correctamente"
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))