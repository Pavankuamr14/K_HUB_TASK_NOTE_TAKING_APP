from app.models.user_model import User
from app.models.todo_model import Notes
from uuid import UUID
from typing import List
from app.schemas.notes_schema import NoteCreate,NoteUpdate,NoteOut




class Noteservice:
  
  @staticmethod
  async def list_notes(user:User)-> List[NoteOut]:
    notes=await Notes.find(Notes.owner.id==user.id).to_list() 
    return [NoteOut.from_orm(note) for note in notes]  # Convert Notes to NoteOut
    # return Note
  @staticmethod
  async def create_note(user:User,data:NoteCreate) -> Notes:
    note=Notes(**data.dict(),owner=user)
    return await note.insert()
  # @staticmethod
  # async def retrieve_note(current_user:User,note_id:UUID):
  #   note=await Notes.find_one(Notes.note_id==note_id,Notes.owner.id==current_user.user_id)
  #   if note:
  #     return NoteOut.from_orm(note)  # Convert Notes to NoteOut
  #   return None


  @staticmethod
  async def retrieve_note(current_user:User,note_id:UUID):
    note=await Notes.find_one(Notes.note_id==note_id,Notes.owner.id==current_user.id)
    
    return note
  @staticmethod
  async def update_note(current_user:User,note_id:UUID,data:NoteUpdate):
    note = await Noteservice.retrieve_note(current_user,note_id)
    await note.update({"$set":data.dict(exclude_unset=True)})
    await note.save()
    return note
  
  @staticmethod
  async def delete_note(current_user:User,note_id:UUID):
    note = await Noteservice.retrieve_note(current_user,note_id)
    if note:
      await note.delete()
    return None
  