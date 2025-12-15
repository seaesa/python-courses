from datetime import datetime
from task_service import load_tasks, save_tasks
from models import Task

FILENAME = "tasks.txt"


def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def main():
    tasks = load_tasks(FILENAME)

    while True:
        print("\n1. Xem tất cả task")
        print("2. Xem các task quá hạn")
        print("3. Thêm task mới")
        print("4. Đánh dấu task là done")
        print("5. Thoát")

        choice = input("Chọn: ")

        try:
            if choice == "1":
                show_tasks(tasks)

            elif choice == "2":
                now = datetime.now()
                for task in tasks:
                    if task.is_overdue(now):
                        print(task)

            elif choice == "3":
                desc = input("Mô tả: ")
                due_str = input("Ngày hạn (YYYY-MM-DD): ")
                due_date = datetime.strptime(due_str, "%Y-%m-%d")

                tasks.append(Task(desc, due_date))
                save_tasks(FILENAME, tasks)

            elif choice == "4":
                show_tasks(tasks)
                idx = int(input("Nhập số thứ tự: ")) - 1
                tasks[idx].status = "done"
                save_tasks(FILENAME, tasks)

            elif choice == "5":
                break

            else:
                print("❌ Lựa chọn không hợp lệ")

        except ValueError:
            print("❌ Dữ liệu nhập không hợp lệ")
        except Exception as e:
            print(f"❌ Có lỗi xảy ra: {e}")


if __name__ == "__main__":
    main()
