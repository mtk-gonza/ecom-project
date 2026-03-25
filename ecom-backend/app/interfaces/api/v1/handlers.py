from fastapi import Request
from fastapi.responses import JSONResponse

from app.application.exceptions import (
    ApplicationError,
    NotFoundError,
    ValidationError,
    ConflictError
)

from app.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)

# 🔹 Mapeo de excepciones → status HTTP
EXCEPTION_STATUS_MAP = {
    NotFoundError: 404,
    ValidationError: 400,
    ConflictError: 409,
}

def get_status_code(exc: ApplicationError) -> int:
    return EXCEPTION_STATUS_MAP.get(type(exc), 500)

# 🔹 Registro de handlers
def register_exception_handlers(app):

    @app.exception_handler(ApplicationError)
    async def application_error_handler(request: Request, exc: ApplicationError):
        status_code = get_status_code(exc)

        # Log del error
        if status_code >= 500:
            logger.error(f"[{request.method}] {request.url} - {exc.message}")
        else:
            logger.warning(f"[{request.method}] {request.url} - {exc.message}")

        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "error": {
                    "code": exc.code,
                    "message": exc.message
                }
            }
        )