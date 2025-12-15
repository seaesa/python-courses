from student_service import (
    load_students_from_file,
    calc_avg_score,
    find_top_student,
    filter_failed,
)


def main():
    filename = input("Nhập tên file điểm sinh viên: ")

    try:
        students = load_students_from_file(filename)

        avg = calc_avg_score(students)
        print(f"Điểm trung bình lớp: {avg:.2f}")

        top = find_top_student(students)
        if top:
            print("Sinh viên điểm cao nhất:")
            print(top)

        failed = filter_failed(students)
        print("Danh sách sinh viên bị rớt:")
        for s in failed:
            print("-", s)

    except FileNotFoundError:
        print("❌ Không mở được file")
    except Exception as e:
        print(f"❌ Có lỗi xảy ra: {e}")


if __name__ == "__main__":
    main()
