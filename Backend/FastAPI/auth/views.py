from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from . import utils as auth_utils
from .dependencies import (
    get_current_active_auth_user,
    get_current_auth_user_for_refresh,
    validate_auth_user,
)
from .schemas import TokenInfo
from core.models import User
from api_v1.users.schemas import UserSchema

http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix="/jwt",
    tags=["JWT"],
    dependencies=[
        Depends(http_bearer),
    ],
)


@router.post("/login", response_model=TokenInfo)
async def auth_user_issue_jwt(
    user: User = Depends(validate_auth_user),
):
    access_token = auth_utils.create_access_token(user)
    refresh_token = auth_utils.create_refresh_token(user)
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post(
    "/refresh",
    response_model=TokenInfo,
    response_model_exclude_none=True,
)
async def refresh_jwt(
    user: User = Depends(
        get_current_auth_user_for_refresh,
    )
):
    access_token = auth_utils.create_access_token(user)
    return TokenInfo(
        access_token=access_token,
    )


@router.get("/users/current", response_model=UserSchema)
async def get_current_user(
    user: User = Depends(get_current_active_auth_user),
):
    return user
