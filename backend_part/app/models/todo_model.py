from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed , Link,before_event,Replace,Insert
from pydantic import Field, EmailStr
from .user_model import User

class Notes(Document):
  note_id:UUID=Field(default_factory=uuid4, unqiue=True)
  status:bool=False
  title:Indexed(str)
  description:str=None
  created_at:datetime=Field(default_factory=datetime.utcnow)
  updated_at:datetime=Field(default_factory=datetime.utcnow)
  owner:Link[User]
  
  def __repr__(self) -> str:
        return f"<Note {self.title}>"

  def __str__(self) -> str:
      return self.title

  def __hash__(self) -> int:
      return hash(self.title)

  def __eq__(self, other: object) -> bool:
      if isinstance(other, Notes):
          return self.todo_id == other.todo_id
      return False
  @before_event([Replace,Insert])
  
  def update_update_at(self):
    self.updated_at=datetime.utcnow()
      
  class Setting:
    name:"Note_taking_app"
  
  