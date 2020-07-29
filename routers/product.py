import os
import uuid
from typing import List

import aiofiles
from fastapi import APIRouter, UploadFile, File, HTTPException, Form

from models.product import product
from schemas.products_schema import ProductSchema
from db import database, BASEDIR


router = APIRouter()


@router.post('/add_product/', status_code=201)
async def create_product(file: UploadFile = File(...),
                         name: str = Form(...),
                         description: str = Form(...)):

    _, ext = os.path.splitext(file.filename)
    IMG_DIR = os.path.join(BASEDIR, 'static/product_images')
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)
    print(f'IMG_DIR {IMG_DIR}')
    content = await file.read()
    if file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(status_code=406, detail="Only .jpeg or .png  files allowed")
    file_name = f'{uuid.uuid4().hex}{ext}'
    print(os.path.join(IMG_DIR, file_name))
    async with aiofiles.open(os.path.join(IMG_DIR, file_name), mode='wb') as f:
        await f.write(content)
    path_to_img = os.path.abspath(os.path.join(IMG_DIR, file_name))
    query = product.insert().values(name=name, description=description, images=path_to_img)
    item = await database.execute(query)

    response_object = {
        "id": item,
        "name": name,
        "description": description,
        "img": path_to_img
    }
    return response_object


@router.get("/products/", response_model=List[ProductSchema])
async def read_notes():
    query = product.select()
    return await database.fetch_all(query)
