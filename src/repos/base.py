from typing import Any, TYPE_CHECKING, Optional

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


if TYPE_CHECKING:
    from core.types import MODEL, TYPE_MODEL


class BaseRepo:
    """Base repo, use for all repos"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_model(
        self, model: "TYPE_MODEL", conditions: list[Any]
    ) -> Optional["MODEL"]:
        smtp = select(model).where(*conditions)
        return await self.session.scalar(smtp)

    async def _create_model(self, model: "TYPE_MODEL", model_in) -> "MODEL":
        instance = model(**model_in.model_dump(exclude_unset=True))
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def _update_partial_model(self, model: "TYPE_MODEL", model_in) -> "MODEL":
        instance = await self._get_model(model, conditions=[model.id == model_in.id])
        for field, value in model_in.model_dump(exclude_unset=True).items():
            setattr(instance, field, value)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
