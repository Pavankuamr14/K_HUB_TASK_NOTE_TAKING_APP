from fastapi import APIRouter
from typing import List
from uuid import UUID   
from app.schemas.notes_schema import NoteOut,NoteCreate,NoteUpdate
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from fastapi import Depends
from app.models.todo_model import Notes
from app.services.note_service import Noteservice

todo_router = APIRouter()

@todo_router.get('/',summary="Get all notes of user",response_model=list[NoteOut])

async def list(current_user:User=Depends(get_current_user)):
  # retrun await 
  return await Noteservice.list_notes(current_user)

@todo_router.post('/create',summary="Create Notes",response_model=Notes)

async def create_note(data:NoteCreate,current_user:User=Depends(get_current_user)):
  return await Noteservice.create_note(current_user,data)


@todo_router.get('/{note_id}',summary="Get a note by note_id",response_model=NoteOut)


async def retrieve(note_id:UUID,current_user:User=Depends(get_current_user)):
  return await Noteservice.retrieve_note (current_user,note_id)

@todo_router.put('/{note_id}',summary="Update a note by note_id",response_model=NoteOut)

async def update(note_id:UUID,data:NoteUpdate,current_user:User=Depends(get_current_user)):
  return await Noteservice.update_note(current_user,note_id,data)


@todo_router.delete('/{note_id}',summary="Delete a note by note_id")

async def delete(note_id:UUID,current_user:User=Depends(get_current_user)):
  await Noteservice.delete_note(current_user,note_id)
  return None
