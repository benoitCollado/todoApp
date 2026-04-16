from sqlmodel import select
from app.models.item import Todo, TodoCreate

class TodoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create(self, todo_data: TodoCreate) -> Todo:
        db_todo = Todo.model_validate(todo_data)
        self.session.add(db_todo)
        await self.session.commit()
        await self.session.refresh(db_todo)
        return db_todo
    
    async def get_all(self):
        result = await self.session.exec(select(Todo))
        return result.all()