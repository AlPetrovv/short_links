from fastapi import FastAPI
from routers import main_router

app = FastAPI(
    title="Short link API",
    description="Welcome to the Short link API",
)

app.include_router(main_router)

if __name__ == "__main__":
    import uvicorn
    from config import settings

    uvicorn.run(
        "main:app",
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        reload=settings.uvicorn.reload,
    )
