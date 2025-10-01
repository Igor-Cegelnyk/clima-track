import asyncio

import httpx

from app.config import settings
from app.config.config import WeatherApiSettings


class WeatherAPI:

    @staticmethod
    async def get_weather_info():
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                settings.weather_api.url,
                params={
                    "q": settings.weather_api.city,
                    "appid": settings.weather_api.api_key,
                    "units": "metric",
                },
            )
            resp.raise_for_status()
            return resp.json()

    async def get_temperature(self):
        weather = await self.get_weather_info()
        return {"temperature": weather["main"]["temp"], "date": weather["dt"]}


if __name__ == "__main__":
    req = WeatherAPI()
    res = asyncio.run(req.get_temperature())
    print(res)
