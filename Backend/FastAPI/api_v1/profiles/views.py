from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.profiles.dependencies import profile_by_user_id
from FastAPI.api_v1.profiles.schemas import (
    ProfileCreate,
    ProfileSchema,
    ProfileUpdatePartial,
)
from FastAPI.api_v1.profiles import crud
from FastAPI.core.models import db_helper, Profile


router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.get(
    "",
    response_model=ProfileSchema,
    status_code=status.HTTP_200_OK,
)
async def read_profile(
    profile: Profile = Depends(profile_by_user_id),
):
    return profile


@router.post(
    "",
    response_model=ProfileSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_profile(
    user_id: int,
    profile_in: ProfileCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user_profile(
        session=session,
        user_id=user_id,
        profile_in=profile_in,
    )


@router.patch("/{user_id}", response_model=ProfileSchema)
async def update_profile_partial(
    profile_update: ProfileUpdatePartial,
    profile: Profile = Depends(profile_by_user_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_user_profile(
        session=session,
        profile=profile,
        profile_update=profile_update,
        partial=True,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_profile(
    profile: Profile = Depends(profile_by_user_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_user_profile(
        session=session,
        profile=profile,
    )
