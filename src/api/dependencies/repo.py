from typing import AsyncGenerator

from core.db_helper import helper
from repos.request import RequestRepo


async def get_repo() -> AsyncGenerator[RequestRepo, None]:
    """Get request repo dependency"""
    async with helper.session_factory() as session:
        yield RequestRepo(session=session)
