students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

courses = {"math", "python"}

print("=== a. Danh sach hoc vien ===")
for sid, name, age in students:
    print(f"{sid} - {name} ({age})")

python_scores = []
for sid, name, age in students:
    python_scores.append((sid, name, scores[sid]["python"]))

print("\n=== b. Python Scores ===")
print(python_scores)

top_student = max(python_scores, key=lambda x: x[2])
print(f"\n=== c. Top Python: {top_student[1]} - {top_student[2]}")

courses.add("database")
for sid in scores:
    scores[sid]["database"] = 0

print("\n=== d. Courses & Scores sau khi thêm 'database' ===")
print(courses)
print(scores)
