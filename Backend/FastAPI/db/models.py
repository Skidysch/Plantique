from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Enum, ForeignKey, \
                       Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

plant_category_association = Table(
    'plant_category_association',
    Base.metadata,
    Column('plant_id', Integer, ForeignKey('plants.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    birth_date = Column(Date)
    role = Column(Enum('Admin', 'User', name='user_roles'))
    is_active = Column(Boolean, default=True)


class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    soil_type = Column(String)
    image_url = Column(String)
    price = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
    categories = relationship('Category',
                              secondary=plant_category_association,
                              back_populates='plants'
                              )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
    plants = relationship('Plant',
                          secondary=plant_category_association,
                          back_populates='categories'
                          )
