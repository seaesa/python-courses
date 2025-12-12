users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}

# a. user_map
user_map = {uid: name for uid, name in users}

print("=== a. User Map ===")
print(user_map)

# b. In danh sách bài viết
print("\n=== b. Danh sách bài viết ===")
for pid, info in posts.items():
    author = user_map[info["author_id"]]
    tags = ", ".join(sorted(info["tags"]))
    print(f"[{pid}] {info['title']} - {author} - Tags: {tags}")

# c. Tập tất cả tag
all_tags = set()
for post in posts.values():
    all_tags.update(post["tags"])

print("\n=== c. All Tags ===")
print(all_tags)

# d. Đếm số bài viết theo tag
tag_counter = {}
for post in posts.values():
    for t in post["tags"]:
        tag_counter[t] = tag_counter.get(t, 0) + 1

print("\n=== d. Tag Counter ===")
print(tag_counter)
