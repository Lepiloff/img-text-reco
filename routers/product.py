import os
import uuid

import aiofiles

from schemas.products_schema import ProductSchema
from models.product import product
from fastapi import APIRouter, UploadFile, File, HTTPException, Form

router = APIRouter()


@router.post('/add_product/', response_model=ProductSchema, status_code=201)
# async def create_product(payload: ProductSchema, file: UploadFile = File(...)):
async def create_product(file: UploadFile = File(...), payload: ProductSchema = Form(...)):
    _, ext = os.path.splitext(file.filename)
    print(ext)
    content = await file.read()
    if file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(status_code=406, detail="Only .jpeg or .png  files allowed")
    file_name = f'{uuid.uuid4().hex}{ext}'
    async with aiofiles.open(os.path.join('/static/product_images', file_name), "wb") as f:
        await f.write(content)
    path_to_img = os.path.abspath(file_name)
    query = product.insert().values(name=payload.name, description=payload.description, image=path_to_img)


    response_object = {
        # "id": product_id,
        # "title": payload.name,
        # "description": payload.description,
    }
    return response_object