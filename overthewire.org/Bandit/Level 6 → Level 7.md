## Đề 
```text
The password for the next level is stored somewhere on the server and has all of the following properties:
 
    owned by user bandit7
    owned by group bandit6
    33 bytes in size
``` 
## Kết nối máy chủ 
> ssh bandit6@bandit.labs.overthewire.org -p 2220 (password : P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU)
## Giải 
- Vì ở đây nó bắt mình tìm mật khẩu của file có user là bandit7 và group là bandit6 có kích thước 33 byte 
- Dùng pwd để xác định vị trí hiện tại (đang nằm ở /home/bandit6)
- Tôi di chuyển để tìm xem có gì không thì tại /home có rất nhiều folder
- Để tổng quan hơn ta sẽ tìm từ thư mục gốc (/)
- 
- Có vẻ kết quả hơi nhiều, ta còn 2 dữ kiện là `user bandit7` và group `bandit6`
- Giờ có một cách để in ra được `user` và `group` là sử dụng option -user và -group của lệnh find
- Lúc đầu tôi sử dụng kết hợp giữa find và du, nhưng không có kết quả
> find / -type f -user bandit7 -group bandit6 -exec du -b {} + | awk '$1 == 33 {print $2}'
- Thực ra lệnh find cũng cho phép tìm theo size
> find / -type f -user bandit7 -group bandit6 -size 33c 2>dev/null
```text
2: Đây là một đối số được chuyển đến lệnh find để xử lý thông báo lỗi. Trong trường hợp này, 2 chỉ đơn giản là một con số được thêm vào lệnh để "đàn áp" thông báo lỗi. Trong ngữ cảnh này, nếu find không thể truy cập một số thư mục hoặc tệp, nó sẽ không xuất thông báo lỗi lên màn hình. Số 2 thường được sử dụng trong UNIX-like shells để chỉ đến lỗi chuẩn (stderr).
```
- Nó sẽ đưa đến dev/null để không in ra
- Kết quả:
> /var/lib/dpkg/info/bandit7.password
- In password
> Password : z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

