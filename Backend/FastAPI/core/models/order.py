from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .order_plant_association import OrderPlantAssociation


class Order(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "orders"

    plants_details: Mapped[list["OrderPlantAssociation"]] = relationship(
        back_populates="order",
    )
