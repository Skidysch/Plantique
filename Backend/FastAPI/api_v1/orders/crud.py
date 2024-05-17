from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from .schemas import OrderCreate
from core.models import Order, OrderPlantAssociation, User


async def get_orders(
    session: AsyncSession,
) -> list[Order]:
    query = (
        select(Order)
        .options(
            selectinload(
                Order.plants_details,
            ).joinedload(
                OrderPlantAssociation.plant,
            ),
            joinedload(Order.user).joinedload(User.profile),
            joinedload(Order.user).joinedload(User.cart),
        )
        .order_by(Order.id)
    )
    orders = await session.scalars(query)
    return list(orders)


async def create_order(
    order_in: OrderCreate,
    session: AsyncSession,
):
    order = Order(user_id=order_in.cart.user_id)
    session.add(order)
    await session.commit()

    for item in order_in.cart.plants_details:
        association = OrderPlantAssociation(
            order_id=order.id,
            plant_id=item.plant.id,
            quantity=item.quantity,
            unit_price=item.plant.price,
        )
        session.add(association)
        await session.commit()

    return {"order_id": order.id}


async def get_order(
    order_id: int,
    session: AsyncSession,
) -> Order | None:
    query = (
        select(Order)
        .where(Order.id == order_id)
        .options(
            selectinload(Order.plants_details).joinedload(OrderPlantAssociation.plant),
            joinedload(Order.user).joinedload(User.profile),
            joinedload(Order.user).joinedload(User.cart),
        )
    )
    order = await session.scalar(query)
    return order


async def delete_order(
    session: AsyncSession,
    order: Order,
) -> None:
    await session.delete(order)
    await session.commit()
