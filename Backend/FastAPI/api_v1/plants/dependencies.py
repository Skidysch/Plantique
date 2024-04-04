from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Plant


async def plant_by_id(
    plant_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Plant:
    plant = await crud.get_plant(
        session=session,
        plant_id=plant_id,
    )
    if plant is not None:
        return plant
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Plant not found!",
    )
