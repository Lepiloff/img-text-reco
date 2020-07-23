from pydantic import BaseModel, HttpUrl
from typing import Optional, List


class ProductImage(BaseModel):
    url: HttpUrl
    name: str


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    images: Optional[List[ProductImage]] = None
