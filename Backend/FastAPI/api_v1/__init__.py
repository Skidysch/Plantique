__all__ = (
    "router",
    "PlantRelationSchema",
    "CategoryRelationSchema",
    "CartRelationSchema",
    "UserRelationSchema",
)

from fastapi import APIRouter

from .relation_schemas import (
    CategoryRelationSchema,
    PlantRelationSchema,
    CartRelationSchema,
    UserRelationSchema
)

# from .db_migration.script import router as migration_router
from auth.views import router as auth_router
from .carts.views import router as carts_router
from .categories.views import router as categories_router
from .collections.views import router as collections_router
from .plants.views import router as plants_router
from .profiles.views import router as profiles_router
from .users.views import router as users_router
from payment.views import router as payment_router
from .orders.views import router as orders_router

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
