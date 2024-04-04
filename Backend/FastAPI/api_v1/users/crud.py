from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreate, UserUpdate, UserUpdatePartial
from core.models import User


async def get_users(
    session: AsyncSession,
) -> list[User]:
    query = select(User).order_by(User.id)
    result = await session.execute(query)
    users = result.scalars().all()
    return list(users)


async def get_user(
    session: AsyncSession,
    user_id: int,
) -> User | None:
    return await session.get(User, user_id)


# async def get_current_user(
#     db: AsyncSession,
#     token: str = Depends(services.oauth2schema),
# ) -> User:
#     try:
#         payload = jwt.decode(
#             token,
#             services.JWT_SECRET,
#             algorithms=["HS256"],
#         )
#         user = db.query(models.User).get(payload["id"])
#     except:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid Email or Password",
#         )

#     return schemas.User.model_validate(user)


async def create_user(
    session: AsyncSession,
    user_in: UserCreate,
) -> User:

    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdate | UserUpdatePartial,
    partial: bool = False,
) -> User:
    for key, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, key, value)

    await session.commit()

    return user


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:
    await session.delete(user)
    await session.commit()
