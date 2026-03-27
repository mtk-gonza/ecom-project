from app.infrastructure.logging.logger import get_logger
from app.domain.ports.category_repository import CategoryRepository
from app.domain.entities.category import Category
from app.domain.exceptions import NotFoundError, ConflictError
from app.interfaces.api.v1.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse

logger = get_logger(__name__)

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    # =========================
    # GET ALL
    # =========================    
    def get_categories(self, skip: int = 0, limit: int = 100) -> list[CategoryResponse]:
        logger.info('Retrieving category list.')
        return self.category_repository.get_all(skip=skip, limit=limit)

    # =========================
    # GET BY ID
    # =========================
    def get_category(self, category_id: int) -> CategoryResponse:
        logger.info(f'Searching for category with ID: {category_id}.')
        category = self.category_repository.get_by_id(category_id)
        if not category:
            logger.warning(f'Category with ID: {category_id} not found.')
            raise NotFoundError(f'Category with ID: {category_id} not found.')
        return category

    # =========================
    # CREATE
    # =========================
    def create_category(self, category_data: CategoryCreate) -> CategoryResponse:
        logger.info(f'Creating category with name: {category_data.name}.')
        existing = self.category_repository.get_by_name(category_data.name)
        if existing:
            logger.error(f'Category with name: {category_data.name} already exists.')
            raise ConflictError('Category already exists.')
        category = Category(
            id=None,
            name=category_data.name,
            description=category_data.description
        )
        return self.category_repository.create(category)

    # =========================
    # UPDATE
    # =========================
    def update_category(self, category_id: int, category_data: CategoryUpdate) -> CategoryResponse:
        logger.info(f'Updating category with ID: {category_id}.')
        existing = self.category_repository.get_by_id(category_id)
        if not existing:
            logger.warning(f'Category with ID: {category_id} not found.')
            raise NotFoundError(f'Category with ID: {category_id} not found.')
        updated_category = Category(
            id=category_id,
            name=category_data.name,
            description=category_data.description
        )
        return self.category_repository.update(category_id, updated_category)
    
    # =========================
    # DELETE
    # =========================
    def delete_category(self, category_id: int) -> bool:
        logger.info(f'Deleting product with ID: {category_id}.')
        existing = self.category_repository.get_by_id(category_id)
        if not existing:
            logger.warning(f'Category with ID: {category_id} not found.')
            raise NotFoundError(f'Category with ID: {category_id} not found.')
        return self.category_repository.delete(category_id)