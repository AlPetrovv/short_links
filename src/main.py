from fastapi import FastAPI
from routers import main_router

from config import settings

app = FastAPI(
    title="Short link API",
    description="Welcome to the Short link API",
)

app.include_router(main_router)

if __name__ == "__main__":
    import uvicorn
    import logging
    logger = logging.getLogger(__name__)
    logger.error(settings.db.url)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.uvicorn.reload)
