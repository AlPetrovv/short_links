from urllib.parse import urljoin

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IDPKINTMixin, CratedAtMixin


class Link(IDPKINTMixin, CratedAtMixin, Base):
    source_url: Mapped[str] = mapped_column(String(400))
    code: Mapped[str] = mapped_column(String(6))
    use_count: Mapped[int] = mapped_column(default=0)

    def __str__(self):
        return f"Link{self.id}: {self.source_url} -> {self.code}"


    def get_short_url(self, base_url: str) -> str:
        return urljoin(base_url, self.code)