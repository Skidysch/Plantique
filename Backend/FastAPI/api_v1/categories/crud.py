from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import CategoryCreate, CategoryUpdate, CategoryUpdatePartial
from core.models import Category


async def get_categories(
    session: AsyncSession,
) -> list[Category]:
    query = select(Category).order_by(Category.id)
    result = await session.execute(query)
    categories = result.scalars().all()

    return list(categories)


async def get_category(
    session: AsyncSession,
    category_id: int,
) -> Category | None:
    return await session.get(Category, category_id)


async def create_category(
    session: AsyncSession,
    category_in: CategoryCreate,
) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()
    await session.refresh(category)

    return category


async def update_category(
    session: AsyncSession,
    category: Category,
    category_update: CategoryUpdate | CategoryUpdatePartial,
    partial: bool = False,
) -> Category:
    for key, value in category_update.model_dump(exclude_unset=partial).items():
        setattr(category, key, value)

    await session.commit()

    return category


async def delete_category(
    session: AsyncSession,
    category: Category,
) -> None:
    await session.delete(category)
    await session.commit()