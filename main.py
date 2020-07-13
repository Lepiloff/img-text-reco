from fastapi import FastAPI
from routers import notes, text_ocr
from db import database, engine, metadata


#Create the tables, not for production
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(notes.router, prefix='/notes', tags=['notes'])
app.include_router(text_ocr.router, prefix='/image')

# def detect_text(path):
#     """Detects text in the file."""
#     client = vision.ImageAnnotatorClient()
#
#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()
#
#     image = vision.types.Image(content=content)
#
#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     label_dicts = []
#     for text in texts:
#         # Write each label (EntityAnnotation) into a dictionary
#         dict = {'description': text.description}
#         # Populate the array
#         label_dicts.append(dict)
#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))
#     return label_dicts
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     _, ext = os.path.splitext(file.filename)
#     content = await file.read()
#     if file.content_type not in ['image/jpeg', 'image/png']:
#         raise HTTPException(status_code=406, detail="Only .jpeg or .png  files allowed")
#     file_name = f'{uuid.uuid4().hex}{ext}'
#     async with aiofiles.open(file_name, "wb") as f:
#         await f.write(content)
#     path_to_img = os.path.abspath(file_name)
#     try:
#         response = detect_text(path_to_img)
#     finally:
#         await aiofiles.os.remove(path_to_img)
#     return {"file_info": response}
