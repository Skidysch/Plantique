from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.users import crud
from FastAPI.core.models import db_helper, User


async def user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    user = await crud.get_user(
        session=session,
        search_field="id",
        search_value=user_id,
    )
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found!",
    )


async def user_by_username(
    username: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    user = await crud.get_user(
        session=session,
        search_field="username",
        search_value=username,
    )
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found!",
    )


async def user_by_email(
    email: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    user = await crud.get_user(
        session=session,
        search_field="email",
        search_value=email,
    )
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found!",
    )
