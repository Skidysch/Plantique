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


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud.get_user_by_username(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username has been taken, please, create another one")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    if not users:
        raise HTTPException(status_code=404, detail="No users exist yet, you can be the first one")
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.patch("/users/{user_id}", response_model=schemas.User)
def edit_user(user_id: int, updated_user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if updated_user.email and crud.get_user_by_email(db, email=updated_user.email):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    if updated_user.username and crud.get_user_by_username(db, username=updated_user.username):
        raise HTTPException(status_code=400, detail="Username has been already taken, please, create another one")
    return crud.update_user(db=db, user_id=user_id, updated_user=updated_user)


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)
