from typing import TYPE_CHECKING

from app.database import db_helper
from app.repositories import CityRepository, TemperatureRepository
from app.models import City, Temperature
from app.services.weather_api import WeatherAPI
from app.config import settings

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class WeatherService:
    def __init__(self, city_name: str = None):
        self.city_name = city_name or settings.weather_api.city
        self.weather_api = WeatherAPI()

    async def get_or_create_city(self, session: "AsyncSession") -> City:
        city_repo = CityRepository(session)
        city = await city_repo.get_by_name(self.city_name)
        if not city:
            city = await city_repo.create(City(name=self.city_name))
        return city

    async def fetch_temperature(self, city: City) -> dict:
        return await self.weather_api.get_temperature(city)

    @staticmethod
    async def save_temperature(session: "AsyncSession", temp_info: dict) -> Temperature:
        temp_repo = TemperatureRepository(session)
        return await temp_repo.create(Temperature(**temp_info))

    async def fetch_and_save(self):
        async with db_helper.session_factory() as session:
            city = await self.get_or_create_city(session)
            temp_info = await self.fetch_temperature(city)
            temp = await self.save_temperature(session, temp_info)
            return temp
