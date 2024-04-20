from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, User
from .dependencies import user_by_email, user_by_id, user_by_username
from .schemas import UserSchema, UserCreate, UserUpdate, UserUpdatePartial

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "",
    response_model=list[UserSchema],
)
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_users(
        session=session,
    )


@router.post(
    "",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(
        session=session,
        user_in=user_in,
    )


@router.get(
    "/id/{user_id}",
    response_model=UserSchema,
)
async def get_user_by_id(
    user: User = Depends(user_by_id),
):
    return user


@router.get(
    "/username/{username}",
    response_model=UserSchema,
)
async def get_user_by_username(
    user: User = Depends(user_by_username),
):
    return user


@router.get(
    "/email/{email}",
    response_model=UserSchema,
)
async def get_user_by_email(
    user: User = Depends(user_by_email),
):
    return user


@router.put(
    "/{user_id}",
    response_model=UserSchema,
)
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.patch(
    "/{user_id}",
    response_model=UserSchema,
)
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user_update = UserUpdatePartial.model_validate(
        {key: value for key, value in user_update if value is not None},
    )
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_user(session=session, user=user)
