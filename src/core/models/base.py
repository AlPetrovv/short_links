from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

from config import settings
from core.utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls):
        return f"{camel_case_to_snake_case(cls.__name__)}s"

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.__class__.__name__}"