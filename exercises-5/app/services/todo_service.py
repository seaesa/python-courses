from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository
from app.schemas.request.todo_schema import TodoCreate, TodoUpdate
from app.models.todo import Todo

repo = TodoRepository()


def create_todo(db: Session, data: TodoCreate) -> Todo:
    if repo.get_by_title(db, data.title):
        raise HTTPException(status_code=409, detail="Title already exists")

    todo = Todo(**data.model_dump())
    repo.add(db, todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todo(db: Session, todo_id: int) -> Todo:
    todo = repo.get(db, todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    return todo


def list_todos(db, done, keyword, offset, limit):
    return repo.search(db, done=done, keyword=keyword, offset=offset, limit=limit)


def update_todo_put(db, todo_id, data: TodoCreate):
    todo = get_todo(db, todo_id)
    for k, v in data.model_dump().items():
        setattr(todo, k, v)
    db.commit()
    return todo


def update_todo_patch(db, todo_id, data: TodoUpdate):
    todo = get_todo(db, todo_id)
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(todo, k, v)
    db.commit()
    return todo


def delete_todo(db, todo_id):
    todo = get_todo(db, todo_id)
    db.delete(todo)
    db.commit()
