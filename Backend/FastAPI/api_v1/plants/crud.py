from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import PlantCreate, PlantUpdate, PlantUpdatePartial
from core.models import Plant


async def get_plants(
    session: AsyncSession,
) -> list[Plant]:
    query = select(Plant).order_by(Plant.id)
    result = await session.execute(query)
    plants = result.scalars().all()

    return list(plants)


async def get_plant(
    session: AsyncSession,
    plant_id: int,
) -> Plant | None:
    return await session.get(Plant, plant_id)


async def create_plant(
    session: AsyncSession,
    plant_in: PlantCreate,
) -> Plant:
    plant = Plant(**plant_in.model_dump())
    session.add(plant)
    await session.commit()
    await session.refresh(plant)

    return plant


async def update_plant(
    session: AsyncSession,
    plant: Plant,
    plant_update: PlantUpdate | PlantUpdatePartial,
    partial: bool = False,
) -> Plant:
    for key, value in plant_update.model_dump(exclude_unset=partial).items():
        setattr(plant, key, value)

    await session.commit()

    return plant


async def delete_plant(
    session: AsyncSession,
    plant: Plant,
) -> None:
    await session.delete(plant)
    await session.commit()
