from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.plants import crud
from FastAPI.core.models import db_helper, Plant


async def plant_by_id(
    plant_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Plant:
    plant = await crud.get_plant(
        session=session,
        search_field="id",
        search_value=plant_id,
    )
    if plant is not None:
        return plant
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Plant not found!",
    )


async def plant_by_slug(
    plant_slug: Annotated[str, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Plant:
    plant = await crud.get_plant(
        session=session,
        search_field="slug",
        search_value=plant_slug,
    )
    if plant is not None:
        return plant
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Plant not found!",
    )
