products = [
    (1, "Ban Phim", 250_000),
    (2, "Chuot", 150_000),
    (3, "Man Hinh", 3_000_000),
    (4, "Tai Nghe", 500_000),
]

orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]

# a. product_map
product_map = {pid: {"name": name, "price": price} for pid, name, price in products}

print("=== a. Product Map ===")
print(product_map)

# b. Tính tổng tiền cho từng hóa đơn
for order in orders:
    total = 0
    for pid in order["items"]:
        total += product_map[pid]["price"]
    order["total"] = total

# c. In danh sách hóa đơn
print("\n=== c. Danh sach hoa don ===")
for order in orders:
    print(
        f"{order['order_id']}: {len(order['items'])} san pham, Tong tien = {order['total']:,} VND"
    )

# d. Sản phẩm đã bán
all_products_sold = set()
for order in orders:
    all_products_sold.update(order["items"])

print("\n=== d. Tổng sản phẩm khác nhau đã bán ===")
print(f"So luong san pham khac nhau da ban: {len(all_products_sold)}")
