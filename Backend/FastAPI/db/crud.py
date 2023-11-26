from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User) \
             .filter(models.User.id == user_id) \
             .first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User) \
             .filter(models.User.email == email) \
             .first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User) \
             .filter(models.User.username == username) \
             .first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User) \
             .offset(skip) \
             .limit(limit) \
             .all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username,
                          full_name=user.full_name,
                          email=user.email,
                          hashed_password=fake_hashed_password,
                          birth_date=user.birth_date,
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, updated_user: schemas.UserUpdate):
    db_user = get_user(db, user_id)

    if db_user:
        for key, value in updated_user.model_dump().items():
            if value is not None:
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user

    return None


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user

    return None
