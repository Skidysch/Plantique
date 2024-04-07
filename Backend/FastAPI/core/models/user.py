from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .profile import Profile
    from .cart import Cart
    from .order import Order


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
    )
    profile: Mapped["Profile"] = relationship(back_populates="user")
    cart: Mapped["Cart"] = relationship(back_populates="user")
    orders: Mapped[list["Order"]] = relationship(back_populates="user")
