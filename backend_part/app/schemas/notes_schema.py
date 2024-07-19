# from pydantic import BaseModel,Field
# from uuid import UUID
# from datetime import datetime
# from typing import Optional
# class NoteCreate(BaseModel):
#   title:str = Field(...,title='Title of the note',max_length=50,min_length=1)
#   description:str = Field(...,title='Title of the note',max_length=5000,min_length=1)
#   status:Optional[bool] = False
  
# class NoteUpdate(BaseModel):
#   title:Optional[str] = Field(...,title='Title of the note',max_length=50,min_length=1)
#   description:Optional[str] = Field(...,title='Title of the note',max_length=5000,min_length=1)
#   status:Optional[bool] = False


# class NoteOut(BaseModel):
#   note_id:UUID
#   status:bool
#   title:str
#   description:str
#   created_at:datetime
#   updated_at:datetime

from pydantic import BaseModel,Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class NoteCreate(BaseModel):
  title:str = Field(...,title='Title of the note',max_length=50,min_length=1)
  description:str = Field(...,title='Title of the note',max_length=5000,min_length=1)
  status:Optional[bool] = False

class NoteUpdate(BaseModel):
  title:Optional[str] = Field(...,title='Title of the note',max_length=50,min_length=1)
  description:Optional[str] = Field(...,title='Title of the note',max_length=5000,min_length=1)
  status:Optional[bool] = False


class NoteOut(BaseModel):
  note_id:UUID
  status:bool
  title:str
  description:str
  created_at:datetime
  updated_at:datetime

  class Config:
      from_attributes = True  # Add this line
