from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .category import Category
    from .cart_plant_association import CartPlantAssociation
    from .order_plant_association import OrderPlantAssociation


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
    categories: Mapped[list["Category"]] = relationship(
        secondary="plant_category_association",
        cascade="all,delete",
        back_populates="plants",
    )
    carts_details: Mapped[list["CartPlantAssociation"]] = relationship(
        cascade="all,delete",
        back_populates="plant",
    )
    orders_details: Mapped[list["OrderPlantAssociation"]] = relationship(
        cascade="all,delete",
        back_populates="plant",
    )
