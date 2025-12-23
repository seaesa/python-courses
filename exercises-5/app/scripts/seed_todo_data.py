from app.core.database import SessionLocal
from app.models.todo import Todo


def run():
    db = SessionLocal()
    if db.query(Todo).count() == 0:
        db.add_all(
            [
                Todo(title="Learn FastAPI", priority=1),
                Todo(title="Learn SQLAlchemy", priority=2),
                Todo(title="Alembic Migration", priority=3),
                Todo(title="Dockerize App", priority=4),
                Todo(title="Clean Architecture", priority=5),
            ]
        )
        db.commit()
    db.close()


if __name__ == "__main__":
    run()
