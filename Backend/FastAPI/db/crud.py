import fastapi
import jwt
import passlib.hash as hash
from sqlalchemy.orm import Session

from . import models, schemas
from services import get_db, oauth2schema, JWT_SECRET

# TODO: consider changing crud to interface


# Users
async def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User] | None:
    return db.query(models.User) \
             .offset(skip) \
             .limit(limit) \
             .all()


async def get_current_user(db: Session = fastapi.Depends(get_db), token: str = fastapi.Depends(oauth2schema)) -> schemas.User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = db.query(models.User).get(payload['id'])
    except:
        raise fastapi.HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )

    return schemas.User.model_validate(user)


async def get_user_by_id(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User) \
             .filter(models.User.id == user_id) \
             .first()


async def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User) \
             .filter(models.User.email == email) \
             .first()


async def get_user_by_username(db: Session, username: str) -> models.User | None:
    return db.query(models.User) \
             .filter(models.User.username == username) \
             .first()


async def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    password = user.model_dump().pop('password')
    del user.password
    hashed_password = hash.bcrypt.hash(password)

    db_user = models.User(**user.model_dump(), hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def update_user(db: Session, user_id: int, updated_user: schemas.UserUpdate) -> models.User | None:
    db_user = await get_user_by_id(db, user_id)

    if db_user:
        for key, value in updated_user.model_dump().items():
            if value is not None:
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user

    return None


async def delete_user(db: Session, user_id: int) -> models.User | None:
    db_user = await get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user

    return None


# Plants
async def get_plants(db: Session, skip: int = 0, limit: int = 100) -> list[models.Plant] | None:
    return db.query(models.Plant) \
            .offset(skip) \
            .limit(limit) \
            .all()


async def get_plant_by_id(db: Session, plant_id: int) -> models.Plant | None:
    return db.query(models.Plant) \
           .filter(models.Plant.id == plant_id) \
           .first()


async def get_plant_by_slug(db: Session, plant_slug: str) -> models.Plant | None:
    return db.query(models.Plant) \
           .filter(models.Plant.slug == plant_slug) \
           .first()


async def create_plant(db: Session, plant: schemas.PlantCreate):
    category_ids = plant.categories
    del plant.categories

    db_plant = models.Plant(**plant.model_dump())
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)

    if category_ids:
        categories = db.query(models.Category).filter(models.Category.id.in_(category_ids)).all()
        db_plant.categories.extend(categories)
        db.commit()
        db.refresh(db_plant)

    return db_plant


async def update_plant(db: Session, plant_id: int, updated_plant: schemas.PlantUpdate) -> models.Plant | None:
    db_plant = await get_plant_by_id(db, plant_id)

    if db_plant:
        category_ids = db_plant.category
        del db_plant.category
        if category_ids is not None:
            categories = db.query(models.Category).filter(models.Category.id.in_(category_ids)).all()
            setattr(db_plant, 'categories', categories)

        for key, value in updated_plant.model_dump().items():
            if value is not None:
                setattr(db_plant, key, value)

        db.commit()
        db.refresh(db_plant)
        return db_plant

    return None


async def delete_plant(db: Session, plant_id: int) -> models.Plant | None:
    db_plant = await get_plant_by_id(db, plant_id)
    if db_plant:
        db.delete(db_plant)
        db.commit()
        return db_plant

    return None


# Category
async def get_categories(db: Session, skip: int = 0, limit: int = 100) -> list[models.Category] | None:
    return db.query(models.Category) \
             .offset(skip) \
             .limit(limit) \
             .all()


async def get_category_by_id(db: Session, category_id: int) -> models.Category | None:
    return db.query(models.Category) \
             .filter(models.Category.id == category_id) \
             .first()


async def get_category_by_slug(db: Session, category_slug: str) -> models.Category | None:
    return db.query(models.Category) \
             .filter(models.Category.slug == category_slug) \
             .first()


async def create_category(db: Session, category: schemas.CategoryCreate):
    plant_ids = category.plants
    del category.plants

    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    if plant_ids:
        plants = db.query(models.Plant).filter(models.Plant.id.in_(plant_ids)).all()
        db_category.plants.extend(plants)
        db.commit()
        db.refresh(db_category)

    return db_category


async def update_category(db: Session, category_id: int, updated_category: schemas.CategoryUpdate) -> models.Category | None:
    db_category = await get_category_by_id(db, category_id)

    if db_category:
        plant_ids = updated_category.plants
        del updated_category.plants
        if plant_ids is not None:
            plants = db.query(models.Plant).filter(models.Plant.id.in_(plant_ids)).all()
            setattr(db_category, 'plants', plants)

        for key, value in updated_category.model_dump().items():
            if value is not None:
                setattr(db_category, key, value)

        db.commit()
        db.refresh(db_category)
        return db_category

    return None


async def delete_category(db: Session, category_id: int) -> models.Category | None:
    db_category = await get_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return db_category

    return None


# Collection
async def get_collections(db: Session, skip: int = 0, limit: int = 100) -> list[models.Collection] | None:
    return db.query(models.Collection) \
            .offset(skip) \
            .limit(limit) \
            .all()


async def get_collection_by_id(db: Session, collection_id: int) -> models.Collection | None:
    return db.query(models.Collection) \
           .filter(models.Collection.id == collection_id) \
           .first()


async def get_collection_by_slug(db: Session, collection_slug: str) -> models.Collection | None:
    return db.query(models.Collection) \
           .filter(models.Collection.slug == collection_slug) \
           .first()


async def create_collection(db: Session, collection: schemas.CollectionCreate):
    db_collection = models.Collection(**collection.model_dump())
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)

    return db_collection


async def update_collection(db: Session, collection_id: int, updated_collection: schemas.CollectionUpdate) -> models.Collection | None:
    db_collection = await get_collection_by_id(db, collection_id)

    if db_collection:
        for key, value in updated_collection.model_dump().items():
            if value is not None:
                setattr(db_collection, key, value)

        db.commit()
        db.refresh(db_collection)

        return db_collection

    return None


async def delete_collection(db: Session, collection_id: int) -> models.Collection | None:
    db_collection = await get_collection_by_id(db, collection_id)
    if db_collection:
        db.delete(db_collection)
        db.commit()
        return db_collection

    return None
