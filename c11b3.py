print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Hàm tính số tiền nhận được sau k tháng
def benefit(t, n, k):
    # Tính số tiền nhận được sau k tháng
    total_amount = n * (1 + t / 100) ** k
    return total_amount

# Nhập dữ liệu từ người dùng
try:
    t = float(input("Nhập lãi suất hàng tháng (t%): "))
    n = float(input("Nhập số vốn ban đầu (n): "))
    k = int(input("Nhập số tháng gửi (k): "))

    # Kiểm tra tính hợp lệ của đầu vào
    if t < 0 or n <= 0 or k <= 0:
        print("Lãi suất, vốn ban đầu và số tháng gửi phải là số dương hợp lệ.")
    else:
        # Tính và in kết quả
        result = benefit(t, n, k)
        print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")
except ValueError:
    print("Vui lòng nhập số hợp lệ cho lãi suất, số vốn và số tháng.")
