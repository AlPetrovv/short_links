from typing import Type, Union

from .models import Base, Link

# MODEL - Union all models
MODEL = Union[Base, Link]

# TYPE_MODEL - Union all models(use for typing)
TYPE_MODEL = Type[MODEL]

__all__ = ["MODEL", "TYPE_MODEL"]
