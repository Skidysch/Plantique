from sqlalchemy import ScalarResult, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


from .schemas import UserCreate, UserUpdate, UserUpdatePartial
from api_v1.carts.crud import create_user_cart
from api_v1.profiles.crud import create_user_profile
from api_v1.profiles.schemas import ProfileCreate
from core.models import User


async def get_users(
    session: AsyncSession,
) -> list[User]:
    query = (
        select(User)
        .options(joinedload(User.profile), joinedload(User.cart))
        .order_by(User.id)
    )
    users: ScalarResult[User] = await session.scalars(query)
    return list(users)


async def get_user(
    session: AsyncSession,
    user_id: int,
) -> User | None:

    query = (
        select(User)
        .options(joinedload(User.profile), joinedload(User.cart))
        .where(User.id == user_id)
    )
    user: User | None = await session.scalar(query)
    return user


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

    # TODO: Find a way to unite everything in transaction
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)

    profile = await create_user_profile(
        session=session,
        user_id=user.id,
        profile_in=ProfileCreate.model_validate({}),
    )
    user.profile = profile

    cart = await create_user_cart(
        session=session,
        user_id=user.id,
    )
    user.cart = cart

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
