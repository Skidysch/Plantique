from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from FastAPI.api_v1.collections.schemas import (
    CollectionCreate,
    CollectionUpdate,
    CollectionUpdatePartial,
)
from FastAPI.core.models import Collection


async def get_collections(
    session: AsyncSession,
) -> list[Collection]:
    query = (
        select(Collection)
        .options(selectinload(Collection.categories))
        .order_by(Collection.id)
    )
    collections = await session.scalars(query)

    return list(collections)


async def get_collection(
    session: AsyncSession,
    search_field: str,
    search_value: str | int,
) -> Collection | None:
    match search_field:
        case "slug":
            query_field = Collection.slug
            query_value = str(search_value)
        case _:
            query_field = Collection.id
            query_value = int(search_value)

    query = (
        select(Collection)
        .options(selectinload(Collection.categories))
        .where(query_field == query_value)
    )
    collection: Collection | None = await session.scalar(query)
    return collection


async def create_collection(
    session: AsyncSession,
    collection_in: CollectionCreate,
) -> Collection:
    collection = Collection(
        **collection_in.model_dump(),
        categories=[],
    )
    session.add(collection)
    await session.commit()
    await session.refresh(collection, ["categories"])

    return collection


async def update_collection(
    session: AsyncSession,
    collection: Collection,
    collection_update: CollectionUpdate | CollectionUpdatePartial,
    partial: bool = False,
) -> Collection:
    for key, value in collection_update.model_dump(exclude_unset=partial).items():
        setattr(collection, key, value)

    await session.commit()

    return collection


async def delete_collection(
    session: AsyncSession,
    collection: Collection,
) -> None:
    await session.delete(collection)
    await session.commit()
