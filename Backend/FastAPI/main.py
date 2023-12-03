from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)

    if not users:
        raise HTTPException(status_code=404, detail="No users exist yet, you can be the first one")

    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    allowed_genders = {'Male', 'Female'}

    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud.get_user_by_username(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username has been taken, please, create another one")

    if user.gender.capitalize() not in allowed_genders:
        raise HTTPException(status_code=400, detail="Invalid gender")

    return crud.create_user(db=db, user=user)


@app.patch("/users/{user_id}", response_model=schemas.User)
def edit_user(user_id: int, updated_user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    allowed_genders = {'Male', 'Female'}

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if updated_user.email and crud.get_user_by_email(db, email=updated_user.email):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    if updated_user.username and crud.get_user_by_username(db, username=updated_user.username):
        raise HTTPException(status_code=400, detail="Username has been already taken, please, create another one")

    if updated_user.gender and updated_user.gender.capitalize() not in allowed_genders:
        raise HTTPException(status_code=400, detail="Invalid gender")

    return crud.update_user(db=db, user_id=user_id, updated_user=updated_user)


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)


# Plants
@app.get("/plants/", response_model=list[schemas.Plant])
def read_plants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    plants = crud.get_plants(db, skip=skip, limit=limit)

    if not plants:
        raise HTTPException(status_code=404, detail="No plants exist yet, come back in a while")

    return plants


@app.get("/plants/{plant_id}", response_model=schemas.Plant)
def read_plant(plant_id: int, db: Session = Depends(get_db)):
    plant = crud.get_plant_by_id(db, plant_id)

    if plant is None:
        raise HTTPException(status_code=400, detail="Plant not found")

    return plant


@app.post("/plants/", response_model=schemas.Plant)
def create_plant(plant: schemas.PlantCreate, db: Session = Depends(get_db)):
    if crud.get_plant_by_slug(db, plant_slug=plant.slug):
        raise HTTPException(status_code=400, detail="Plant with this slug already exists")

    return crud.create_plant(db=db, plant=plant)


@app.patch("/plants/{plant_id}", response_model=schemas.Plant)
def edit_plant(plant_id: int, updated_plant: schemas.PlantUpdate, db: Session = Depends(get_db)):
    db_plant = crud.get_plant_by_id(db, plant_id=plant_id)

    if db_plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")
    if updated_plant.slug and crud.get_plant_by_slug(db, plant_slug=updated_plant.slug):
        raise HTTPException(status_code=400, detail="Plant with this slug already exists")

    return crud.update_plant(db=db, plant_id=plant_id, updated_plant=updated_plant)


@app.delete("/plants/{plant_id}", response_model=schemas.Plant)
def delete_plant(plant_id: int, db: Session = Depends(get_db)):
    db_plant = crud.get_plant_by_id(db, plant_id=plant_id)
    if db_plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")
    return crud.delete_plant(db=db, plant_id=plant_id)


# Categories
@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)

    if not categories:
        raise HTTPException(status_code=404, detail="No categories exist yet, come back in a while")

    return categories


@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, category_id)

    if category is None:
        raise HTTPException(status_code=400, detail="category not found")

    return category


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    if crud.get_category_by_slug(db, category_slug=category.slug):
        raise HTTPException(status_code=400, detail="Category with this slug already exists")

    return crud.create_category(db=db, category=category)


@app.patch("/categories/{category_id}", response_model=schemas.Category)
def edit_category(category_id: int, updated_category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_id(db, category_id=category_id)

    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    if updated_category.slug and crud.get_category_by_slug(db, category_slug=updated_category.slug):
        raise HTTPException(status_code=400, detail="Category with this slug already exists")

    return crud.update_category(db=db, category_id=category_id, updated_category=updated_category)


@app.delete("/categories/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_id(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.delete_category(db=db, category_id=category_id)


# Collections
@app.get("/collections/", response_model=list[schemas.Collection])
def read_collections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    collections = crud.get_collections(db, skip=skip, limit=limit)

    if not collections:
        raise HTTPException(status_code=404, detail="No collections exist yet, come back in a while")

    return collections


@app.get("/collections/{collection_id}", response_model=schemas.Collection)
def read_collection(collection_id: int, db: Session = Depends(get_db)):
    collection = crud.get_collection_by_id(db, collection_id)

    if collection is None:
        raise HTTPException(status_code=400, detail="Collection not found")

    return collection


@app.post("/collections/", response_model=schemas.Collection)
def create_collection(collection: schemas.CollectionCreate, db: Session = Depends(get_db)):
    if crud.get_collection_by_slug(db, collection_slug=collection.slug):
        raise HTTPException(status_code=400, detail="Collection with this slug already exists")

    return crud.create_collection(db=db, collection=collection)


@app.patch("/collections/{collection_id}", response_model=schemas.Collection)
def edit_collection(collection_id: int, updated_collection: schemas.CollectionUpdate, db: Session = Depends(get_db)):
    db_collection = crud.get_collection_by_id(db, collection_id=collection_id)

    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    if updated_collection.slug and crud.get_collection_by_slug(db, collection_slug=updated_collection.slug):
        raise HTTPException(status_code=400, detail="Collection with this slug already exists")

    return crud.update_collection(db=db, collection_id=collection_id, updated_collection=updated_collection)


@app.delete("/collections/{collection_id}", response_model=schemas.Collection)
def delete_collection(collection_id: int, db: Session = Depends(get_db)):
    db_collection = crud.get_collection_by_id(db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return crud.delete_collection(db=db, collection_id=collection_id)
