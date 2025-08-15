import datetime as dt

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class IDPKINTMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


class CratedAtMixin:
    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime, default=dt.datetime.now, server_default=func.current_time()
    )
