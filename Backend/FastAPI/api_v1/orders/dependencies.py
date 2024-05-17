from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Order


async def order_by_id(
    order_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Order:
    order = await crud.get_order(
        session=session,
        order_id=order_id,
    )
    if order is not None:
        return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Order not found!",
    )
