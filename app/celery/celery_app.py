from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger
from kombu import Exchange, Queue
from celery.schedules import crontab

from app.config import settings, Logger

log = Logger().get_logger()

celery_app = Celery(
    "app.celery.celery_app",
    broker=settings.redis.celery_url_backend,
    backend=settings.redis.celery_url_backend,
)


@after_setup_logger.connect
def setup_celery_logger(logger, *args, **kwargs):
    logger.handlers = []
    logger.addHandler(log.handlers[0])
    logger.setLevel(log.level)


@after_setup_task_logger.connect
def setup_celery_task_logger(logger, *args, **kwargs):
    logger.handlers = []
    logger.addHandler(log.handlers[0])
    logger.setLevel(log.level)


celery_app.conf.update(
    broker_connection_retry_on_startup=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Europe/Kiev",
    enable_utc=False,
    task_default_queue="ct_queue",
    result_expires=settings.redis.expires,
    task_queues=[
        Queue(
            "ct_queue",
            Exchange("ct_queue"),
            routing_key="ct_queue",
        )
    ],
    worker_send_task_events=True,
)


celery_app.conf.beat_schedule = {
    "run_temperature_search": {
        "task": "app.celery.tasks.task_temperature_search.run_temperature_search",
        "schedule": crontab(minute=0),
    },
}

celery_app.autodiscover_tasks(["app.celery.tasks"])
