from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PlantBase(BaseModel):
    name: str
    slug: str
    link: str
    description: str
    soil_type: str
    # TODO: consider ways to store image_url in database
    image_url: str
    price: float
    stock_available: bool = False
    stock_quantity: int = 0

    # categories: list[Category]
    # carts: list[Cart]
    # orders: list[Order]


class Plant(PlantBase):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime
    # categories: list["Category"]
    id: int


class PlantCreate(PlantBase):
    # categories: list[int] = []
    pass


class PlantUpdate(PlantCreate):
    pass


class PlantUpdatePartial(BaseModel):
    name: str | None = None
    slug: str | None = None
    link: str | None = None
    description: str | None = None
    soil_type: str | None = None
    image_url: str | None = None
    price: float | None = None
    stock_available: bool | None = None
    stock_quantity: int | None = None