from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent


class DbSettings(BaseModel):
    url: str = (
        "postgresql+asyncpg://"
        "postgres:43231323:Postgres:2311345@localhost:5432/PlantiqueDB"
    )
    # Only debug mode could be set for True!
    echo: bool = False


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()


settings = Settings()
