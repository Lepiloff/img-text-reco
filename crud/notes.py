from db import database
from models.notes import notes
from schemas.notes import NoteSchema


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)