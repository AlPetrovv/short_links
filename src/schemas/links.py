import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, Field


class Link(BaseModel):
    source_url: Annotated[str, Field(max_length=400)]
    code: Annotated[str, Field(max_length=6)]
    use_count: int = Field(default=0)


class LinkIn(BaseModel):
    source_url: Annotated[str, Field(max_length=400)]

class LinkRead(Link):
    id: int
    created_at: datetime.datetime



class CreateLink(Link):
    pass

class UpdatePartialLink(BaseModel):
    id: int
    source_url: Optional[Annotated[str, Field(max_length=400)]] = None
    code: Optional[Annotated[str, Field(max_length=6)]] = None
    use_count: Optional[int] = None


