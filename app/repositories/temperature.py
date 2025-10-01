from app.models import Temperature
from app.repositories import SqlAlchemyRepository


class TemperatureRepository(SqlAlchemyRepository):
    model = Temperature
