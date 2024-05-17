from pydantic import BaseModel, ConfigDict

from api_v1 import PlantRelationSchema


class CartPlantAssociationSchema(BaseModel):
    id: int
    plant: PlantRelationSchema
    quantity: int


class CartBase(BaseModel):
    pass


class CartSchema(CartBase):
    # ORM mode
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    plants_details: list[CartPlantAssociationSchema]


class CartCreate(CartBase):
    pass


class CartUpdate(CartBase):
    quantity: int | None = None
    replace: bool | None = None
