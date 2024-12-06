print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Định nghĩa hàm kiểm tra số chẵn hay lẻ
def checkValue(n):
    if n % 2 == 0:  # Kiểm tra nếu số n chia hết cho 2
        print("Đây là một số chẵn")
    else:  # Nếu không chia hết cho 2
        print("Đây là một số lẻ")

# Gọi hàm để kiểm tra
checkValue(7)  # Kiểm tra số 7
checkValue(8)  # Kiểm tra số 8
