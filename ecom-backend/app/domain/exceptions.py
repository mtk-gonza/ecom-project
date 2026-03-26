class ApplicationError(Exception):
    """Base para todas las excepciones de la aplicación"""

    def __init__(self, message: str, code: str = "error"):
        self.message = message
        self.code = code
        super().__init__(message)


class NotFoundError(ApplicationError):
    """Recurso no encontrado"""
    # raise NotFoundError(f"Producto con id {product_id} no existe")
    def __init__(self, message: str = "Recurso no encontrado"):
        super().__init__(message, code="not_found")


class ValidationError(ApplicationError):
    """Error de validación de negocio"""
    # raise ValidationError("El precio debe ser mayor a 0")
    def __init__(self, message: str = "Error de validación"):
        super().__init__(message, code="validation_error")


class ConflictError(ApplicationError):
    """Conflictos (ej: duplicados)"""

    def __init__(self, message: str = "Conflicto de datos"):
        super().__init__(message, code="conflict")