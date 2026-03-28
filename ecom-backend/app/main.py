import sys
import uvicorn
from fastapi import FastAPI
from app.interfaces.api.v1.routes.auth_router import auth_router
from app.interfaces.api.v1.routes.category_router import category_router
from app.interfaces.api.v1.routes.license_router import license_router
from app.interfaces.api.v1.routes.product_routes import product_router
from app.interfaces.api.v1.routes.role_router import role_router
from app.infrastructure.db.base import Base
from app.infrastructure.db.session import init_db, engine, SessionLocal
from app.infrastructure.logging.config import setup_logging
from app.interfaces.api.v1.handlers import register_exception_handlers
from app.seeds.seeder_handler import run_seeder
from app.config.settings import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="e-com API")

setup_logging()
register_exception_handlers(app)
run_seeder()

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(license_router)
app.include_router(product_router)
app.include_router(role_router)

if __name__ == '__main__':
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.API_PORT,
        reload=True
    )