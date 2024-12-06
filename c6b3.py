
print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Định nghĩa hàm với đối số không xác định
def get_sum(*num):
    tmp = 0
    # Duyệt qua từng tham số được truyền vào
    for i in num:
        tmp += i  # Cộng dồn các giá trị
    return tmp  # Trả về tổng

# Gọi hàm với nhiều tham số
result = get_sum(1, 2, 3, 4, 5)
print(result)  # In ra kết quả
