## Đề 
> Can you find the flag? 
## Link 
> https://mercury.picoctf.net/static/df92c613964fca8edec3b2981f69c3e4/shark2.pcapng
## Hint 
> Did you really find _the_ flag?
> Look for traffic that seems suspicious.
## Giải 
- Đầu tiên theo chỉ dẫn tôi xem thử dữ liệu có cái strings nào có chứ flag không bằng lệnh `tcp contains "picoCTF"` thì nguyên 1 kho với phương thức http hiện ra. Đây ắt hẳn là giả.
- Tiếp theo tôi sử dụng `export object` thì vẫn không có gì đặt biệt
- Lại cố chấp phân tích tại `conversation` thì thấy tại mục ipv4 có giao tiếp giữa ip `8.8.8.8` và `192.168.38.104` có 1 vài điểm lưu ý 
- Tại cái queries luôn có form như sau : `[str].reddshrimpandherring.com.windomain.local`
- Kiểm tra lần lượt bằng `conversation` tại gói 4374 có strings `sq==` rất có thể nó là base64
- Ta sẽ thu thập các đoạn trước cụm `.reddshrimpandherring.com.windomain.local` và ip `18.217.1.57` và giao thức dns bằng filter `dns and ip.dst == 18.217.1.57`
- Copy lần lượt từng strings và nối lại ta sẽ được `cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==`
- Decode ta sẽ có flag : `picoCTF{dns_3xf1l_ftw_deadbeef}`