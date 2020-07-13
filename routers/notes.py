from schemas.notes import NoteDB, NoteSchema
from crud import notes

from fastapi import APIRouter

router = APIRouter()


@router.post('/create_note/', response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await notes.post(payload)
    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object