from typing import Optional

from core.models import Link
from schemas.links import CreateLink, UpdatePartialLink
from .base import BaseRepo


class LinkRepo(BaseRepo):
    """Repo for links"""

    async def get_link(self, link_id: int) -> Optional[Link]:
        return await self._get_model(Link, [Link.id == link_id])

    async def get_link_by_code(self, short_url: str) -> Optional[Link]:
        return await self._get_model(Link, [Link.code == short_url])

    async def get_link_by_source_url(self, source_url: str) -> Optional[Link]:
        return await self._get_model(Link, [Link.source_url == source_url])

    async def create_link(self, link_in: CreateLink) -> Link:
        return await self._create_model(Link, link_in)

    async def update_partial_link(self, link_in: UpdatePartialLink) -> Link:
        return await self._update_partial_model(Link, link_in)
