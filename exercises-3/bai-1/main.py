from file_utils import read_file_content, count_word_frequency


def main():
    filename = input("Nhập tên file cần phân tích: ")

    try:
        content = read_file_content(filename)
        freq = count_word_frequency(content)

        total_words = sum(freq.values())
        print(f"Tổng số từ: {total_words}")
        print("Top 10 từ xuất hiện nhiều nhất:")

        top10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]
        for word, count in top10:
            print(f"- {word}: {count}")

    except FileNotFoundError:
        print("❌ File không tồn tại")
    except Exception as e:
        print(f"❌ Có lỗi xảy ra: {e}")


if __name__ == "__main__":
    main()
