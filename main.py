from fastapi import FastAPI
from routers import notes, text_ocr
from db import database, engine, metadata


#Create the tables, not for production
# metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(notes.router, prefix='/notes', tags=['notes'])
app.include_router(text_ocr.router, prefix='/image')

