from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Plant(Base):
    name: Mapped[str]
    slug: Mapped[str]
    link: Mapped[str]
    description: Mapped[str]
    soil_type: Mapped[str]
    # TODO: consider ways to store image_url in database
    image_url: Mapped[str]
    price: Mapped[float]
    stock_available: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
    )
    stock_quantity: Mapped[int] = mapped_column(
        default=0,
        server_default="0",
    )
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
        onupdate=datetime.now,
    )

    # categories: Mapped[list[Category]] = relationship('Category', secondary=PlantCategoryAssociation, back_populates="plants",)
    # carts: Mapped[list[Cart]] = relationship('Cart', secondary=PlantCartAssociation, back_populates="plants",)
    # orders: Mapped[list[Order]] = relationship('Order', secondary=PlantOrderAssociation, back_populates="plants",)
