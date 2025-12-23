from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.todo import Todo
from app.repositories.base import BaseRepository


class TodoRepository(BaseRepository[Todo]):
    def __init__(self):
        super().__init__(Todo)

    def get_by_title(self, db: Session, title: str):
        stmt = select(Todo).where(Todo.title.ilike(title))
        return db.scalar(stmt)

    def search(self, db: Session, *, done, keyword, offset, limit):
        stmt = select(Todo)

        if done is not None:
            stmt = stmt.where(Todo.done == done)
        if keyword:
            stmt = stmt.where(Todo.title.ilike(f"%{keyword}%"))

        return db.scalars(stmt.offset(offset).limit(limit)).all()
