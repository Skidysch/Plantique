import datetime
from typing import Any
import uuid

import bcrypt
from fastapi.security import OAuth2PasswordBearer
import jwt

from FastAPI.core.models import User
from FastAPI.core.settings import settings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/jwt/login",
)
TOKEN_TYPE_FIELD = "type"
ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"


def encode_jwt(
    payload: dict[str, Any],
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: datetime.timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.datetime.now(datetime.UTC)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + datetime.timedelta(
            minutes=expire_minutes,
        )
    to_encode.update(
        iat=now,
        exp=expire,
        jti=str(uuid.uuid4()),
    )
    encoded = jwt.encode(  # type: ignore
        payload=to_encode,
        key=private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
) -> dict[str, Any]:
    decoded = jwt.decode(  # type: ignore
        jwt=token,
        key=public_key,
        algorithms=[algorithm],
    )
    return decoded


def create_jwt(
    token_type: str,
    token_data: dict[str, Any],
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: datetime.timedelta | None = None,
) -> str:
    jwt_payload: dict[str, Any] = {TOKEN_TYPE_FIELD: token_type}
    jwt_payload.update(token_data)
    return encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
    )


def create_access_token(
    user: User,
):
    jwt_payload = {
        "sub": user.id,
        "username": user.username,
        "email": user.email,
    }
    return create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_minutes=settings.auth_jwt.access_token_expire_minutes,
    )


def create_refresh_token(
    user: User,
):
    jwt_payload: dict[str, Any] = {
        "sub": user.id,
    }
    return create_jwt(
        token_type=REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=datetime.timedelta(
            days=settings.auth_jwt.refresh_token_expire_days,
        ),
    )


def hash_password(
    password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(
        password=pwd_bytes,
        salt=salt,
    )


def validate_password(
    password: str,
    hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )
