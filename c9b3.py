print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Đây là các hàm thực hiện các phép toán cơ bản
# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    if y == 0:
        return "Không thể chia cho 0"
    else:
        return x / y

# In ra các lựa chọn phép toán
print("Chọn phép toán.")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")

# Nhận lựa chọn và số liệu từ người dùng
choice = input("Nhập lựa chọn (1/2/3/4): ")

# Nhập hai số
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

# Thực hiện phép toán tương ứng với lựa chọn của người dùng
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Lựa chọn không hợp lệ")
