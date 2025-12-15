from datetime import datetime


class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date
        self.status = status

    def is_overdue(self, now: datetime) -> bool:
        return self.status == "todo" and self.due_date < now

    def __str__(self) -> str:
        status = self.status.upper()
        date_str = self.due_date.strftime("%Y-%m-%d")
        return f"[{status}] {self.description} (Hạn: {date_str})"
