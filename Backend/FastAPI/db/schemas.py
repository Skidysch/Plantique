from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    full_name: str
    email: str
    birth_date: date


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        # orm_mode
        from_attributes = True
