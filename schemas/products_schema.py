from pydantic import BaseModel, HttpUrl
from typing import Optional


class ProductSchema(BaseModel):
    name: str
    description: Optional[str] = None
    images: Optional[str] = None
