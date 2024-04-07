from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .category import Category


class Collection(Base):
    name: Mapped[str]
    slug: Mapped[str]
    link: Mapped[str]
    description: Mapped[str]
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
        back_populates="collection",
    )
