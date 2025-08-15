from typing import TYPE_CHECKING
from urllib.parse import urljoin

import validators
from fastapi import APIRouter, Request, Depends, HTTPException
from starlette import status
from starlette.responses import RedirectResponse

from api.dependencies.repo import get_repo
from schemas.links import LinkIn, LinkRead, CreateLink, UpdatePartialLink
from services.links import create_code

router = APIRouter(tags=["Links"])

if TYPE_CHECKING:
    from repos.request import RequestRepo


@router.post("/shorten", status_code=201)
async def shorten_link(request: Request, link_in: LinkIn, repo: "RequestRepo" = Depends(get_repo)):
    """ Create short link and return short url"""
    # check if source url is valid
    if not validators.url(str(link_in.source_url)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid URL")
    # check if source url already exists
    exists_link = await repo.links.get_link_by_source_url(str(link_in.source_url))
    if exists_link is not None:
        return exists_link
    code = create_code()
    # generate code until it is unique
    while await repo.links.get_link_by_code(code) is not None:
        code = create_code()
    # create link
    link_in = CreateLink(source_url=link_in.source_url, code=code)
    link = await repo.links.create_link(link_in)
    return {"short_url": link.get_short_url(str(request.base_url))}


@router.get("/s/{code}")
async def redirect_link(code: str, repo: "RequestRepo" = Depends(get_repo)):
    """Redirect to source url by code"""
    link = await repo.links.get_link_by_code(code)
    if link is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")
    link_in = UpdatePartialLink.model_validate({"id": link.id, "use_count": link.use_count + 1})
    await repo.links.update_partial_link(link_in)
    return RedirectResponse(link.source_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)


@router.get("/stats/{code}", response_model=LinkRead, response_model_exclude={"code", "id"})
async def get_stats(code: str, repo: "RequestRepo" = Depends(get_repo)):
    return await repo.links.get_link_by_code(code)
