from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from FastAPI.api_v1.carts.schemas import CartUpdate
from FastAPI.core.models import Cart, CartPlantAssociation


async def get_user_cart(
    session: AsyncSession,
    search_field: str,
    search_value: str | int,
) -> Cart | None:
    match search_field:
        case "association_id":
            query = (
                select(Cart)
                .join(CartPlantAssociation)
                .where(CartPlantAssociation.id == search_value)
                .options(
                    selectinload(Cart.plants_details).joinedload(
                        CartPlantAssociation.plant
                    ),
                )
            )
        case _:
            query = (
                select(Cart)
                .where(Cart.user_id == search_value)
                .options(
                    selectinload(Cart.plants_details).joinedload(
                        CartPlantAssociation.plant
                    ),
                )
            )

    cart = await session.scalar(query)
    return cart


async def create_user_cart(
    session: AsyncSession,
    user_id: int,
) -> Cart:
    cart = Cart(user_id=user_id)
    session.add(cart)
    await session.commit()
    return cart


async def add_plant_to_cart(
    session: AsyncSession,
    cart: Cart,
    plant_id: int,
    params_update: CartUpdate,
) -> Cart:
    association = CartPlantAssociation(
        cart_id=cart.id,
        plant_id=plant_id,
        quantity=params_update.quantity,
    )

    cart.plants_details.append(association)
    await session.commit()
    await session.refresh(cart, ["plants_details"])
    return cart


async def update_plant_quantity(
    session: AsyncSession,
    cart: Cart,
    association_id: int,
    params_update: CartUpdate,
) -> Cart:
    association = await session.get_one(
        CartPlantAssociation,
        association_id,
    )
    if params_update.replace:
        if params_update.quantity <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantity cannot be zero or negative",
            )
        association.quantity = params_update.quantity
    else:
        if association.quantity + params_update.quantity <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Result cannot be zero or negative",
            )
        association.quantity += params_update.quantity
    await session.commit()
    await session.refresh(cart, ["plants_details"])
    return cart


async def delete_plant_from_cart(
    session: AsyncSession,
    association_id: int,
) -> None:
    association = await session.get_one(
        CartPlantAssociation,
        association_id,
    )

    await session.delete(association)
    await session.commit()
