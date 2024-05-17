from decimal import Decimal
import os
from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
import stripe

from api_v1.orders.dependencies import order_by_id
from core.models import db_helper, Order


router = APIRouter(
    prefix="/payment",
    tags=["PAYMENT"],
)
stripe.api_key = os.getenv("STRIPE_CHECKOUT_SECRET_KEY")


@router.post(
    "/process/{order_id}",
)
async def payment_process(
    order_id: int,
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
):
    try:
        order: Order = await order_by_id(order_id, session)

        session_data: dict[str, Any] = {
            "client_reference_id": order.id,
            "mode": "payment",
            "success_url": "http://localhost:5173/payment/success",
            "cancel_url": "http://localhost:5173/payment/cancel",
            "line_items": [],
        }

        for item in order.plants_details:
            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": int(
                            Decimal(str(item.plant.price)) * Decimal("100")
                        ),
                        "currency": "usd",
                        "product_data": {
                            "name": item.plant.name,
                        },
                    },
                    "quantity": item.quantity,
                }
            )
        checkout_session = stripe.checkout.Session.create(
            **session_data,
        )

        return JSONResponse({"stripe_session_id": checkout_session.id})
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/success",
)
async def payment_success():
    return {"detail": "Payment successfully fulfilled"}


@router.get(
    "/cancel",
)
async def payment_cancel():
    return {"detail": "Payment has been declined"}
