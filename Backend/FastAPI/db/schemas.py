from datetime import date, datetime
from typing import List, Optional, Type

from pydantic import BaseModel


# Users
class UserBase(BaseModel):
    username: str
    full_name: str | None = None
    email: str
    birth_date: date | None = None
    gender: str
    profile_picture: str | None = None


class User(UserBase):
    is_active: bool
    id: int

    class Config:
        # orm_mode
        from_attributes = True


class UserAdmin(User):
    password: str
    role: str
    created_at: datetime


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    birth_date: Optional[date] = None
    password: Optional[str] = None
    profile_picture: Optional[str] = None
    gender: Optional[str] = None


# Related models
class PlantRelated(BaseModel):
    id: int
    name: str
    slug: str
    link: str


class CategoryRelated(BaseModel):
    id: int
    name: str
    slug: str
    link: str


class CollectionRelated(BaseModel):
    id: int
    name: str
    slug: str
    link: str


# Plants
class PlantBase(BaseModel):
    name: str
    slug: str
    link: str
    description: str
    soil_type: str
    image_url: str
    price: float
    stock_available: bool = False
    stock_quantity: int = 0


class Plant(PlantBase):
    created_at: datetime
    updated_at: datetime
    categories: List[CategoryRelated]
    id: int

    class Config:
        # orm_mode
        from_attributes = True


class PlantCreate(PlantBase):
    categories: List[int] = []


class PlantUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    soil_type: Optional[str] = None
    image_url: Optional[str] = None
    price: Optional[float] = None
    stock_available: Optional[bool] = None
    stock_quantity: Optional[int] = None
    categories: Optional[List[int]] = None


# Categories
class CategoryBase(BaseModel):
    name: str
    slug: str
    link: str
    description: str
    image_url: str


class Category(CategoryBase):
    created_at: datetime
    updated_at: datetime
    collection_id: int
    collection: CollectionRelated
    plants: List[PlantRelated]
    id: int

    class Config:
        # orm_mode
        from_attributes = True


class CategoryCreate(CategoryBase):
    collection_id: int
    plants: List[int]


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    link: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    collection_id: Optional[int] = None
    plants: Optional[List[int]] = None


# Collections
class CollectionBase(BaseModel):
    name: str
    slug: str
    link: str
    description: str


class Collection(CollectionBase):
    created_at: datetime
    updated_at: datetime
    categories: List[CategoryRelated]
    id: int

    class Config:
        # orm_mode
        from_attributes = True


class CollectionCreate(CollectionBase):
    pass


class CollectionUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    link: Optional[str] = None
    description: Optional[str] = None


PlantCreate.model_rebuild()
CategoryCreate.model_rebuild()
CollectionCreate.model_rebuild()
