from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Cart


async def create_user_cart(
    session: AsyncSession,
    user_id: int,
) -> Cart:
    cart = Cart(user_id=user_id)
    session.add(cart)
    await session.commit()
    return cart
