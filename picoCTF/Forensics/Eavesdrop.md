## Đề 
> Download this packet capture and find the flag.

    Download packet capture
## Link 
> https://artifacts.picoctf.net/c/135/capture.flag.pcap
## Hint 
> All we know is that this packet capture includes a chat conversation and a file transfer.
## Giải 
- Sau khi tải xuống được 1 file có tên capture.flap.pcap
- Em bắt đầu các tác vụ kiểm tra đơn giản như : Kiểm tra xem có file nào truyền đi không? Kiểm tra luồng dữ liệu xem có gì không? Kiểm tra tổng quan các gói dữ liệu...
- Sau khi kiểm tra luồng dữ liệu tcp em thấy 1 đoạn chat sau 
```text
Hey, how do you decrypt this file again?
You're serious?
Yeah, I'm serious
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Ok, great, thanks.
Let's use Discord next time, it's more secure.
C'mon, no one knows we use this program like this!
Whatever.
Hey.
Yeah?
Could you transfer the file to me again?
Oh great. Ok, over 9002?
Yeah, listening.
Sent it
Got it.
You're unbelievable
```
- Em thấy được 1 đoạn kết nối giải mã openssl sử dụng file file.des3 và đầu ra là file file.txt
- Giờ mục tiêu của ta là tìm file file.des3
- Thấy dòng dưới có đề cập đến port 9002
- Em sẽ filter đến port 9002
```text
Salted__<K&....,J.......o..%....I{97X...........
```
- Đây chính là file file.des3
- Chúng ta cần lưu dưới dạng hexa bằng cách tuỳ chọn raw
- Lưu ý : Chỉ có thể chạy được khi file ở loại ` openssl enc'd data with salted password`
- Còn nếu copy paste thì phải đổi loại file lại
> openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123 
- Kiểm tra file file.txt
```text
┌──(trongtam㉿kali)-[~/Downloads]
└─$ cat file.txt 
picoCTF{nc_73115_411_0ee7267a}    
```
