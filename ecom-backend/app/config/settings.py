import os

class Settings:
    DB_TYPE = os.getenv("DB_TYPE", "sqlite")

    if DB_TYPE == "sqlite":
        DATABASE_URL = "sqlite:///./dev.db"
    else:
        DATABASE_URL = "mysql+pymysql://user:password@localhost/db_name"

settings = Settings()