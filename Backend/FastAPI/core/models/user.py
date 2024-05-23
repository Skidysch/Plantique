from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from FastAPI.core.models.base import Base

if TYPE_CHECKING:
    from FastAPI.core.models.profile import Profile
    from FastAPI.core.models.cart import Cart
    from FastAPI.core.models.order import Order


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[bytes]
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
    )
    profile: Mapped["Profile"] = relationship(
        cascade="all,delete",
        back_populates="user",
    )
    cart: Mapped["Cart"] = relationship(
        cascade="all,delete",
        back_populates="user",
    )
    orders: Mapped[list["Order"]] = relationship(
        cascade="all,delete",
        back_populates="user",
    )
