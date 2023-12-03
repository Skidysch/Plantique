from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas


# Users
def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User] | None:
    return db.query(models.User) \
             .offset(skip) \
             .limit(limit) \
             .all()


def get_user_by_id(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User) \
             .filter(models.User.id == user_id) \
             .first()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User) \
             .filter(models.User.email == email) \
             .first()


def get_user_by_username(db: Session, username: str) -> models.User | None:
    return db.query(models.User) \
             .filter(models.User.username == username) \
             .first()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username,
                          full_name=user.full_name,
                          email=user.email,
                          hashed_password=fake_hashed_password,
                          birth_date=user.birth_date,
                          gender=user.gender.capitalize(),
                          profile_picture=user.profile_picture,
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, updated_user: schemas.UserUpdate) -> models.User | None:
    db_user = get_user_by_id(db, user_id)

    if db_user:
        for key, value in updated_user.model_dump().items():
            if value is not None:
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user

    return None


def delete_user(db: Session, user_id: int) -> models.User | None:
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user

    return None


# Plants
def get_plants(db: Session, skip: int = 0, limit: int = 100) -> list[models.Plant] | None:
    return db.query(models.Plant) \
            .offset(skip) \
            .limit(limit) \
            .all()


def get_plant_by_id(db: Session, plant_id: int) -> models.Plant | None:
    return db.query(models.Plant) \
           .filter(models.Plant.id == plant_id) \
           .first()


def get_plant_by_slug(db: Session, plant_slug: str) -> models.Plant | None:
    return db.query(models.Plant) \
           .filter(models.Plant.slug == plant_slug) \
           .first()


def create_plant(db: Session, plant: schemas.PlantCreate):
    db_categories = []
    for id in plant.categories:
        db_category = db.query(models.Category) \
                    .filter(models.Category.id == id) \
                    .first()
        if db_category is None:
            raise HTTPException(status_code=404, detail=f'Category with id={id} does not exist')

        db_categories.append(db_category)

    db_plant = models.Plant(name=plant.name,
                            slug=plant.slug,
                            link=plant.link,
                            description=plant.description,
                            soil_type=plant.soil_type,
                            image_url=plant.image_url,
                            price=plant.price,
                            stock_available=plant.stock_available,
                            stock_quantity=plant.stock_quantity,
                            categories=db_categories
                            )
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant


def update_plant(db: Session, plant_id: int, updated_plant: schemas.PlantUpdate) -> models.Plant | None:
    db_plant = get_plant_by_id(db, plant_id)

    if db_plant:
        new_plant = updated_plant.model_dump()
        new_categories = new_plant.pop('categories')
        for key, value in new_plant.items():
            if value is not None:
                setattr(db_plant, key, value)
            if new_categories is not None:
                db_categories = []
                for id in new_categories:
                    db_category = db.query(models.Category) \
                               .filter(models.Category.id == id) \
                               .first()
                    if db_category is None:
                        raise HTTPException(status_code=404, detail=f'Category with id={id} does not exist')
                    db_categories.append(db_category)
                db_plant.categories = db_categories

        db.commit()
        db.refresh(db_plant)
        return db_plant

    return None


def delete_plant(db: Session, plant_id: int) -> models.Plant | None:
    db_plant = get_plant_by_id(db, plant_id)
    if db_plant:
        db.delete(db_plant)
        db.commit()
        return db_plant

    return None


# Category
def get_categories(db: Session, skip: int = 0, limit: int = 100) -> list[models.Category] | None:
    return db.query(models.Category) \
             .offset(skip) \
             .limit(limit) \
             .all()


def get_category_by_id(db: Session, category_id: int) -> models.Category | None:
    return db.query(models.Category) \
             .filter(models.Category.id == category_id) \
             .first()


def get_category_by_slug(db: Session, category_slug: str) -> models.Category | None:
    return db.query(models.Category) \
             .filter(models.Category.slug == category_slug) \
             .first()


def create_category(db: Session, category: schemas.CategoryCreate):
    print(type(category.collection_id))
    db_collection = db.query(models.Collection) \
                      .filter(models.Collection.id == category.collection_id) \
                      .first()

    if db_collection is None:
        raise HTTPException(status_code=404, detail="This collection does not exist")

    db_plants = []
    for id in category.plants:
        db_plant = db.query(models.Plant) \
                    .filter(models.Plant.id == id) \
                    .first()
        if db_plant is None:
            raise HTTPException(status_code=404, detail=f'Plant with id={id} does not exist')

        db_plants.append(db_plant)

    db_category = models.Category(name=category.name,
                                  slug=category.slug,
                                  link=category.link,
                                  description=category.description,
                                  image_url=category.image_url,
                                  collection_id=category.collection_id,
                                  collection=db_collection,
                                  plants=db_plants
                                  )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, updated_category: schemas.CategoryUpdate) -> models.Category | None:
    db_category = get_category_by_id(db, category_id)

    if db_category:
        new_category = updated_category.model_dump()
        new_collection = new_category.pop('collection_id')
        new_plants = new_category.pop('plants')

        for key, value in new_category.items():
            if value is not None:
                setattr(db_category, key, value)

            if new_collection is not None:
                db_collection = db.query(models.Collection) \
                              .filter(models.Collection.id == new_collection) \
                              .first()
                if db_collection is None:
                    raise HTTPException(status_code=404, detail=f'Collection with id={new_collection} does not exist')
                db_category.collection = db_collection

            if new_plants is not None:
                db_plants = []
                for id in new_plants:
                    db_plant = db.query(models.Plant) \
                               .filter(models.Plant.id == id) \
                               .first()
                    if db_plant is None:
                        raise HTTPException(status_code=404, detail=f'Plant with id={id} does not exist')
                    db_plants.append(db_plant)
                db_category.plants = db_plants

        db.commit()
        db.refresh(db_category)
        return db_category

    return None


def delete_category(db: Session, category_id: int) -> models.Category | None:
    db_category = get_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return db_category

    return None


# Collection
def get_collections(db: Session, skip: int = 0, limit: int = 100) -> list[models.Collection] | None:
    return db.query(models.Collection) \
            .offset(skip) \
            .limit(limit) \
            .all()


def get_collection_by_id(db: Session, collection_id: int) -> models.Collection | None:
    return db.query(models.Collection) \
           .filter(models.Collection.id == collection_id) \
           .first()


def get_collection_by_slug(db: Session, collection_slug: str) -> models.Collection | None:
    return db.query(models.Collection) \
           .filter(models.Collection.slug == collection_slug) \
           .first()


def create_collection(db: Session, collection: schemas.CollectionCreate):
    db_collection = models.Collection(name=collection.name,
                                      slug=collection.slug,
                                      link=collection.link,
                                      description=collection.description,
                                      categories=collection.categories
                                      )
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection


def update_collection(db: Session, collection_id: int, updated_collection: schemas.CollectionUpdate) -> models.Collection | None:
    db_collection = get_collection_by_id(db, collection_id)

    if db_collection:
        new_collection = updated_collection.model_dump()

        for key, value in new_collection.items():
            if value is not None:
                setattr(db_collection, key, value)

        db.commit()
        db.refresh(db_collection)
        return db_collection

    return None


def delete_collection(db: Session, collection_id: int) -> models.Collection | None:
    db_collection = get_collection_by_id(db, collection_id)
    if db_collection:
        db.delete(db_collection)
        db.commit()
        return db_collection

    return None
