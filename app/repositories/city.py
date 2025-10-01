from app.models import City
from app.repositories import SqlAlchemyRepository


class CityRepository(SqlAlchemyRepository):
    model = City
