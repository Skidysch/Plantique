from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

# if TYPE_CHECKING:
#     from .cart import Cart


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
    )
    # cart_id: Mapped[int] = mapped_column(
    #     ForeignKey("carts.id"),
    # )
    # cart: Mapped["Cart"] = relationship("Cart", back_populates="user")
    # orders: list[Order] = relationship("Order", back_populates="user")

    # Move to profile
    # first_name: Mapped[str]
    # last_name: Mapped[str]
    # profile_picture: Mapped[str]
    # birth_date: Mapped[datetime]
    # created_at: Mapped[datetime] = mapped_column(
    #     default=datetime.now,
    #     server_default=func.now(),
    # )
