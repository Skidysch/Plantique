from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .category import Category


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
        back_populates="plants",
    )
    # # Association between Plant -> PlantCategoryAssociation -> Category
    # # Unneccessary here, because our association does not have other fields.
    # # We will use similar approach with our Cart Plant association.
    # categories_details: Mapped[list["PlantCategoryAssociation"]] = relationship(
    #     back_populates="plant",
    # )
    # carts: Mapped[list[Cart]] = relationship('Cart', secondary=CartPlantAssociation, back_populates="plants",)
    # orders: Mapped[list[Order]] = relationship('Order', secondary=OrderPlantAssociation, back_populates="plants",)
