from typing import TYPE_CHECKING

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship

from FastAPI.core.models.base import Base
from FastAPI.core.models.mixins import UserRelationMixin
from FastAPI.core.models.db_helper import db_helper

if TYPE_CHECKING:
    from FastAPI.core.models.cart_plant_association import (
        CartPlantAssociation,
    )


class Cart(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "cart"

    plants_details: Mapped[list["CartPlantAssociation"]] = relationship(
        cascade="all,delete",
        back_populates="cart",
    )

    async def clear(
        self,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ):
        for association in self.plants_details:
            await session.delete(association)
        await session.commit()
