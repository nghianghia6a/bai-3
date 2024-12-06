print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")


import math

# Khởi tạo vị trí ban đầu
pos = [0, 0]

# Vòng lặp để nhận dữ liệu từ người dùng
while True:
    s = input("Nhập hướng và số bước (hoặc bỏ trống để kết thúc): ")
    
    # Nếu không có dữ liệu đầu vào, kết thúc vòng lặp
    if not s:
        break
    
    # Tách hướng và số bước
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    
    # Cập nhật vị trí theo hướng
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass

# Tính toán khoảng cách từ (0,0) đến vị trí hiện tại
distance = math.sqrt(pos[0]**2 + pos[1]**2)

# In ra khoảng cách làm tròn đến số nguyên gần nhất
print(int(round(distance)))
