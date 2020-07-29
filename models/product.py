from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime

from db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String(50))
    # images = relationship('Image', back_populates='products')
    images = Column(String)


product = Product.__table__

