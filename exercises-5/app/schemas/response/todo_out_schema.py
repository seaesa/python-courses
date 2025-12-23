from pydantic import BaseModel
from datetime import datetime


class TodoOut(BaseModel):
    id: int
    title: str
    description: str | None
    priority: int
    done: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
