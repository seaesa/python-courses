from student import Student


def load_students_from_file(filename: str) -> list[Student]:
    students: list[Student] = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    name, age_str, score_str = line.split(",")
                    age = int(age_str)
                    score = float(score_str)
                    students.append(Student(name, age, score))
                except ValueError:
                    print(f"⚠️ Dòng {line_no} sai format, bỏ qua")

    except FileNotFoundError:
        raise

    return students


def calc_avg_score(students: list[Student]) -> float:
    if not students:
        return 0.0
    return sum(s.score for s in students) / len(students)


def find_top_student(students: list[Student]):
    if not students:
        return None
    return max(students, key=lambda s: s.score)


def filter_failed(students: list[Student]) -> list[Student]:
    return [s for s in students if not s.is_passed()]
