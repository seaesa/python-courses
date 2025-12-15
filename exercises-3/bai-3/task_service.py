from datetime import datetime
from models import Task


def load_tasks(filename: str) -> list[Task]:
    tasks: list[Task] = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    desc, due_str, status = line.split(";")
                    due_date = datetime.strptime(due_str, "%Y-%m-%d")
                    tasks.append(Task(desc, due_date, status))
                except ValueError:
                    print(f"⚠️ Dòng {line_no} sai format, bỏ qua")

    except FileNotFoundError:
        pass

    return tasks


def save_tasks(filename: str, tasks: list[Task]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            date_str = task.due_date.strftime("%Y-%m-%d")
            f.write(f"{task.description};{date_str};{task.status}\n")
