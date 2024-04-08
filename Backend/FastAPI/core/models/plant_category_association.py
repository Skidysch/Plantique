from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .plant import Plant
    from .category import Category


class PlantCategoryAssociation(Base):
    __tablename__ = "plant_category_association"
    __table_args__ = (
        UniqueConstraint(
            "plant_id",
            "category_id",
            name="idx_unique_plant_category",
        ),
    )

    plant_id: Mapped[int] = mapped_column(
        ForeignKey("plants.id", ondelete="CASCADE"),
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"),
    )
