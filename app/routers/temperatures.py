from typing import List, TYPE_CHECKING

from fastapi import APIRouter, Depends

from app.auth.dependencies import verify_token
from app.config import settings
from app.repositories import TemperatureRepository
from app.routers.dependencies import get_temp_repository, validate_day, get_system_city
from app.schemas.temperature import TemperatureRead, CityRequest
from app.services.weather import WeatherService


if TYPE_CHECKING:
    from app.models import City


router = APIRouter(
    prefix=settings.api_prefix.temperatures,
    tags=["Temperature"],
)


@router.get(
    "/",
    summary="Get temperatures by date",
    response_model=List[TemperatureRead],
    dependencies=[Depends(verify_token)],
)
async def get_temperatures(
    day: int = Depends(validate_day),
    city: "City" = Depends(get_system_city),
    temp_repo: TemperatureRepository = Depends(get_temp_repository),
) -> List[TemperatureRead]:
    result = await temp_repo.get_all({"temperature_date": day, "city_id": city.id})
    return [TemperatureRead.model_validate(elem) for elem in result]


@router.post(
    "/",
    summary="Loading the temperature for the current time",
    response_model=TemperatureRead,
    dependencies=[Depends(verify_token)],
)
async def load_temperatures(
    params: CityRequest,
) -> TemperatureRead:
    service = WeatherService(params.city_name)
    temp = await service.fetch_and_save()
    return TemperatureRead.model_validate(temp)
