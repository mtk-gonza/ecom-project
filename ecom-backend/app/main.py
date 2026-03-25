from fastapi import FastAPI
from app.interfaces.api.v1.routes.product_routes import product_router
from app.infrastructure.db.base import Base
from app.infrastructure.db.session import engine
from app.infrastructure.logging.config import setup_logging
from app.interfaces.api.v1.handlers import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI(title="e-com API")

setup_logging()
register_exception_handlers(app)

app.include_router(product_router)