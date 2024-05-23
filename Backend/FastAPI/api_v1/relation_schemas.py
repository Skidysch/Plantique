from pydantic import BaseModel

from FastAPI.api_v1.profiles.schemas import ProfileSchema


class PlantRelationSchema(BaseModel):
    id: int
    name: str
    slug: str
    link: str
    description: str
    soil_type: str
    image_url: str
    price: float
    stock_available: bool = False
    stock_quantity: int = 0


class CategoryRelationSchema(BaseModel):
    id: int
    name: str
    slug: str
    link: str
    description: str
    image_url: str


class CartRelationSchema(BaseModel):
    id: int


class UserRelationSchema(BaseModel):
    id: int
    profile: ProfileSchema
    username: str
    email: str
