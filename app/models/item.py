from sqlmodel import SQLModel, Field
from typing import Optional

class TodoBase(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    is_completed: bool = False
    
class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
class TodoCreate(TodoBase):
    pass