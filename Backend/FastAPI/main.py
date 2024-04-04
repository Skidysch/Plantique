from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_v1 import router as router_v1
from core.settings import settings
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Here comes actions that could be used
    # during app initialization.

    yield
    # Here would come actions after app is done its work,
    # e.g. here we can close database and release resources.


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(router_v1, prefix=settings.api_v1_prefix)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)


# Token
@app.post("/token")
async def generate_token(
    form_data: security.OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(services.get_db),
):
    user = await services.authenticate_user(
        email=form_data.username, password=form_data.password, db=db
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return await services.create_token(user)


# Users
@app.get("/users", response_model=list[schemas.User])
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(services.get_db)
):
    users = await crud.get_users(db, skip=skip, limit=limit)

    if not users:
        raise HTTPException(
            status_code=404, detail="No users exist yet, you can be the first one"
        )

    return users


@app.get("/users/current", response_model=schemas.User)
async def get_current_user(user: schemas.User = Depends(crud.get_current_user)):
    return user


@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(services.get_db)):
    db_user = await crud.get_user_by_id(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@app.post("/users")
async def create_user(user: schemas.UserCreate, db: Session = Depends(services.get_db)):
    allowed_genders = {"Male", "Female"}

    if await crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if await crud.get_user_by_username(db, username=user.username):
        raise HTTPException(
            status_code=400,
            detail="Username has been taken, please, create another one",
        )

    if user.gender.capitalize() not in allowed_genders:
        raise HTTPException(status_code=400, detail="Invalid gender")

    user = await crud.create_user(db=db, user=user)

    return await services.create_token(user=user)


@app.patch("/users/{user_id}", response_model=schemas.User)
async def edit_user(
    user_id: int,
    updated_user: schemas.UserUpdate,
    db: Session = Depends(services.get_db),
):
    db_user = await crud.get_user_by_id(db, user_id=user_id)
    allowed_genders = {"Male", "Female"}

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if updated_user.email and await crud.get_user_by_email(
        db, email=updated_user.email
    ):
        raise HTTPException(
            status_code=400, detail="User with this email already exists"
        )
    if updated_user.username and await crud.get_user_by_username(
        db, username=updated_user.username
    ):
        raise HTTPException(
            status_code=400,
            detail="Username has been already taken, please, create another one",
        )

    if updated_user.gender and updated_user.gender.capitalize() not in allowed_genders:
        raise HTTPException(status_code=400, detail="Invalid gender")

    return await crud.update_user(db=db, user_id=user_id, updated_user=updated_user)


@app.delete("/users/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(services.get_db)):
    db_user = await crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.delete_user(db=db, user_id=user_id)


# Plants
@app.get("/plants", response_model=list[schemas.Plant])
async def read_plants(
    skip: int = 0, limit: int = 100, db: Session = Depends(services.get_db)
):
    plants = await crud.get_plants(db, skip=skip, limit=limit)

    if not plants:
        raise HTTPException(
            status_code=404, detail="No plants exist yet, come back in a while"
        )

    return plants


@app.get("/plants/{plant_id}", response_model=schemas.Plant)
async def read_plant(plant_id: str, db: Session = Depends(services.get_db)):
    if plant_id.isdigit():
        plant = await crud.get_plant_by_id(db, int(plant_id))
    else:
        plant = await crud.get_plant_by_slug(db, plant_id)

    if plant is None:
        raise HTTPException(status_code=400, detail="Plant not found")

    return plant


@app.get("/plants/filter/{category_id}", response_model=list[schemas.Plant])
async def filter_plants_by_category(category_id: int, db: Session = Depends(services.get_db)):
    plants = await crud.filter_plants_by_category(db, category_id=category_id)

    if plants is None:
        raise HTTPException(status_code=400, detail="No plants in this category")

    return plants


@app.post("/plants", response_model=schemas.Plant)
async def create_plant(
    plant: schemas.PlantCreate, db: Session = Depends(services.get_db)
):
    if await crud.get_plant_by_slug(db, plant_slug=plant.slug):
        raise HTTPException(
            status_code=400, detail="Plant with this slug already exists"
        )

    return await crud.create_plant(db=db, plant=plant)


@app.patch("/plants/{plant_id}", response_model=schemas.Plant)
async def edit_plant(
    plant_id: int,
    updated_plant: schemas.PlantUpdate,
    db: Session = Depends(services.get_db),
):
    db_plant = await crud.get_plant_by_id(db, plant_id=plant_id)

    if db_plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")
    if updated_plant.slug and await crud.get_plant_by_slug(
        db, plant_slug=updated_plant.slug
    ):
        raise HTTPException(
            status_code=400, detail="Plant with this slug already exists"
        )

    return await crud.update_plant(
        db=db, plant_id=plant_id, updated_plant=updated_plant
    )


@app.delete("/plants/{plant_id}", response_model=schemas.Plant)
async def delete_plant(plant_id: int, db: Session = Depends(services.get_db)):
    db_plant = await crud.get_plant_by_id(db, plant_id=plant_id)
    if db_plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")
    return await crud.delete_plant(db=db, plant_id=plant_id)


# Categories
@app.get("/categories", response_model=list[schemas.Category])
async def read_categories(
    skip: int = 0, limit: int = 100, db: Session = Depends(services.get_db)
):
    categories = await crud.get_categories(db, skip=skip, limit=limit)

    if not categories:
        raise HTTPException(
            status_code=404, detail="No categories exist yet, come back in a while"
        )

    return categories


@app.get("/categories/{category_id}", response_model=schemas.Category)
async def read_category(category_id: str, db: Session = Depends(services.get_db)):
    if category_id.isdigit():
        category = await crud.get_category_by_id(db, int(category_id))
    else:
        category = await crud.get_category_by_slug(db, category_id)

    if category is None:
        raise HTTPException(status_code=400, detail="Plant not found")

    return category


@app.get("/categories/filter/{collection_id}", response_model=list[schemas.Category])
async def filter_categories_by_collection(collection_id: int, db: Session = Depends(services.get_db)):
    categories = await crud.filter_categories_by_collection(db, collection_id=collection_id)

    if categories is None:
        raise HTTPException(status_code=400, detail="No categories in this collection")

    return categories


@app.post("/categories", response_model=schemas.Category)
async def create_category(
    category: schemas.CategoryCreate, db: Session = Depends(services.get_db)
):
    if await crud.get_category_by_slug(db, category_slug=category.slug):
        raise HTTPException(
            status_code=400, detail="Category with this slug already exists"
        )

    return await crud.create_category(db=db, category=category)


@app.patch("/categories/{category_id}", response_model=schemas.Category)
async def edit_category(
    category_id: int,
    updated_category: schemas.CategoryUpdate,
    db: Session = Depends(services.get_db),
):
    db_category = await crud.get_category_by_id(db, category_id=category_id)

    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    if updated_category.slug and await crud.get_category_by_slug(
        db, category_slug=updated_category.slug
    ):
        raise HTTPException(
            status_code=400, detail="Category with this slug already exists"
        )

    return await crud.update_category(
        db=db, category_id=category_id, updated_category=updated_category
    )


@app.delete("/categories/{category_id}", response_model=schemas.Category)
async def delete_category(category_id: int, db: Session = Depends(services.get_db)):
    db_category = await crud.get_category_by_id(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return await crud.delete_category(db=db, category_id=category_id)


# Collections
@app.get("/collections", response_model=list[schemas.Collection])
async def read_collections(
    skip: int = 0, limit: int = 100, db: Session = Depends(services.get_db)
):
    collections = await crud.get_collections(db, skip=skip, limit=limit)

    if not collections:
        raise HTTPException(
            status_code=404, detail="No collections exist yet, come back in a while"
        )

    return collections


@app.get("/collections/{collection_id}", response_model=schemas.Collection)
async def read_collection(collection_id: int, db: Session = Depends(services.get_db)):
    collection = await crud.get_collection_by_id(db, collection_id)

    if collection is None:
        raise HTTPException(status_code=400, detail="Collection not found")

    return collection


@app.post("/collections", response_model=schemas.Collection)
async def create_collection(
    collection: schemas.CollectionCreate, db: Session = Depends(services.get_db)
):
    if await crud.get_collection_by_slug(db, collection_slug=collection.slug):
        raise HTTPException(
            status_code=400, detail="Collection with this slug already exists"
        )

    return await crud.create_collection(db=db, collection=collection)


@app.patch("/collections/{collection_id}", response_model=schemas.Collection)
async def edit_collection(
    collection_id: int,
    updated_collection: schemas.CollectionUpdate,
    db: Session = Depends(services.get_db),
):
    db_collection = await crud.get_collection_by_id(db, collection_id=collection_id)

    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    if updated_collection.slug and await crud.get_collection_by_slug(
        db, collection_slug=updated_collection.slug
    ):
        raise HTTPException(
            status_code=400, detail="Collection with this slug already exists"
        )

    return await crud.update_collection(
        db=db, collection_id=collection_id, updated_collection=updated_collection
    )


@app.delete("/collections/{collection_id}", response_model=schemas.Collection)
async def delete_collection(collection_id: int, db: Session = Depends(services.get_db)):
    db_collection = await crud.get_collection_by_id(db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return await crud.delete_collection(db=db, collection_id=collection_id)
