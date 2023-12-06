import os

from dotenv import load_dotenv
import fastapi.security as security
import jwt
from sqlalchemy.orm import Session

from db import database, models, schemas, crud

load_dotenv()

oauth2schema = security.OAuth2PasswordBearer(tokenUrl='/token')
JWT_SECRET = os.getenv('JWT_SECRET')


def create_database():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_token(user: models.User):
    user_obj = schemas.User.model_validate(user)
    if user_obj.birth_date is not None:
        user_obj.birth_date = user_obj.birth_date.isoformat()

    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def authenticate_user(email: str, password: str, db: Session) -> models.User | None:
    user = await crud.get_user_by_email(db=db, email=email)

    if user is None or not user.verify_password(password):
        return None

    return user
