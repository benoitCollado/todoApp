from sqlmodel import select
from app.models.item import Todo, TodoCreate, TodoUpdate
from sqlalchemy.ext.asyncio import AsyncSession

class TodoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, todo_data: TodoCreate) -> Todo:
        try:
            db_todo = Todo.model_validate(todo_data)
            self.session.add(db_todo)
            await self.session.commit()
            await self.session.refresh(db_todo)
            return db_todo
        except Exception as e:
            raise ValueError(f"Error creating todo: {e}")
    
    async def get_all(self):
        try:
            result = await self.session.exec(select(Todo))
            return result.all()
        except Exception as e:
            raise ValueError(f"Error getting all todos: {e}")

    async def get_by_id(self, todo_id: int) -> Todo | None:
        try:
            result = await self.session.exec(select(Todo).where(Todo.id == todo_id))
            return result.first()
        except Exception as e:
            raise ValueError(f"Error getting todo by id: {e}")
    
    async def update(self, todo_data: TodoUpdate) -> Todo:
        try:
            todo = await self.get_by_id(todo_data.id)
            if not todo:
                raise ValueError("Todo not found")
            todo.title = todo_data.title
            todo.description = todo_data.description
            todo.completed = todo_data.completed
            await self.session.commit()
            await self.session.refresh(todo)    
            return todo
        except Exception as e:
            raise ValueError(f"Error updating todo: {e}")
    
    async def delete(self, todo_id: int) -> bool:
        try:
            todo = await self.get_by_id(todo_id)
            if not todo:
                raise ValueError("Todo not found")
            await self.session.delete(todo)
            await self.session.commit()
            return True
        except Exception as e:
            raise ValueError(f"Error deleting todo: {e}")