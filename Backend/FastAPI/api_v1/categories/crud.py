from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from FastAPI.api_v1.categories.schemas import (
    CategoryCreate,
    CategoryUpdate,
    CategoryUpdatePartial,
)
from FastAPI.core.models import Category


async def get_categories(
    session: AsyncSession,
) -> list[Category]:
    query = (
        select(Category)
        .options(
            selectinload(Category.plants),
            joinedload(Category.collection),
        )
        .order_by(Category.id)
    )
    categories = await session.scalars(query)

    return list(categories)


async def get_category(
    session: AsyncSession,
    search_field: str,
    search_value: str | int,
) -> Category | None:
    match search_field:
        case "slug":
            query_field = Category.slug
        case _:
            query_field = Category.id

    query = (
        select(Category)
        .options(
            selectinload(Category.plants),
            joinedload(Category.collection),
        )
        .where(query_field == search_value)
    )
    category: Category | None = await session.scalar(query)
    return category


async def create_category(
    session: AsyncSession,
    category_in: CategoryCreate,
) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()
    await session.refresh(category, ["plants", "collection"])

    return category


async def update_category(
    session: AsyncSession,
    category: Category,
    category_update: CategoryUpdate | CategoryUpdatePartial,
    partial: bool = False,
) -> Category:
    for (
        key,
        value,
    ) in category_update.model_dump(exclude_unset=partial).items():
        setattr(category, key, value)

    await session.commit()

    return category


async def delete_category(
    session: AsyncSession,
    category: Category,
) -> None:
    await session.delete(category)
    await session.commit()


async def get_categories_by_collection_id(
    session: AsyncSession,
    collection_id: int,
) -> list[Category]:
    query = (
        select(Category)
        .options(
            joinedload(Category.collection),
            selectinload(Category.plants),
        )
        .where(Category.collection_id == collection_id)
    )
    categories = await session.scalars(query)
    return list(categories)
