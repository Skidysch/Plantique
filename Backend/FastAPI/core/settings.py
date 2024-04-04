from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    api_v1_prefix: str =  "/api/v1"
    db_url: str = (
        "postgresql+asyncpg://postgres:43231323:Postgres:2311345@localhost:5432/PlantiqueDB"
    )
    # Only debug mode could be set for True!
    db_echo: bool = False


settings = Setting()
