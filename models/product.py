from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime

from db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String(50))

    images = relationship('Image', back_populates='products')


product = Product.__tablename__


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates='images')


image = Image.__table__
