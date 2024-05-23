from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from FastAPI.core.models.base import Base
from FastAPI.core.models.mixins import UserRelationMixin

if TYPE_CHECKING:
    from FastAPI.core.models.order_plant_association import (
        OrderPlantAssociation,
    )


class Order(Base, UserRelationMixin):
    _user_back_populates = "orders"

    plants_details: Mapped[list["OrderPlantAssociation"]] = relationship(
        cascade="all,delete",
        back_populates="order",
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
    paid: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
    )
