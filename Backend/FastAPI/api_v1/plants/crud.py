from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .schemas import PlantCreate, PlantUpdate, PlantUpdatePartial
from core.models import Plant, Category


async def get_plants(
    session: AsyncSession,
) -> list[Plant]:
    query = (
        select(Plant)
        .options(
            selectinload(Plant.categories),
        )
        .order_by(Plant.id)
    )
    plants = await session.scalars(query)

    return list(plants)


async def get_plant(
    session: AsyncSession,
    search_field: str,
    search_value: str | int,
) -> Plant | None:
    match search_field:
        case "slug":
            query_field = Plant.slug
        case _:
            query_field = Plant.id

    query = (
        select(Plant)
        .options(selectinload(Plant.categories))
        .where(query_field == search_value)
    )
    plant: Plant | None = await session.scalar(query)
    return plant


async def create_plant(
    session: AsyncSession,
    plant_in: PlantCreate,
) -> Plant:
    if plant_in.categories:
        query = select(Category).where(Category.id.in_(plant_in.categories))
        result = await session.scalars(query)
        categories: list[Category] = list(result)
    else:
        categories = []
    del plant_in.categories

    plant = Plant(
        **plant_in.model_dump(),
        categories=categories,
    )
    session.add(plant)
    await session.commit()
    await session.refresh(
        plant,
        ["categories"],
    )

    return plant


async def update_plant(
    session: AsyncSession,
    plant: Plant,
    plant_update: PlantUpdate | PlantUpdatePartial,
    partial: bool = False,
) -> Plant:
    if plant_update.categories:
        query = select(Category).where(Category.id.in_(plant_update.categories))
        result = await session.scalars(query)
        categories = list(result)
        setattr(plant, "categories", categories)
    del plant_update.categories

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


async def get_plants_by_category_id(
    session: AsyncSession,
    category_id: int,
) -> list[Plant]:
    query = (
        select(Plant)
        .options(selectinload(Plant.categories))
        .where(Plant.categories.any(Category.id == category_id))
    )
    plants = await session.scalars(query)
    return list(plants)
