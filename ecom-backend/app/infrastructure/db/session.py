from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings
from app.infrastructure.db.base import Base

engine = create_engine(settings.DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# 🔥 FALTA ESTO
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🛠 Función para crear las tablas
def init_db():
    # Importar los modelos aquí para que se registren en Base.metadata antes de crear tablas
    from app.infrastructure.db.models import (
        role_model,
        image_model,
        license_model,
        category_model,
        user_model,
        product_model,
        specification_model,
        user_roles_model
    )
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente.")