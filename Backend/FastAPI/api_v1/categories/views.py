from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Category
from .dependencies import category_by_id
from .schemas import (
    CategorySchema,
    CategoryCreate,
    CategoryUpdate,
    CategoryUpdatePartial,
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get(
    "",
    response_model=list[CategorySchema],
)
async def get_categories(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_categories(
        session=session,
    )


@router.post(
    "",
    response_model=CategorySchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    category_in: CategoryCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_category(
        session=session,
        category_in=category_in,
    )


@router.get(
    "/{category_id}",
    response_model=CategorySchema,
)
async def get_category(
    category: Category = Depends(category_by_id),
):
    return category


@router.put(
    "/{category_id}",
    response_model=CategorySchema,
)
async def update_category(
    category_update: CategoryUpdate,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_category(
        session=session,
        category=category,
        category_update=category_update,
    )


@router.patch(
    "/{category_id}",
    response_model=CategorySchema,
)
async def update_category_partial(
    category_update: CategoryUpdatePartial,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_category(
        session=session,
        category=category,
        category_update=category_update,
        partial=True,
    )


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_category(
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_category(session=session, category=category)
