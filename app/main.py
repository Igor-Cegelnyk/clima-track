from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.config import settings
from app.database import db_helper
from app.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # Clean up the ML models and release the resources
    db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
)

main_app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
