from FastAPI.api_v1.collections.crud import (
    get_collections,
    create_collection,
)
from FastAPI.api_v1.collections.schemas import CollectionCreate
from FastAPI.api_v1.categories.crud import (
    get_categories,
    create_category,
)
from FastAPI.api_v1.categories.schemas import CategoryCreate
from FastAPI.api_v1.plants.crud import get_plants, create_plant
from FastAPI.api_v1.plants.schemas import PlantCreate

from FastAPI.core.models import db_helper, db_helper_local

# Endpoint variation for migration
# from fastapi import Depends, APIRouter

# from core.models import db_helper_sqlite

# router = APIRouter(prefix="/migration", tags=["Migration"])


# @router.get("")
# async def main(
#     sqlite_session: AsyncSession = Depends(
#         db_helper_sqlite.scoped_session_dependency,
#     ),
#     pg_session: AsyncSession = Depends(
#         db_helper.scoped_session_dependency,
#     ),
# ):
# categories_sqlite = await get_categories(session=sqlite_session)
# for category in categories[4:]:
#     category.collection_id += 1
#     category_schema = {
#         "name": category.name,
#         "slug": category.slug,
#         "link": category.link,
#         "description": category.description,
#         "image_url": category.image_url,
#         "collection_id": category.collection_id,
#     }
#     category_in = CategoryCreate.model_validate(category_schema)
#     await create_category(session=pg_session, category_in=category_in)
# plants = await get_plants(session=sqlite_session)
# for plant in plants[7:]:
#     categories = [cat.id + 1 for cat in plant.categories]
#     plant_schema = {
#         "name": plant.name,
#         "slug": plant.slug,
#         "link": plant.link,
#         "description": plant.description,
#         "soil_type": plant.soil_type,
#         "image_url": plant.image_url,
#         "price": plant.price,
#         "stock_available": True,
#         "stock_quantity": 10,
#         "categories": categories
#     }
#     plant_in = PlantCreate.model_validate(plant_schema)
#     await create_plant(session=pg_session, plant_in=plant_in)


# Script variation for migration
async def migrate_from_local_db_to_docker_db():
    async with db_helper_local.session_factory() as pg_session, db_helper.session_factory() as docker_session:
        collections_docker = await get_collections(session=docker_session)
        # Don't fill the container database, if it is not empty
        if len(collections_docker):
            return

        collections = await get_collections(session=pg_session)
        for collection in collections:
            collection_schema = {
                "name": collection.name,
                "slug": collection.slug,
                "link": collection.link,
                "description": collection.description,
            }
            collection_in = CollectionCreate.model_validate(collection_schema)
            await create_collection(
                session=docker_session,
                collection_in=collection_in,
            )

        categories = await get_categories(session=pg_session)
        for category in categories:
            category.collection_id -= 1
            category_schema = {
                "name": category.name,
                "slug": category.slug,
                "link": category.link,
                "description": category.description,
                "image_url": category.image_url,
                "collection_id": category.collection_id,
            }
            category_in = CategoryCreate.model_validate(category_schema)
            await create_category(
                session=docker_session,
                category_in=category_in,
            )

        plants = await get_plants(session=pg_session)
        for plant in plants:
            categories = [cat.id - 1 for cat in plant.categories]
            plant_schema = {
                "name": plant.name,
                "slug": plant.slug,
                "link": plant.link,
                "description": plant.description,
                "soil_type": plant.soil_type,
                "image_url": plant.image_url,
                "price": plant.price,
                "stock_available": True,
                "stock_quantity": 10,
                "categories": categories,
            }
            plant_in = PlantCreate.model_validate(plant_schema)
            await create_plant(session=docker_session, plant_in=plant_in)


if __name__ == "__main__":
    import asyncio
    asyncio.run(migrate_from_local_db_to_docker_db())
