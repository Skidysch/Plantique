from datetime import datetime

from pydantic import BaseModel, ConfigDict

from FastAPI.api_v1 import CategoryRelationSchema


class CollectionBase(BaseModel):
    name: str
    slug: str
    link: str
    description: str


class CollectionSchema(CollectionBase):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime
    categories: list[CategoryRelationSchema] = []
    id: int


class CollectionCreate(CollectionBase):
    pass


class CollectionUpdate(CollectionCreate):
    pass


class CollectionUpdatePartial(BaseModel):
    name: str | None = None
    slug: str | None = None
    link: str | None = None
    description: str | None = None
