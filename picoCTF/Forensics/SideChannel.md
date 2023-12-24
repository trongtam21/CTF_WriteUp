## Đề 
> There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? Download the PIN checker program here pin_checker Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using nc saturn.picoctf.net 53639 and provide it the PIN to get your flag.
## Link
> https://artifacts.picoctf.net/c/74/pin_checker
## Connect netcat 
> nc saturn.picoctf.net 53639
## Hint 
> Read about "timing-based side-channel attacks."
> Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.
> Don't run your attacks against the master server, it is secured against them. The PIN code you get from the pin_checker binary is the same as the one for the master server.
## Giải
- Kết nối với máy chủ xem sau 
- Tại đây họ bắt nhập PIN
- Dựa và hint thứ 3 ta có thể lấy file `pin_checker` để tìm PIN từ đây
- Nhưng có điều là chạy file pin_checker không được =))) `./pin_checker`
```text
./pin_checker                                     
zsh: permission denied: ./pin_checker
```
- Vì thông báo không có quyền nên ta phải cấp quyền cho nó 
- `chmod +x pin_checker`
- Giờ thì chạy nó thôi 
- Câu đầu tiên đập vào mắt là :
```text
Please enter your 8-digit PIN code:
```
- Vì mã pin đã được giới hạn 8 chữ số nên ta có thể thu hẹp phạm vi tìm kiếm
- Đối với hint 1 
- Về tấn công `timing-based side-channel` theo như google thì đây là :
```text
Timing-based side-channel là một loại tấn công mật mã liên quan đến việc phân tích lượng thời gian cần thiết để hệ thống thực hiện một hoạt động cụ thể. Kẻ tấn công đo thời gian cần thiết để thực hiện một số hoạt động mã hóa nhất định, chẳng hạn như mã hóa hoặc giải mã và sử dụng thông tin này để hiểu rõ hơn về tính bảo mật của hệ thống.

Kẻ tấn công sử dụng thông tin này để suy ra các bí mật được sử dụng trong hệ thống mật mã, chẳng hạn như khóa hoặc mật khẩu. Kiểu tấn công này có thể được sử dụng để phá vỡ các cơ chế bảo mật khác nhau, chẳng hạn như giao thức xác thực, xác minh mật khẩu và mã hóa.
```
- Có nghĩa khi ta nhập 2 mã PIN khác nhau, thời gian xử lý là khác nhau tuỳ vào nó có gần với mật khẩu chính xác hay không 
- Để kiểm tra xem suy nghĩ của mình là đúng hay sai tôi sẽ viết 1 script để xem thời gian chạy của mỗi mã PIN khác nhau
```text
import os 
import time 

for i in range(10000000, 100000000, 10000000):
#lay gia tri thoi gian truoc khi chay
	dau = time.time()
	print(i)
	os.system(f'echo "{i}" | ./pin_checker')
#lay gia tri thoi gian sau khi chay
	sau = time.time()
	sum_time_run = sau - dau
	print(sum_time_run)
```
- Đây là sau khi chạy 
```text
10000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.16505980491638184
20000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.1621243953704834
30000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.21753287315368652
40000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.3217661380767822
50000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.16131877899169922
60000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.15843558311462402
70000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.18326926231384277
80000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.1679856777191162
90000000
Please enter your 8-digit PIN code:
8
Checking PIN...
Access denied.
0.16034936904907227
```
- Có thể nhận ra tại i = 40000000 thời gian chạy lâu hơn hẳn
- Bây giờ cần tìm thời gian chạy lâu nhất => PIN > Flag 
- Thay script lại tí 
```text
import os 
import time 
max = 0
for i in range(10000000, 100000000, 10000000):
#lay gia tri thoi gian truoc khi chay
	dau = time.time()
	#print(i)
	os.system(f'echo "{i}" | ./pin_checker > /dev/null 2>&1')
#lay gia tri thoi gian sau khi chay
	sau = time.time()
	sum_time_run = sau - dau
	if sum_time_run > max :
		max = sum_time_run
		i_max = i
print(i_max)
print(max)
```
- `/dev/null 2>&1` là lệnh ẩn khỏi màn hình, đoạn code chỉ hiển thị giá trị PIN có thời gian xử lý cao nhất 
> Sau khi chạy : 40000000    
> 0.3773956298828125
- Thay đổi giá trị hàm for ngắn lại nữa 
> for i in range(`40000000, 50000000, 1000000`):
> Sau khi chạy :  48000000
> 0.4621877670288086
- Tiếp tục thay đổi giá trị hàm for
> for i in range(48000000, 50000000, 100000):
> Sau khi chạy : 48300000
> 0.6854500770568848
- Tiếp tục 
> for i in range(48300000, 49000000, 10000):
> Sau khi chạy : 48390000
> 0.9181723594665527
- Tiếp tục 
> for i in range(48390000, 48400000, 100):
> Sau khi chạy : 48390500
> 1.0159051418304443
- Tiếp tục
> for i in range(48390500, 48390600, 10):
> 48390510
> 1.1949114799499512
- Bây giờ con số đã xuống đến hàng đơn vị ta nên kiểm tra từng cái, do càng gần thời gian sẽ càng gần nhau => tạo sai số
```text
import os 
import time 
max = 0
for i in range(48390510, 48390520, 1):
	print(i)
	os.system(f'echo "{i}" | ./pin_checker')
```
```text
48390513
Please enter your 8-digit PIN code:
8
Checking PIN...
Access granted. You may use your PIN to log into the master server.
```
- Ta đã tìm được PIN 
- Kết nối bằng netcat để nhận flag thôi 
> Flag : picoCTF{t1m1ng_4tt4ck_914c5ec3}



