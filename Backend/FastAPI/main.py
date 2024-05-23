from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from FastAPI.api_v1 import router as router_v1
from FastAPI.core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Here comes actions that could be used
    # during app initialization.

    yield
    # Here would come actions after app is done its work,
    # e.g. here we can close database and release resources.


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)
