from fastapi import HTTPException, APIRouter, UploadFile, File
from crud.text_ocr import create_upload_file
router = APIRouter()


@router.post("/uploadfile/")
async def file_upload(file: UploadFile = File(...)):
    response = await create_upload_file(file)
    return response
