from fastapi import APIRouter, Depends
from app.database.database import get_session
from app.repositories.todo_repository import TodoRepository
from app.services.todo_service import TodoService
from app.models.item import Todo, TodoCreate, TodoUpdate

router = APIRouter()

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate, session=Depends(get_session)):
    repo = TodoRepository(session)
    service = TodoService(repo)
    return await service.add_todo(todo)

@router.get("/", response_model=list[Todo])
async def get_all_todos(session=Depends(get_session)):
    repo = TodoRepository(session)
    service = TodoService(repo)
    return await service.get_all_todos()

@router.get("/{todo_id}", response_model=Todo)
async def get_todo_by_id(todo_id: int, session=Depends(get_session)):
    repo = TodoRepository(session)
    service = TodoService(repo)
    return await service.get_todo_by_id(todo_id)

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_data: TodoUpdate, session=Depends(get_session)):
    repo = TodoRepository(session)
    service=TodoService(repo)
    return await service.update_todo(todo_data)

@router.delete("/{todo_id}", response_model=bool)
async def delete_todo(todo_id:int, session=Depends(get_session)):
    repo = TodoRepository(session)
    service = TodoRepository(repo)
    return await service.delete(todo_id)