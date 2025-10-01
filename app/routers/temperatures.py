from fastapi import APIRouter

from app.config import settings

router = APIRouter(
    prefix=settings.api_prefix.temperatures,
    tags=["Temperature"],
)


@router.get(
    "/",
    summary="",
)
async def get_temperatures() -> None:
    return None
