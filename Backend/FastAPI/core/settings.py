import os
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

# Backend folder path
BASE_DIR = Path(__file__).parent.parent.parent


class DbSettings(BaseModel):
    url: str = os.getenv("DB_URL") or ""
    sqlite_url: str = os.getenv("DB_SQLITE_URL") or ""
    docker_url: str = os.environ.get("DB_DOCKER_URL") or ""
    # Only debug mode could be set for True!
    echo: bool = False


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30


class Stripe(BaseModel):
    publishable_key: str | None = os.getenv("STRIPE_CHECKOUT_PUBLISHABLE_KEY")
    secret_key: str | None = os.getenv("STRIPE_CHECKOUT_SECRET_KEY")
    api_version: str = "2024-04-10"


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()
    auth_jwt: AuthJWT = AuthJWT()
    stripe: Stripe = Stripe()


settings = Settings()
