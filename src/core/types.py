
from typing import Type, Union

from .models import Base, Link

MODEL = Union[Base, Link]
TYPE_MODEL = Type[MODEL]

__all__ = ["MODEL", "TYPE_MODEL"]
