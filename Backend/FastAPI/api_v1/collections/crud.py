from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import CollectionCreate, CollectionUpdate, CollectionUpdatePartial
from core.models import Collection


async def get_collections(
    session: AsyncSession,
) -> list[Collection]:
    query = select(Collection).order_by(Collection.id)
    result = await session.execute(query)
    collections = result.scalars().all()

    return list(collections)


async def get_collection(
    session: AsyncSession,
    collection_id: int,
) -> Collection | None:
    return await session.get(Collection, collection_id)


async def create_collection(
    session: AsyncSession,
    collection_in: CollectionCreate,
) -> Collection:
    collection = Collection(**collection_in.model_dump())
    session.add(collection)
    await session.commit()
    await session.refresh(collection)

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
