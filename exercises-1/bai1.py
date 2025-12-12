def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 0


def is_valid_date(day, month, year):
    if year < 1 or month < 1 or month > 12:
        return False
    return 1 <= day <= days_in_month(month, year)


def next_day(day, month, year):
    day += 1
    if day > days_in_month(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year


def previous_day(day, month, year):
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = days_in_month(month, year)
    return day, month, year


d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if not is_valid_date(d, m, y):
    print("Ngày không hợp lệ!")
else:
    nd = next_day(d, m, y)
    pd = previous_day(d, m, y)
    print("Ngày kế tiếp:", nd)
    print("Ngày trước đó:", pd)
