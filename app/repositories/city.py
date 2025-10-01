from typing import Annotated

from sqlalchemy import select

from app.models import City
from app.repositories import SqlAlchemyRepository


class CityRepository(SqlAlchemyRepository):
    model = City

    async def get_by_name(self, city_name: str) -> Annotated[City, None]:
        stmt = select(self.model).filter_by(name=city_name)
        result = await self.session.scalar(stmt)
        return result
