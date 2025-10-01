from typing import TYPE_CHECKING

from fastapi import Depends, Query

from app.config import settings
from app.database import db_helper
from app.models import City
from app.repositories import TemperatureRepository, CityRepository
from app.schemas.temperature import TemperatureDay

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_temp_repository(
    session: "AsyncSession" = Depends(db_helper.session_getter),
) -> TemperatureRepository:
    return TemperatureRepository(session=session)


async def get_city_repository(
    session: "AsyncSession" = Depends(db_helper.session_getter),
) -> CityRepository:
    return CityRepository(session=session)


async def get_system_city(
    city_repo: "CityRepository" = Depends(get_city_repository),
) -> City:
    return await city_repo.get_by_name(city_name=settings.weather_api.city)


async def validate_day(
    day: str = Query(
        ...,
        description="Temperature date",
        examples=["2025-10-01"],
    )
) -> int:
    return TemperatureDay(day=day).day
