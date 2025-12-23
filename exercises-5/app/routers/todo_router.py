from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.request.todo_schema import TodoCreate, TodoUpdate
from app.schemas.response.todo_out_schema import TodoOut
from app.services import todo_service

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("", response_model=TodoOut, status_code=201)
def create(data: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, data)


@router.get("", response_model=list[TodoOut])
def list_todos(
    done: bool | None = None,
    keyword: str | None = None,
    offset: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return todo_service.list_todos(db, done, keyword, offset, limit)


@router.get("/{todo_id}", response_model=TodoOut)
def get(todo_id: int, db: Session = Depends(get_db)):
    return todo_service.get_todo(db, todo_id)


@router.put("/{todo_id}", response_model=TodoOut)
def put(todo_id: int, data: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.update_todo_put(db, todo_id, data)


@router.patch("/{todo_id}", response_model=TodoOut)
def patch(todo_id: int, data: TodoUpdate, db: Session = Depends(get_db)):
    return todo_service.update_todo_patch(db, todo_id, data)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo_service.delete_todo(db, todo_id)
