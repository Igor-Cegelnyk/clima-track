from typing import TYPE_CHECKING

from fastapi import Depends

from app.database import db_helper
from app.repositories import TemperatureRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_repository(
    session: "AsyncSession" = Depends(db_helper.session_getter),
) -> TemperatureRepository:
    return TemperatureRepository(session=session)
