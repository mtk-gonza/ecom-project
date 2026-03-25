from app.domain.entities.product import Product
from app.domain.ports.product_repository import ProductRepository
from app.application.dtos.product_dto import CreateProductDTO
from app.application.exceptions import ValidationError


class CreateProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, dto: CreateProductDTO) -> Product:
        # 🔹 1. Validaciones básicas (si hace falta extra)
        if dto.price < 0:
            raise ValidationError("El precio no puede ser negativo")

        # 🔹 2. Crear entidad de dominio
        product = Product(
            id=None,
            sku=dto.sku,
            slug=dto.slug,
            name=dto.name,
            description=dto.description,
            price=dto.price,
            currency=dto.currency,
            cost_price=dto.cost_price,
            discount=dto.discount,
            stock=dto.stock,
            barcode=dto.barcode,
            installments=dto.installments,
            special=dto.special,
            is_featured=dto.is_featured,
            status=dto.status,
            licence_id=dto.licence_id,
            category_id=dto.category_id,
            specifications=dto.specifications,
            images=dto.images,
        )

        # 🔹 3. Persistir
        created_product = self.repository.create(product)  # o save()

        return created_product