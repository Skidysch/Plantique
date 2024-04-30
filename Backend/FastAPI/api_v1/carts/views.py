from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import cart_by_user_id, cart_by_association_id
from .schemas import CartSchema, CartUpdate
from core.models import Cart, db_helper

router = APIRouter(prefix="/carts", tags=["Carts"])


@router.get(
    "/id/{user_id}",
    response_model=CartSchema,
)
async def get_cart_by_user_id(
    cart: Cart = Depends(cart_by_user_id),
):
    return cart


@router.get(
    "/assoc_id/{association_id}",
    response_model=CartSchema,
)
async def get_cart_by_association_id(
    cart: Cart = Depends(cart_by_association_id),
):
    return cart


@router.post(
    "/id/{user_id}/add/{plant_id}",
    response_model=CartSchema,
)
async def add_plant_to_cart(
    params_update: CartUpdate,
    plant_id: int,
    cart: Cart = Depends(cart_by_user_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.add_plant_to_cart(
        session=session,
        cart=cart,
        plant_id=plant_id,
        params_update=params_update,
    )


@router.patch(
    "/update/{association_id}",
    response_model=CartSchema,
)
async def update_plant_quantity(
    association_id: int,
    params_update: CartUpdate,
    cart: Cart = Depends(cart_by_association_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_plant_quantity(
        session=session,
        cart=cart,
        association_id=association_id,
        params_update=params_update,
    )


@router.delete(
    "/delete/{association_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_plant_from_cart(
    association_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_plant_from_cart(
        session=session,
        association_id=association_id,
    )
