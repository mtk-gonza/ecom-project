from abc import ABC, abstractmethod
from app.domain.entities.image import Image

class ImageRepository(ABC):
    
    @abstractmethod
    def save(self, image: Image) -> Image: ...

    @abstractmethod
    def create(self, image: Image) -> Image: ...
