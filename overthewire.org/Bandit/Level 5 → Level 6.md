## Đề 
```text
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
    human-readable
    1033 bytes in size
    not executable
```
## Kết nối máy chủ 
> ssh bandit5@bandit.labs.overthewire.org -p 2220 (password : lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR)
## Giải 
- Giờ ta sẽ tìm file với 3 điều kiện (Đọc được, thực thi được, size là 1033 byte)
- Ta sẽ có 1 lệnh du để tìm các điều kiện trên 
- Tài liệu đọc [tại đây](https://quantrimang.com/cong-nghe/cac-lenh-du-tien-dung-nhat-trong-linux-165399)
- Đầu tiên em liệt kê các file xem sao 
```text
bandit5@bandit:~$ find /home/bandit5 -type f
/home/bandit5/inhere/maybehere14/.file3
/home/bandit5/inhere/maybehere14/spaces file2
/home/bandit5/inhere/maybehere14/-file2
/home/bandit5/inhere/maybehere14/-file1
/home/bandit5/inhere/maybehere14/-file3
/home/bandit5/inhere/maybehere14/spaces file3
/home/bandit5/inhere/maybehere14/.file1
/home/bandit5/inhere/maybehere14/spaces file1
/home/bandit5/inhere/maybehere14/.file2
/home/bandit5/inhere/maybehere09/.file3
/home/bandit5/inhere/maybehere09/spaces file2
/home/bandit5/inhere/maybehere09/-file2
/home/bandit5/inhere/maybehere09/-file1
/home/bandit5/inhere/maybehere09/-file3
/home/bandit5/inhere/maybehere09/spaces file3
/home/bandit5/inhere/maybehere09/.file1
/home/bandit5/inhere/maybehere09/spaces file1
/home/bandit5/inhere/maybehere09/.file2
/home/bandit5/inhere/maybehere00/.file3
/home/bandit5/inhere/maybehere00/spaces file2
/home/bandit5/inhere/maybehere00/-file2
/home/bandit5/inhere/maybehere00/-file1
/home/bandit5/inhere/maybehere00/-file3
/home/bandit5/inhere/maybehere00/spaces file3
/home/bandit5/inhere/maybehere00/.file1
/home/bandit5/inhere/maybehere00/spaces file1
/home/bandit5/inhere/maybehere00/.file2
/home/bandit5/inhere/maybehere17/.file3
/home/bandit5/inhere/maybehere17/spaces file2
/home/bandit5/inhere/maybehere17/-file2
/home/bandit5/inhere/maybehere17/-file1
/home/bandit5/inhere/maybehere17/-file3
/home/bandit5/inhere/maybehere17/spaces file3
/home/bandit5/inhere/maybehere17/.file1
/home/bandit5/inhere/maybehere17/spaces file1
/home/bandit5/inhere/maybehere17/.file2
/home/bandit5/inhere/maybehere11/.file3
/home/bandit5/inhere/maybehere11/spaces file2
/home/bandit5/inhere/maybehere11/-file2
/home/bandit5/inhere/maybehere11/-file1
/home/bandit5/inhere/maybehere11/-file3
/home/bandit5/inhere/maybehere11/spaces file3
/home/bandit5/inhere/maybehere11/.file1
/home/bandit5/inhere/maybehere11/spaces file1
/home/bandit5/inhere/maybehere11/.file2
/home/bandit5/inhere/maybehere15/.file3
/home/bandit5/inhere/maybehere15/spaces file2
/home/bandit5/inhere/maybehere15/-file2
/home/bandit5/inhere/maybehere15/-file1
/home/bandit5/inhere/maybehere15/-file3
/home/bandit5/inhere/maybehere15/spaces file3
/home/bandit5/inhere/maybehere15/.file1
/home/bandit5/inhere/maybehere15/spaces file1
/home/bandit5/inhere/maybehere15/.file2
/home/bandit5/inhere/maybehere05/.file3
/home/bandit5/inhere/maybehere05/spaces file2
/home/bandit5/inhere/maybehere05/-file2
/home/bandit5/inhere/maybehere05/-file1
/home/bandit5/inhere/maybehere05/-file3
/home/bandit5/inhere/maybehere05/spaces file3
/home/bandit5/inhere/maybehere05/.file1
/home/bandit5/inhere/maybehere05/spaces file1
/home/bandit5/inhere/maybehere05/.file2
/home/bandit5/inhere/maybehere01/.file3
/home/bandit5/inhere/maybehere01/spaces file2
/home/bandit5/inhere/maybehere01/-file2
/home/bandit5/inhere/maybehere01/-file1
/home/bandit5/inhere/maybehere01/-file3
/home/bandit5/inhere/maybehere01/spaces file3
/home/bandit5/inhere/maybehere01/.file1
/home/bandit5/inhere/maybehere01/spaces file1
/home/bandit5/inhere/maybehere01/.file2
/home/bandit5/inhere/maybehere04/.file3
/home/bandit5/inhere/maybehere04/spaces file2
/home/bandit5/inhere/maybehere04/-file2
/home/bandit5/inhere/maybehere04/-file1
/home/bandit5/inhere/maybehere04/-file3
/home/bandit5/inhere/maybehere04/spaces file3
/home/bandit5/inhere/maybehere04/.file1
/home/bandit5/inhere/maybehere04/spaces file1
/home/bandit5/inhere/maybehere04/.file2
/home/bandit5/inhere/maybehere16/.file3
/home/bandit5/inhere/maybehere16/spaces file2
/home/bandit5/inhere/maybehere16/-file2
/home/bandit5/inhere/maybehere16/-file1
/home/bandit5/inhere/maybehere16/-file3
/home/bandit5/inhere/maybehere16/spaces file3
/home/bandit5/inhere/maybehere16/.file1
/home/bandit5/inhere/maybehere16/spaces file1
/home/bandit5/inhere/maybehere16/.file2
/home/bandit5/inhere/maybehere07/.file3
/home/bandit5/inhere/maybehere07/spaces file2
/home/bandit5/inhere/maybehere07/-file2
/home/bandit5/inhere/maybehere07/-file1
/home/bandit5/inhere/maybehere07/-file3
/home/bandit5/inhere/maybehere07/spaces file3
/home/bandit5/inhere/maybehere07/.file1
/home/bandit5/inhere/maybehere07/spaces file1
/home/bandit5/inhere/maybehere07/.file2
/home/bandit5/inhere/maybehere10/.file3
/home/bandit5/inhere/maybehere10/spaces file2
/home/bandit5/inhere/maybehere10/-file2
/home/bandit5/inhere/maybehere10/-file1
/home/bandit5/inhere/maybehere10/-file3
/home/bandit5/inhere/maybehere10/spaces file3
/home/bandit5/inhere/maybehere10/.file1
/home/bandit5/inhere/maybehere10/spaces file1
/home/bandit5/inhere/maybehere10/.file2
/home/bandit5/inhere/maybehere13/.file3
/home/bandit5/inhere/maybehere13/spaces file2
/home/bandit5/inhere/maybehere13/-file2
/home/bandit5/inhere/maybehere13/-file1
/home/bandit5/inhere/maybehere13/-file3
/home/bandit5/inhere/maybehere13/spaces file3
/home/bandit5/inhere/maybehere13/.file1
/home/bandit5/inhere/maybehere13/spaces file1
/home/bandit5/inhere/maybehere13/.file2
/home/bandit5/inhere/maybehere08/.file3
/home/bandit5/inhere/maybehere08/spaces file2
/home/bandit5/inhere/maybehere08/-file2
/home/bandit5/inhere/maybehere08/-file1
/home/bandit5/inhere/maybehere08/-file3
/home/bandit5/inhere/maybehere08/spaces file3
/home/bandit5/inhere/maybehere08/.file1
/home/bandit5/inhere/maybehere08/spaces file1
/home/bandit5/inhere/maybehere08/.file2
/home/bandit5/inhere/maybehere02/.file3
/home/bandit5/inhere/maybehere02/spaces file2
/home/bandit5/inhere/maybehere02/-file2
/home/bandit5/inhere/maybehere02/-file1
/home/bandit5/inhere/maybehere02/-file3
/home/bandit5/inhere/maybehere02/spaces file3
/home/bandit5/inhere/maybehere02/.file1
/home/bandit5/inhere/maybehere02/spaces file1
/home/bandit5/inhere/maybehere02/.file2
/home/bandit5/inhere/maybehere18/.file3
/home/bandit5/inhere/maybehere18/spaces file2
/home/bandit5/inhere/maybehere18/-file2
/home/bandit5/inhere/maybehere18/-file1
/home/bandit5/inhere/maybehere18/-file3
/home/bandit5/inhere/maybehere18/spaces file3
/home/bandit5/inhere/maybehere18/.file1
/home/bandit5/inhere/maybehere18/spaces file1
/home/bandit5/inhere/maybehere18/.file2
/home/bandit5/inhere/maybehere03/.file3
/home/bandit5/inhere/maybehere03/spaces file2
/home/bandit5/inhere/maybehere03/-file2
/home/bandit5/inhere/maybehere03/-file1
/home/bandit5/inhere/maybehere03/-file3
/home/bandit5/inhere/maybehere03/spaces file3
/home/bandit5/inhere/maybehere03/.file1
/home/bandit5/inhere/maybehere03/spaces file1
/home/bandit5/inhere/maybehere03/.file2
/home/bandit5/inhere/maybehere06/.file3
/home/bandit5/inhere/maybehere06/spaces file2
/home/bandit5/inhere/maybehere06/-file2
/home/bandit5/inhere/maybehere06/-file1
/home/bandit5/inhere/maybehere06/-file3
/home/bandit5/inhere/maybehere06/spaces file3
/home/bandit5/inhere/maybehere06/.file1
/home/bandit5/inhere/maybehere06/spaces file1
/home/bandit5/inhere/maybehere06/.file2
/home/bandit5/inhere/maybehere12/.file3
/home/bandit5/inhere/maybehere12/spaces file2
/home/bandit5/inhere/maybehere12/-file2
/home/bandit5/inhere/maybehere12/-file1
/home/bandit5/inhere/maybehere12/-file3
/home/bandit5/inhere/maybehere12/spaces file3
/home/bandit5/inhere/maybehere12/.file1
/home/bandit5/inhere/maybehere12/spaces file1
/home/bandit5/inhere/maybehere12/.file2
/home/bandit5/inhere/maybehere19/.file3
/home/bandit5/inhere/maybehere19/spaces file2
/home/bandit5/inhere/maybehere19/-file2
/home/bandit5/inhere/maybehere19/-file1
/home/bandit5/inhere/maybehere19/-file3
/home/bandit5/inhere/maybehere19/spaces file3
/home/bandit5/inhere/maybehere19/.file1
/home/bandit5/inhere/maybehere19/spaces file1
/home/bandit5/inhere/maybehere19/.file2
/home/bandit5/.profile
/home/bandit5/.bashrc
/home/bandit5/.bash_logout
```
- Ta dùng lệnh du -b để hiển thị dung lượng theo đơn vị byte 
- Em sẽ kết hợp các lệnh lại với nhau 
> find /home/bandit5 -type f -exec du -b {} + | awk '$1 == 1033 {print $2}'
- Giải thích 1 tí 
- Đầu tiên `find /home/bandit5 -type f -exec du -b {}` sẽ tìm kiếm các file có trong `/home/bandit5` theo đơn vị byte 
- Sau đó dùng dấu `|` để chuyển dữ liệu thu được cho awk (Đây là hàm sử lý kết quả của lệnh), nếu dung lượng cột thứ nhất ($1) = 1033 thì in ra cột thứ 2 ($2)
> Kết quả sau khi chạy là : /home/bandit5/inhere/maybehere07/.file2
- Đọc file `.file2`
> Password : P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU