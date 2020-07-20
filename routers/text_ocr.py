from fastapi import APIRouter, UploadFile, File
from crud.text_ocr import create_upload_file
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("/uploadfile/")
async def file_upload(file: UploadFile = File(...)):
    response = await create_upload_file(file)
    return response


# @router.get("/file/")
# async def file_get():
#     return HTMLResponse(html)

@router.get("/file/")
async def file_receive():
    content = """
<body>
<form action = "http://localhost:8000/image/uploadfile/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
