from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import order_by_id


from FastAPI.api_v1.orders import crud
from FastAPI.api_v1.orders.schemas import OrderCreate, OrderSchema
from FastAPI.core.models import db_helper, Order


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get(
    "",
    response_model=list[OrderSchema],
)
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_orders(
        session=session,
    )


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
)
async def create_order(
    order_in: OrderCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_order(
        session=session,
        order_in=order_in,
    )


@router.get(
    "/{order_id}",
    response_model=OrderSchema,
    status_code=status.HTTP_200_OK,
)
async def get_order(
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Order:
    return order


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_order(
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_order(
        session=session,
        order=order,
    )
