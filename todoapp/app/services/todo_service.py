from app.repositories.todo_repository import TodoRepository
from app.models.item import TodoCreate, Todo, TodoUpdate

class TodoService:
    def __init__(self, repo : TodoRepository):
        self.repo = repo
    
    async def add_todo(self, todo_data: TodoCreate):
        return await self.repo.create(todo_data)
    
    async def get_all_todos(self) -> list[Todo]:
        return await self.repo.get_all()
    
    async def get_todo_by_id(self, todo_id: int) -> Todo | None:
        return await self.repo.get_by_id(todo_id)
    
    async def update_todo(self, todo_data: TodoUpdate) -> Todo:
        return await self.repo.update(todo_data)
    
    async def delete_todo(self, todo_id: int) -> bool:
        return await self.repo.delete(todo_id)
     