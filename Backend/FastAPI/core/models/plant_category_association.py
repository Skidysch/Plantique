from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from FastAPI.core.models.base import Base


class PlantCategoryAssociation(Base):
    __tablename__ = "plant_category_association"
    __table_args__ = (
        UniqueConstraint(
            "plant_id",
            "category_id",
            name="idx_unique_plant_category",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    plant_id: Mapped[int] = mapped_column(
        ForeignKey("plants.id", ondelete="CASCADE"),
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"),
    )
