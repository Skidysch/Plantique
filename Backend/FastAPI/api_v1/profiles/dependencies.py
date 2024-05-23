from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.profiles import crud
from FastAPI.core.models import db_helper, Profile


async def profile_by_user_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Profile:
    profile = await crud.get_user_profile(
        session=session,
        user_id=user_id,
    )
    if profile is not None:
        return profile
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Profile not found!",
    )
