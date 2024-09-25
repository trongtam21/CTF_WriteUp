import subprocess
import random
import shlex  # Thư viện mới

flag = list("*" * 42)
char = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM<>?:\"|{}[];',./!@#$%^&*()qwertyuiopsdfghjklzxcvbnm!@#$%^&*()"

while True:
    # Tạo chuỗi ngẫu nhiên 41 ký tự
    data = ''.join(random.choice(char) for _ in range(41))

    # Sử dụng shlex.quote để an toàn với các ký tự đặc biệt
    quoted_data = shlex.quote(data)

    # Thực thi lệnh và lấy đầu ra
    result = subprocess.run(f'echo {quoted_data} | ./trash_can_fixed', shell=True, capture_output=True, text=True)

    # Lấy đầu ra từ lệnh
    output = result.stdout.strip()  # Loại bỏ khoảng trắng thừa

    # Kiểm tra mã thoát
    if result.returncode != 0:
        print("Lỗi khi thực thi lệnh:", result.stderr)
        break  # Dừng vòng lặp nếu có lỗi

    # Lấy chuỗi sau khoảng trắng cuối cùng
    result = output.rsplit(' ', 1)[-1]

    # Cập nhật flag dựa trên kết quả
    for i in range(len(result)):
        if result[i] != "*" and flag[i] == "*":
            flag[i] = result[i]  # Cập nhật ký tự trong flag nếu có sự khác biệt

    # Kiểm tra nếu flag không còn dấu "*"
    if "*" not in flag:
        print("Flag:", ''.join(flag))  # Chuyển danh sách trở lại chuỗi để in
        break