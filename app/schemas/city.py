from pydantic import BaseModel


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class CityRead(CityBase):
    id: int

    model_config = {"from_attributes": True}
