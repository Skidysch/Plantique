from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProfileCreate, ProfileUpdate, ProfileUpdatePartial
from core.models import Profile


async def get_user_profile(
    session: AsyncSession,
    user_id: int,
) -> Profile | None:
    query = (
        select(Profile)
        .where(Profile.user_id == user_id)
    )
    profile: Profile | None = await session.scalar(query)
    return profile


async def create_user_profile(
    session: AsyncSession,
    user_id: int,
    profile_in: ProfileCreate,
) -> Profile:
    profile = Profile(
        **profile_in.model_dump(),
        user_id=user_id,
    )
    session.add(profile)
    await session.commit()
    return profile


async def update_user_profile(
    session: AsyncSession,
    profile_update: ProfileUpdate | ProfileUpdatePartial,
    profile: Profile,
    partial: bool = False,
) -> Profile:
    for key, value in profile_update.model_dump(
        exclude_unset=partial,
    ).items():
        setattr(profile, key, value)

    await session.commit()

    return profile


async def delete_user_profile(
    session: AsyncSession,
    profile: Profile,
) -> None:
    await session.delete(profile)
    await session.commit()
