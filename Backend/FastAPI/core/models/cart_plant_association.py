from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from FastAPI.core.models.base import Base

if TYPE_CHECKING:
    from FastAPI.core.models.plant import Plant
    from FastAPI.core.models.cart import Cart


class CartPlantAssociation(Base):
    __tablename__ = "cart_plant_association"
    __table_args__ = (
        UniqueConstraint(
            "cart_id",
            "plant_id",
            name="idx_unique_cart_plant",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    cart_id: Mapped[int] = mapped_column(
        ForeignKey("carts.id", ondelete="CASCADE"),
    )
    plant_id: Mapped[int] = mapped_column(
        ForeignKey("plants.id", ondelete="CASCADE"),
    )
    # Association between PlantCartAssociation -> Cart
    cart: Mapped["Cart"] = relationship(
        back_populates="plants_details",
    )
    # Association between PlantCartAssociation -> Plant
    plant: Mapped["Plant"] = relationship(
        back_populates="carts_details",
    )
    quantity: Mapped[int] = mapped_column(
        default=1,
        server_default="1",
    )
