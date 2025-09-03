from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Analit"
    LOG_LEVEL: str = "DEBUG"
    DB_URL: str = "postgresql+asyncpg://user:pass@localhost/dbname"

    class Config:
        env_file = ".env"

settings = Settings()
