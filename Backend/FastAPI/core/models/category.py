from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .collection import Collection
    from .plant import Plant


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str]
    slug: Mapped[str]
    link: Mapped[str]
    description: Mapped[str]
    # TODO: consider ways to store image_url in database
    image_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
        onupdate=datetime.now,
    )
    collection_id: Mapped[int] = mapped_column(
        ForeignKey("collections.id"),
    )
    collection: Mapped["Collection"] = relationship(
        back_populates="categories",
    )
    plants: Mapped[list["Plant"]] = relationship(
        secondary="plant_category_association",
        cascade="all,delete",
        back_populates="categories",
    )
