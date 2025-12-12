s = input("Nhập câu: ")

s = s.strip()

words = s.split()
s = " ".join(words)

if s:
    s = s[0].upper() + s[1:].lower()

while s.endswith("..") or s.endswith("..."):
    s = s[:-1]

if not s.endswith("."):
    s += "."

print("Kết quả:", s)
