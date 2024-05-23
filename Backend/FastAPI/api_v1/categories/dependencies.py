from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.categories import crud
from FastAPI.core.models import db_helper, Category


async def category_by_id(
    category_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Category:
    category = await crud.get_category(
        session=session,
        search_field="id",
        search_value=category_id,
    )
    if category is not None:
        return category
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Category not found!",
    )


async def category_by_slug(
    category_slug: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Category:
    category = await crud.get_category(
        session=session,
        search_field="slug",
        search_value=category_slug,
    )
    if category is not None:
        return category
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Category not found!",
    )
