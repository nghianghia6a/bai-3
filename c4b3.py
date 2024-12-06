print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")


a = "Hello Guy!"  # Biến toàn cục

def say(a):  # Hàm nhận tham số đầu vào a
    a = "Vinh University"  # Biến cục bộ (thay đổi giá trị chỉ trong hàm)
    print(a)  # In giá trị của biến cục bộ

say(a)  # Gọi hàm say() và truyền giá trị của biến toàn cục 'a' vào
print(a)  # In giá trị của biến toàn cục 'a'
