from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    birth_date: datetime | None = None
    profile_picture: str | None = None


class ProfileSchema(ProfileBase):
    # ORM mode
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class ProfileUpdatePartial(ProfileBase):
    pass
