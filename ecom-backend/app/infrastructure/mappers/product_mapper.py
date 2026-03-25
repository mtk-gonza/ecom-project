from app.domain.entities.product import Product
from app.infrastructure.db.models.product_model import ProductModel


def to_domain(model: ProductModel) -> Product:
    return Product(
        id=model.id,
        sku=model.sku,
        slug=model.slug,
        name=model.name,
        description=model.description,
        price=model.price,
        currency=model.currency,
        cost_price=model.cost_price,
        discount=model.discount,
        stock=model.stock,
        barcode=model.barcode,
        installments=model.installments,
        special=model.special,
        is_featured=model.is_featured,
        status=model.status,
        licence_id=model.licence_id,
        category_id=model.category_id,
        specifications=[
            {"key": spec.key, "value": spec.value}
            for spec in model.specifications
        ],
        images=[img.url for img in model.images],
        created_at=model.created_at,
        updated_at=model.updated_at,
    )

def to_model(entity: Product) -> ProductModel:
    return ProductModel(
        id=entity.id,
        sku=entity.sku,
        slug=entity.slug,
        name=entity.name,
        description=entity.description,
        price=entity.price,
        currency=entity.currency,
        cost_price=entity.cost_price,
        discount=entity.discount,
        stock=entity.stock,
        barcode=entity.barcode,
        installments=entity.installments,
        special=entity.special,
        is_featured=entity.is_featured,
        status=entity.status,
        licence_id=entity.licence_id,
        category_id=entity.category_id,
    )