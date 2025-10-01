from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


from app.config import settings
from app.routers import router


main_app = FastAPI()

main_app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
