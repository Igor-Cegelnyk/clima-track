from fastapi import HTTPException
from pydantic import BaseModel, field_validator, Field
from starlette import status

from app.schemas.city import CityRead
from app.utils.convert_date import date_str_to_int, date_int_to_str, time_int_to_str


class TemperatureDay(BaseModel):
    day: str

    @field_validator("day")
    @classmethod
    def validate_date(cls, value: str) -> int:
        try:
            return date_str_to_int(value)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Date is not valid",
            )


class CityRequest(BaseModel):
    city_name: str | None = Field(None, description="City name", examples=["Kyiv"])


class TemperatureBase(BaseModel):
    temperature: float
    temperature_date: int
    temperature_time: int


class TemperatureRead(TemperatureBase):
    id: int
    temperature_date: str
    temperature_time: str
    created_date: str
    created_time: str
    city: CityRead

    model_config = {"from_attributes": True}

    @field_validator("temperature_date", "created_date", mode="before")
    @classmethod
    def parse_date(cls, v) -> str:
        if isinstance(v, int):
            return date_int_to_str(v)
        return v

    @field_validator("temperature_time", "created_time", mode="before")
    @classmethod
    def parse_time(cls, v) -> str:
        if isinstance(v, int):
            return time_int_to_str(v)
        return v
