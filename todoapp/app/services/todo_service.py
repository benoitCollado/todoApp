from app.repositories.todo_repository import TodoRepository
from app.models.item import TodoCreate

class TodoService:
    def __init__(self, repo : TodoRepository):
        self.repo = repo
    
    async def add_todo(self, todo_data: TodoCreate):
        return await self.repo.create(todo_data)
     