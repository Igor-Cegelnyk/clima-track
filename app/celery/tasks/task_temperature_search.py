import asyncio
from datetime import datetime

from app.schemas.temperature import TemperatureRead
from app.services.weather import WeatherService
from app.celery.celery_app import celery_app, log


@celery_app.task(
    bind=True,
    queue="ct_queue",
)
def run_temperature_search(self):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            result = asyncio.ensure_future(WeatherService().fetch_and_save())
        else:
            result = loop.run_until_complete(WeatherService().fetch_and_save())
        return {
            "task_id": self.request.id,
            "datetime": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "status": "success",
            "details": TemperatureRead.from_orm(result).dict(),
        }

    except Exception as exc:
        log.info("Помилка: %r", exc)
        self.retry(exc=exc)
        return None


if __name__ == "__main__":
    run_temperature_search()
