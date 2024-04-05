# from typing import TYPE_CHECKING

# from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .mixins import UserRelationMixin

# if TYPE_CHECKING:
#     from .plant import Plant


class Cart(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "cart"

    # plants: Mapped[list["Plant"]] = relationship(
    #     "Plant",
    #     secondary=PlantCartAssociation,
    #     back_populates="carts",
    # )