from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .mixins import UserRelationMixin

from .base import Base


class Profile(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(
        String(40),
    )
    last_name: Mapped[str | None] = mapped_column(
        String(40),
    )
    birth_date: Mapped[datetime | None]
    profile_picture: Mapped[str | None]
