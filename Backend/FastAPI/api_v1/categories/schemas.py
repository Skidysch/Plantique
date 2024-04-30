from datetime import datetime

from pydantic import BaseModel, ConfigDict

from api_v1 import PlantRelationSchema


class CollectionInCategory(BaseModel):
    id: int
    name: str
    slug: str
    link: str
    description: str


class CategoryBase(BaseModel):
    name: str
    slug: str
    link: str
    description: str
    # TODO: consider ways to store image_url in database
    image_url: str
    collection_id: int


class CategorySchema(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime
    collection: CollectionInCategory | None = None
    plants: list[PlantRelationSchema] = []
    id: int


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryCreate):
    pass


class CategoryUpdatePartial(BaseModel):
    name: str | None = None
    slug: str | None = None
    link: str | None = None
    description: str | None = None
    image_url: str | None = None
