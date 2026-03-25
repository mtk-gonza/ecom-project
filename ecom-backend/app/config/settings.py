from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    # =========================
    # 🔹 CONFIG GENERAL
    # =========================
    DEBUG: bool = False
    API_URL: str = "http://localhost:3050"
    API_PORT: int = 3050
    WEB_PORT: int = 3060

    # =========================
    # 🔹 DB
    # =========================
    DB_TYPE: str = "sqlite"

    SQLITE_DB: str = "dev.db"

    DB_USER: str | None = None
    DB_PASSWORD: str | None = None
    DB_HOST: str | None = None
    DB_PORT: int = 3306
    DB_NAME: str | None = None

    # =========================
    # 🔹 CORS
    # =========================
    CORS_ALLOW_ORIGINS: str = "*"

    # =========================
    # ⚙️ PYDANTIC CONFIG
    # =========================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    # =========================
    # 🌐 CORS
    # =========================
    @property
    def cors_origins_list(self) -> List[str]:
        if self.CORS_ALLOW_ORIGINS == "*":
            return ["*"]
        return [o.strip() for o in self.CORS_ALLOW_ORIGINS.split(",")]

    # =========================
    # 🗄️ DATABASE URL
    # =========================
    @property
    def DATABASE_URL(self) -> str:
        if self.DB_TYPE == "sqlite":
            return f"sqlite:///./{self.SQLITE_DB}"

        if not all([self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME]):
            raise ValueError("Faltan variables para MySQL")

        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()