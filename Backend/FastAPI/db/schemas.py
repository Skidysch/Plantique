from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    full_name: str | None = None
    email: str
    birth_date: date | None = None


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        # orm_mode
        from_attributes = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    birth_date: Optional[date] = None
    password: Optional[str] = None
