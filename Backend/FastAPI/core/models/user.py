from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
    )
    # cart: Cart = relationship("Cart", back_populates="user")
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
