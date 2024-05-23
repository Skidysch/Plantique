from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from FastAPI.core.models.base import Base
from FastAPI.core.models.mixins import UserRelationMixin


class Profile(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(
        String(40),
    )
    last_name: Mapped[str | None] = mapped_column(
        String(40),
    )
    birth_date: Mapped[date | None]
    profile_picture: Mapped[str | None]
