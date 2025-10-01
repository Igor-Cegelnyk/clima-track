__all__ = ["router"]

from fastapi import APIRouter

from .temperatures import router as temperature


router = APIRouter()

router.include_router(temperature)
