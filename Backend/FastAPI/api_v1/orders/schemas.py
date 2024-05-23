from datetime import datetime
from pydantic import BaseModel, ConfigDict

from FastAPI.api_v1.carts.schemas import CartSchema
from FastAPI.api_v1 import PlantRelationSchema, UserRelationSchema


class OrderPlantAssociationSchema(BaseModel):
    id: int
    plant: PlantRelationSchema
    quantity: int
    unit_price: float


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    cart: CartSchema


class OrderSchema(OrderBase):
    model_config = ConfigDict(from_attributes=True)
    user: UserRelationSchema
    plants_details: list[OrderPlantAssociationSchema] = []
    created_at: datetime
    updated_at: datetime
    paid: bool
    id: int


class UserInOrderCreateSchema(BaseModel):
    id: int
    username: str
    email: str


class PlantsInOrderCreateSchema(BaseModel):
    id: int
    quantity: int
    unit_price: float


class OrderCreatedSchema(OrderBase):
    user: UserInOrderCreateSchema
    plants_details: list[PlantsInOrderCreateSchema] = []
    created_at: datetime
    updated_at: datetime
    paid: bool
    id: int
