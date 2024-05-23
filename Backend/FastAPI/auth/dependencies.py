from typing import Any

from fastapi import Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.auth import utils as auth_utils
from FastAPI.core.models import User
from FastAPI.core.models import db_helper
from FastAPI.api_v1.users.crud import get_user

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/jwt/login",
)


async def validate_auth_user(
    username: str = Form(),
    password: str = Form(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    if not (
        user := await get_user(
            session,
            search_field="username",
            search_value=username,
        )
    ):
        raise unauthed_exc

    if not auth_utils.validate_password(
        password=password,
        hashed_password=user.hashed_password,
    ):
        raise unauthed_exc

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is not active",
        )

    return user


async def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
):
    try:
        payload = auth_utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return payload


def validate_token_type(
    payload: dict[str, Any],
    token_type: str,
) -> bool:
    current_token_type = payload.get(auth_utils.TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Invalid token type {current_token_type!r},"
        f" expected {token_type!r}",
    )


async def get_user_by_token_sub(
    payload: dict[str, Any],
    session: AsyncSession,
) -> User:
    user_id: str = payload["sub"]
    if user := await get_user(
        session=session,
        search_field="id",
        search_value=user_id,
    ):
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalid",
    )


class UserGetterFromToken:
    def __init__(self, token_type: str) -> None:
        self.token_type = token_type

    async def __call__(
        self,
        payload: dict[str, Any] = Depends(get_current_token_payload),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ):
        validate_token_type(payload, self.token_type)
        return await get_user_by_token_sub(
            payload=payload,
            session=session,
        )


get_current_auth_user = UserGetterFromToken(
    auth_utils.ACCESS_TOKEN_TYPE,
)
get_current_auth_user_for_refresh = UserGetterFromToken(
    auth_utils.REFRESH_TOKEN_TYPE,
)


async def get_current_active_auth_user(
    user: User = Depends(get_current_auth_user),
) -> User:
    if user.is_active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User is not active",
    )
