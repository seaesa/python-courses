from app.models.base import Base
from app.models.todo import Todo

target_metadata = Base.metadata

context.configure(
    connection=connection,
    target_metadata=target_metadata,
    compare_type=True,
)
