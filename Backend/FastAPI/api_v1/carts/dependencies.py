from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.carts.crud import get_user_cart
from FastAPI.core.models import Cart, db_helper


async def cart_by_user_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Cart:
    cart = await get_user_cart(
        session=session,
        search_field="user_id",
        search_value=user_id,
    )
    if cart is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart not found!",
        )
    return cart


async def cart_by_association_id(
    association_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Cart:
    cart = await get_user_cart(
        session=session,
        search_field="association_id",
        search_value=association_id,
    )
    if cart is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart not found!",
        )
    return cart
