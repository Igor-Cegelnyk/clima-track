import asyncio
from datetime import datetime

import httpx

from app.config import settings
from app.models import City
from app.utils.convert_date import to_tz_datetime


class WeatherAPI:

    @staticmethod
    async def get_weather_info(city_name: str):
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                settings.weather_api.url,
                params={
                    "q": city_name,
                    "appid": settings.weather_api.api_key,
                    "units": "metric",
                },
            )
            resp.raise_for_status()
            return resp.json()

    async def get_temperature(self, city: City):
        weather = await self.get_weather_info(city_name=city.name)
        dt = to_tz_datetime(weather["dt"])
        return {
            "city_id": city.id,
            "temperature": weather["main"]["temp"],
            "temperature_date": int(dt.strftime("%Y%m%d")),
            "temperature_time": int(dt.strftime("%H%M%S")),
        }


if __name__ == "__main__":
    req = WeatherAPI()
    res = asyncio.run(req.get_temperature())
    print(res)
