def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


n = int(input("Nhập n: "))

S = 1.0
for i in range(1, n + 1):
    k = 2 * i - 1
    S += 1 / factorial(k)

print("Tổng S =", S)
