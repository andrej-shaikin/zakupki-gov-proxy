from fastapi import FastAPI

from apps.routes import router as apps_router
from conf import settings

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.PROJECT_TITLE,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url=settings.SWAGGER_URL,
    redoc_url=settings.REDOC_URL,
    openapi_url=settings.OPENAPI_URL,
)

app.include_router(router=apps_router)
