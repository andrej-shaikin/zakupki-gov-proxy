import databases
import sqlalchemy
from environs import Env

env = Env()
env.read_env(override=True)

DEBUG: bool = env.bool("DEBUG", default=False)

DATABASE_URL: str = env.str("DATABASE_URL")

PROJECT_TITLE: str = env.str("PROJECT_TITLE", default="Прокси сервер ГосЗакупок")
PROJECT_DESCRIPTION: str = env.str("PROJECT_DESCRIPTION", default="")
PROJECT_VERSION: str = env.str("PROJECT_VERSION", default="0.0.1")

OPENAPI_URL: str = env.str("OPENAPI_URL", default="/docs/openapi.json")
SWAGGER_URL: str = env.str("SWAGGER_URL", default="/docs")
REDOC_URL: str = env.str("SWAGGER_URL", default="/redoc")

TIMEZONE = "Europe/Moskow"

__DATABASE = databases.Database(DATABASE_URL)
__DATABASE_METADATA = sqlalchemy.MetaData()
