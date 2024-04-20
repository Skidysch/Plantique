# from fastapi import Depends, APIRouter
# from sqlalchemy.ext.asyncio import AsyncSession

# from api_v1.categories.crud import get_categories, create_category
# from api_v1.categories.schemas import CategoryCreate
# from api_v1.plants.crud import get_plants, create_plant
# from api_v1.plants.schemas import PlantCreate
# from core.models import db_helper, db_helper_sqlite

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
