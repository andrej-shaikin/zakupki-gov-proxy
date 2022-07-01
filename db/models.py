from datetime import datetime

import ormar

from conf import settings


class BaseModel(ormar.Model):
    id: int = ormar.Integer(primary_key=True, unique=True, autoincrement=True)
    created_at: datetime = ormar.DateTime(timezone=settings.TIMEZONE, default=datetime.now, nullable=True)

    class Meta:
        abstract = True
        database = settings.DATABASE
        metadata = settings.DATABASE_METADATA


__all__ = ["BaseModel"]
