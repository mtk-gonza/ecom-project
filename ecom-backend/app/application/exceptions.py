class ApplicationError(Exception):
    def __init__(self, message: str, code: str = "error"):
        self.message = message
        self.code = code
        super().__init__(message)

class ApplicationError(Exception):
    """Base para todas las excepciones de la aplicación"""
    pass

class NotFoundError(ApplicationError):
    """Recurso no encontrado"""
    pass

class ValidationError(ApplicationError):
    """Error de validación de negocio"""
    pass

class ConflictError(ApplicationError):
    """Conflictos (ej: duplicados)"""
    pass

class ProductNotFoundError(NotFoundError):
    def __init__(self, product_id: int):
        super().__init__(f"Producto con id {product_id} no existe")