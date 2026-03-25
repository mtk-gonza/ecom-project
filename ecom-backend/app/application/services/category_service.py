import logging
from app.domain.ports.category_repository import CategoryRepositoryPort
from app.domain.entities.category import Category
from app.domain.exceptions import NotFoundException, AlreadyExistsException

logger = logging.getLogger(__name__)

class CategoryService:
    def __init__(self, category_repository: CategoryRepositoryPort):
        self.category_repository = category_repository

    def get_category(self, category_id: int) -> Category:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            logger.warning(f'Category with ID: {category_id} not found.')
            raise NotFoundException(f'Category with ID: {category_id} not found.')
        return category
    
    def get_categories(self, skip: int = 0, limit: int = 100) -> list[Category]:
        return self.category_repository.get_all(skip=skip, limit=limit)

    def create_category(self, category_data: Category) -> Category:
        existing = self.category_repository.get_by_name(category_data.name)
        if existing:
            logger.error(f'Category with name: {category_data.name} already exists.')
            raise AlreadyExistsException('Category already exists.')
        category = Category(
            name=category_data.name,
            description=category_data.description
        )
        return self.category_repository.create(category)

    def update_category(self, category_id: int, category_data: Category) -> Category:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            logger.warning(f'Category with ID: {category_id} not found.')
            raise NotFoundException(f'Category with ID: {category_id} not found.')
        updated_category = Category(
            id=category_id,
            name=category_data.name,
            description=category_data.description
        )
        return self.category_repository.update(category_id, updated_category)

    def delete_category(self, category_id: int) -> bool:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            logger.warning(f'Category with ID: {category_id} not found.')
            raise NotFoundException(f'Category with ID: {category_id} not found.')
        return self.category_repository.delete(category_id)