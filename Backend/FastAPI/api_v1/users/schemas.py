from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr

from api_v1.carts.schemas import CartUser
from api_v1.profiles.schemas import Profile


class UserBase(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr


class User(UserBase):
    # ORM mode
    model_config = ConfigDict(from_attributes=True)

    profile: Profile
    cart: CartUser

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
