from fastapi import APIRouter, Depends
from app.database.database import get_session
from app.repositories.todo_repository import TodoRepository
from app.services.todo_service import TodoService
from app.models.item import Todo, TodoCreate

router = APIRouter()

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate, session=Depends(get_session)):
    repo = TodoRepository(session)
    service = TodoService(repo)
    return await service.add_todo(todo)