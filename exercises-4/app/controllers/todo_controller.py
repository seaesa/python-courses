from fastapi import APIRouter, HTTPException, Query, status
from typing import Optional, List
from app.models.todo import TodoCreate, TodoUpdate, TodoOut
from app.services import todo_service


router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate):
    return todo_service.create_todo(payload)


@router.get("", response_model=List[TodoOut])
def get_todos(
    done: Optional[bool] = None,
    keyword: Optional[str] = None,
    limit: int = Query(10, ge=1, le=50),
):
    return todo_service.get_all_todos(done=done, keyword=keyword, limit=limit)


@router.get("/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int):
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoOut)
def replace_todo(todo_id: int, payload: TodoCreate):
    todo = todo_service.replace_todo(todo_id, payload)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=TodoOut)
def patch_todo(todo_id: int, payload: TodoUpdate):
    todo = todo_service.update_todo(todo_id, payload)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    deleted = todo_service.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
