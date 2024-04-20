from sqlalchemy import ScalarResult, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


from .schemas import UserCreate, UserUpdate, UserUpdatePartial
from api_v1.carts.crud import create_user_cart
from api_v1.profiles.crud import create_user_profile
from api_v1.profiles.schemas import ProfileCreate
from auth.utils import hash_password
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
    search_field: str,
    search_value: str | int,
) -> User | None:
    match search_field:
        case "username":
            query_field = User.username
        case "email":
            query_field = User.email
        case _:
            query_field = User.id

    query = (
        select(User)
        .options(joinedload(User.profile), joinedload(User.cart))
        .where(query_field == search_value)
    )
    user: User | None = await session.scalar(query)
    return user


async def create_user(
    session: AsyncSession,
    user_in: UserCreate,
) -> User:

    hashed_password = hash_password(user_in.password)
    del user_in.password
    # TODO: Find a way to unite everything in transaction
    user = User(**user_in.model_dump(), hashed_password=hashed_password)
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
    if user_update.password is not None:
        hashed_password = hash_password(user_update.password)
        setattr(user, "hashed_password", hashed_password)
        del user_update.password
    for key, value in user_update.model_dump(
        exclude_unset=partial,
    ).items():
        setattr(user, key, value)

    await session.commit()

    return user


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:
    await session.delete(user)
    await session.commit()
