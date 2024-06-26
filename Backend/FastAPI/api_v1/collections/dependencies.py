from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.collections import crud
from FastAPI.core.models import db_helper, Collection


async def collection_by_id(
    collection_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Collection:
    collection = await crud.get_collection(
        session=session,
        search_field="id",
        search_value=collection_id,
    )
    if collection is not None:
        return collection
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Collection not found!",
    )


async def collection_by_slug(
    collection_slug: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Collection:
    collection = await crud.get_collection(
        session=session,
        search_field="slug",
        search_value=collection_slug,
    )
    if collection is not None:
        return collection
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Collection not found!",
    )
