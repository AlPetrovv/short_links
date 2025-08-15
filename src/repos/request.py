from dataclasses import dataclass
from .links import LinkRepo

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class RequestRepo:
    """
    Repo that contains all repos
    """
    session: AsyncSession

    @property
    def links(self) -> LinkRepo:
        return LinkRepo(session=self.session)
