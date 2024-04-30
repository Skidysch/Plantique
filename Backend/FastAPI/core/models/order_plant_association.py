from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .plant import Plant
    from .order import Order


class OrderPlantAssociation(Base):
    __tablename__ = "order_plant_association"
    __table_args__ = (
        UniqueConstraint(
            "order_id",
            "plant_id",
            name="idx_unique_order_plant",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id", ondelete="CASCADE"),
    )
    plant_id: Mapped[int] = mapped_column(
        ForeignKey("plants.id", ondelete="CASCADE"),
    )
    # Association between PlantCategoryAssociation -> Order
    order: Mapped["Order"] = relationship(
        back_populates="plants_details",
    )
    # Association between PlantCategoryAssociation -> Plant
    plant: Mapped["Plant"] = relationship(
        back_populates="orders_details",
    )
    quantity: Mapped[int] = mapped_column(
        default=1,
        server_default="1",
    )
    unit_price: Mapped[float] = mapped_column(
        default=0,
        server_default="0",
    )
