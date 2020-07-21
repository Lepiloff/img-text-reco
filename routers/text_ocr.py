from fastapi import APIRouter, UploadFile, File, Request
from crud.text_ocr import create_upload_file
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')

router = APIRouter()


@router.post("/uploadfile/")
async def file_upload(request: Request, file: UploadFile = File(...)):
    response = await create_upload_file(file)
    # return response
    response = response.get('file_info')
    return templates.TemplateResponse("ocr_result.html", {"request": request, "result": response[0].get('description')})

# @router.get("/file/")
# async def file_get():
#     return HTMLResponse(html)

@router.get("/file/")
async def file_receive():
    content = """
<body>
<form action = "http://./image/uploadfile/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
