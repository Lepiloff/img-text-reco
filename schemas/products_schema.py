from pydantic import BaseModel, HttpUrl
from typing import Optional, List


class ProductImageSchema(BaseModel):
    url: HttpUrl
    name: str


class ProductSchema(BaseModel):
    name: str
    description: Optional[str] = None
    images: Optional[List[ProductImageSchema]] = None
