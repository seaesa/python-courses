from fastapi import FastAPI
from app.controllers.todo_controller import router as todo_router


app = FastAPI(title="Todo In-memory API")


app.include_router(todo_router)
