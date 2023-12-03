from sqlalchemy import Boolean, Column, Date, DateTime, Enum, ForeignKey, \
                       Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

plant_category_association = Table(
    'plant_category_association',
    Base.metadata,
    Column('plant_id', Integer, ForeignKey('plants.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

cart_plant_association = Table(
    'cart_plant_association',
    Base.metadata,
    Column('cart_id', Integer, ForeignKey('carts.id')),
    Column('plant_id', Integer, ForeignKey('plants.id'))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    gender = Column(Enum('Male', 'Female', name='user_gender'))
    profile_picture = Column(String, nullable=True)
    role = Column(Enum('Admin', 'User', name='user_roles'), default='User')
    birth_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=func.now())
    is_active = Column(Boolean, default=True)
    cart = relationship('Cart', uselist=False, back_populates='user')
    orders = relationship('Order', back_populates='user')


class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    link = Column(String, index=True)
    description = Column(String, index=True)
    soil_type = Column(String)
    image_url = Column(String)
    price = Column(Integer)
    stock_available = Column(Boolean)
    stock_quantity = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    categories = relationship('Category',
                              secondary=plant_category_association,
                              back_populates='plants'
                              )
    carts = relationship('Cart',
                         secondary=cart_plant_association,
                         back_populates='plants'
                         )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    link = Column(String, index=True)
    description = Column(String, index=True)
    image_url = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    collection_id = Column(Integer, ForeignKey('collections.id'))
    collection = relationship('Collection', back_populates='categories')
    plants = relationship('Plant',
                          secondary=plant_category_association,
                          back_populates='categories'
                          )


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    link = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    categories = relationship('Category', back_populates='collection')


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship('User', back_populates='cart')
    plants = relationship('Plant',
                          secondary=cart_plant_association,
                          back_populates='carts')


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')
