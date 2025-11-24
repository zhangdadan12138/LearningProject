# from pydantic import BaseSettings
from pydantic_settings import BaseSettings
# from pydantic import BaseSettings, PostgresDsn, field_validator

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Robust Project"
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
