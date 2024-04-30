from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr

from api_v1 import CartRelationSchema
from api_v1.profiles.schemas import ProfileSchema


class UserBase(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr


class UserSchema(UserBase):
    # ORM mode
    model_config = ConfigDict(from_attributes=True)

    profile: ProfileSchema
    cart: CartRelationSchema

    is_active: bool
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
