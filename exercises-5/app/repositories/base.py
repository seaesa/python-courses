from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get(self, db: Session, id: int) -> T | None:
        return db.get(self.model, id)

    def add(self, db: Session, obj: T):
        db.add(obj)
