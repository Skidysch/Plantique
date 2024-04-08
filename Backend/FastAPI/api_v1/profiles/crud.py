from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProfileCreate
from core.models import Profile


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
