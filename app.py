from fastapi import FastAPI

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
