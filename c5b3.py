
print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")


a = "Hello Guy!"  # Biến toàn cục

def say():
    global a  # Khai báo rằng hàm sẽ sử dụng và thay đổi biến toàn cục 'a'
    a = "Vinh University"  # Thay đổi giá trị của biến toàn cục
    print(a)  # In giá trị của biến toàn cục sau khi thay đổi

say()  # Gọi hàm say()
print(a)  # In giá trị của biến toàn cục sau khi thay đổi từ trong hàm
