from pydantic import BaseModel, ConfigDict

# from api_v1.plants.schemas import Plant


class CartBase(BaseModel):
    pass


class CartUser(CartBase):
    id: int


class CartSchema(CartBase):
    # ORM mode
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    # plants: list[Plant]


class CartCreate(CartBase):
    pass


class CartUpdate(CartBase):
    pass
