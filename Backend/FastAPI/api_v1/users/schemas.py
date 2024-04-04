# from datetime import date, datetime
from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr
    # first_name: str | None = None
    # last_name: str | None = None
    # birth_date: date | None = None
    # profile_picture: str | None = None


class User(UserBase):
    # ORM mode
    model_config = ConfigDict(from_attributes=True)

    is_active: bool
    id: int


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    # full_name: Optional[str] = None
    # birth_date: Optional[date] = None
    # profile_picture: Optional[str] = None
    # gender: Optional[str] = None
