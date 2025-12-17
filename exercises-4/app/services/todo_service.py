from fastapi import HTTPException
from typing import Optional
from app.models.todo import TodoCreate, TodoUpdate


_todos: list[dict] = []
_id_counter = 1


def _check_duplicate_title(title: str, exclude_id: Optional[int] = None):
    for t in _todos:
        if exclude_id is not None and t["id"] == exclude_id:
            continue
        if t["title"].lower() == title.lower():
            raise HTTPException(
                status_code=409,
                detail="Todo title already exists",
            )


def create_todo(data: TodoCreate) -> dict:
    global _id_counter
    _check_duplicate_title(data.title)

    todo = {
        "id": _id_counter,
        **data.model_dump(),
    }
    _todos.append(todo)
    _id_counter += 1
    return todo


def get_all_todos(
    *, done: Optional[bool], keyword: Optional[str], limit: int
) -> list[dict]:
    results = _todos

    if done is not None:
        results = [t for t in results if t["done"] == done]

    if keyword:
        kw = keyword.lower()
        results = [t for t in results if kw in t["title"].lower()]

    return results[:limit]


def get_todo_by_id(todo_id: int) -> Optional[dict]:
    for t in _todos:
        if t["id"] == todo_id:
            return t
    return None


def replace_todo(todo_id: int, data: TodoCreate) -> Optional[dict]:
    for idx, t in enumerate(_todos):
        if t["id"] == todo_id:
            _check_duplicate_title(data.title, exclude_id=todo_id)
            new_todo = {
                "id": todo_id,
                **data.model_dump(),
            }
            _todos[idx] = new_todo
            return new_todo
    return None


def update_todo(todo_id: int, data: TodoUpdate) -> Optional[dict]:
    for t in _todos:
        if t["id"] == todo_id:
            if data.title is not None:
                _check_duplicate_title(data.title, exclude_id=todo_id)
                t["title"] = data.title
            if data.description is not None:
                t["description"] = data.description
            if data.priority is not None:
                t["priority"] = data.priority
            if data.done is not None:
                t["done"] = data.done
            return t
    return None


def delete_todo(todo_id: int) -> bool:
    global _todos
    for idx, t in enumerate(_todos):
        if t["id"] == todo_id:
            _todos.pop(idx)
            return True
    return False
