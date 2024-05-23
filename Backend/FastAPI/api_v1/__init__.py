__all__ = (
    "router",
    "PlantRelationSchema",
    "CategoryRelationSchema",
    "CartRelationSchema",
    "UserRelationSchema",
)

from fastapi import APIRouter

from FastAPI.api_v1.relation_schemas import (
    CategoryRelationSchema,
    PlantRelationSchema,
    CartRelationSchema,
    UserRelationSchema,
)

# from .db_migration.script import router as migration_router
from FastAPI.auth.views import router as auth_router
from FastAPI.api_v1.carts.views import router as carts_router
from FastAPI.api_v1.categories.views import router as categories_router
from FastAPI.api_v1.collections.views import router as collections_router
from FastAPI.api_v1.plants.views import router as plants_router
from FastAPI.api_v1.profiles.views import router as profiles_router
from FastAPI.api_v1.users.views import router as users_router
from FastAPI.payment.views import router as payment_router
from FastAPI.api_v1.orders.views import router as orders_router

router = APIRouter()
# router.include_router(migration_router)
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(profiles_router)
router.include_router(carts_router)
router.include_router(orders_router)
router.include_router(payment_router)
router.include_router(collections_router)
router.include_router(categories_router)
router.include_router(plants_router)
