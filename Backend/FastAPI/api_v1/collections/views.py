from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper, Collection
from .dependencies import collection_by_id, collection_by_slug
from .schemas import (
    CollectionSchema,
    CollectionCreate,
    CollectionUpdate,
    CollectionUpdatePartial,
)

router = APIRouter(prefix="/collections", tags=["Collections"])


@router.get(
    "",
    response_model=list[CollectionSchema],
)
async def get_collections(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_collections(
        session=session,
    )


@router.post(
    "",
    response_model=CollectionSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_collection(
    collection_in: CollectionCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_collection(
        session=session,
        collection_in=collection_in,
    )


@router.get(
    "/id/{collection_id}",
    response_model=CollectionSchema,
)
async def get_collection_by_id(
    collection: Collection = Depends(collection_by_id),
):
    return collection


@router.get(
    "/slug/{collection_slug}",
    response_model=CollectionSchema,
)
async def get_collection_by_slug(
    collection: Collection = Depends(collection_by_slug),
):
    return collection


@router.put(
    "/{collection_id}",
    response_model=CollectionSchema,
)
async def update_collection(
    collection_update: CollectionUpdate,
    collection: Collection = Depends(collection_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_collection(
        session=session,
        collection=collection,
        collection_update=collection_update,
    )


@router.patch(
    "/{collection_id}",
    response_model=CollectionSchema,
)
async def update_collection_partial(
    collection_update: CollectionUpdatePartial,
    collection: Collection = Depends(collection_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_collection(
        session=session,
        collection=collection,
        collection_update=collection_update,
        partial=True,
    )


@router.delete(
    "/{collection_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_collection(
    collection: Collection = Depends(collection_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_collection(session=session, collection=collection)
