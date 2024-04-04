from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Plant as plant_model
from .dependencies import plant_by_id
from .schemas import Plant, PlantCreate, PlantUpdate, PlantUpdatePartial

router = APIRouter(prefix="/plants", tags=["Plants"])


@router.get(
    "",
    response_model=list[Plant],
)
async def get_plants(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_plants(
        session=session,
    )


@router.post(
    "",
    response_model=Plant,
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
    "/{plant_id}",
    response_model=Plant,
)
async def get_plant(
    plant: plant_model = Depends(plant_by_id),
):
    return plant


@router.put(
    "/{plant_id}",
    response_model=Plant,
)
async def update_plant(
    plant_update: PlantUpdate,
    plant: plant_model = Depends(plant_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_plant(
        session=session,
        plant=plant,
        plant_update=plant_update,
    )


@router.patch(
    "/{plant_id}",
    response_model=Plant,
)
async def update_plant_partial(
    plant_update: PlantUpdatePartial,
    plant: plant_model = Depends(plant_by_id),
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
    plant: plant_model = Depends(plant_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_plant(session=session, plant=plant)
