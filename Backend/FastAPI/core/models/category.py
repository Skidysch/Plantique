from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


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
    # collection_id: Mapped[int] = mapped_column(
    #     ForeignKey("collections.id"),
    # )
    # collection = relationship('Collection', back_populates='categories')
    # plants = relationship('Plant',
    #                       secondary=plant_category_association,
    #                       back_populates='categories'
    #                       )

    # categories: Mapped[list[Category]] = relationship('Category', secondary=PlantCategoryAssociation, back_populates="plants",)
    # carts: Mapped[list[Cart]] = relationship('Cart', secondary=PlantCartAssociation, back_populates="plants",)
    # orders: Mapped[list[Order]] = relationship('Order', secondary=PlantOrderAssociation, back_populates="plants",)