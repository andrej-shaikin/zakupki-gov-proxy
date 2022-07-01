from datetime import datetime

import ormar

from conf import settings


class BaseModel(ormar.Model):
    id: int = ormar.Integer(primary_key=True, unique=True, autoincrement=True)
    created_at: datetime = ormar.DateTime(timezone=settings.TIMEZONE, default=datetime.now, nullable=True)


__all__ = ["BaseModel"]
