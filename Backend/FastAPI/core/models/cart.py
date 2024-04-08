from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .cart_plant_association import CartPlantAssociation


class Cart(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "cart"

    plants_details: Mapped[list["CartPlantAssociation"]] = relationship(
        cascade="all,delete",
        back_populates="cart",
    )
