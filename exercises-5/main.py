from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.routers.todo_router import router as todo_router

app = FastAPI(
    title="Todo API (DB version)",
    version="1.0.0",
    description="FastAPI + PostgreSQL + Clean Architecture",
)


@app.get("/health/db", tags=["Health"])
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}


app.include_router(todo_router)
