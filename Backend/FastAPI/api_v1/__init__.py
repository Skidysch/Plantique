from fastapi import APIRouter

from auth.views import router as auth_router
from .categories.views import router as categories_router
from .collections.views import router as collections_router
from .plants.views import router as plants_router
from .users.views import router as users_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(collections_router)
router.include_router(categories_router)
router.include_router(plants_router)
