from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from FastAPI.api_v1.plants import crud
from FastAPI.core.models import db_helper, Plant
from FastAPI.api_v1.plants.dependencies import (
    plant_by_id,
    plant_by_slug,
)
from FastAPI.api_v1.plants.schemas import (
    PlantSchema,
    PlantCreate,
    PlantUpdate,
    PlantUpdatePartial,
)

router = APIRouter(prefix="/plants", tags=["Plants"])


@router.get(
    "",
    response_model=list[PlantSchema],
)
async def get_plants(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_plants(
        session=session,
    )


@router.post(
    "",
    response_model=PlantSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_plant(
    plant_in: PlantCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_plant(
        session=session,
        plant_in=plant_in,
    )


@router.get(
    "/id/{plant_id}",
    response_model=PlantSchema,
)
async def get_plant_by_id(
    plant: Plant = Depends(plant_by_id),
):
    return plant


@router.get(
    "/slug/{plant_slug}",
    response_model=PlantSchema,
)
async def get_plant_by_slug(
    plant: Plant = Depends(plant_by_slug),
):
    return plant


@router.put(
    "/{plant_id}",
    response_model=PlantSchema,
)
async def update_plant(
    plant_update: PlantUpdate,
    plant: Plant = Depends(plant_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_plant(
        session=session,
        plant=plant,
        plant_update=plant_update,
    )


@router.patch(
    "/{plant_id}",
    response_model=PlantSchema,
)
async def update_plant_partial(
    plant_update: PlantUpdatePartial,
    plant: Plant = Depends(plant_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_plant(
        session=session,
        plant=plant,
        plant_update=plant_update,
        partial=True,
    )


@router.delete(
    "/{plant_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_plant(
    plant: Plant = Depends(plant_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_plant(session=session, plant=plant)


@router.get(
    "/filter/{category_id}",
    response_model=list[PlantSchema],
)
async def filter_plants_by_category(
    category_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Plant]:
    return await crud.get_plants_by_category_id(
        session=session,
        category_id=category_id,
    )
