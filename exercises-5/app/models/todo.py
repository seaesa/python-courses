from sqlalchemy import String, Integer, Boolean, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from app.models.mixins import TimeMixin


class Todo(Base, TimeMixin):
    __tablename__ = "todos"
    __table_args__ = (UniqueConstraint("title", name="uq_todos_title"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
