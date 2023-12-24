- Đề : Download the packet capture file and use packet analysis software to find the flag.
- Link : https://artifacts.picoctf.net/c/196/network-dump.flag.pcap
- HINT : Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.
- Sau khi tải file `network-dump.flag.pcap` tôi bắt đầu mở nó lên bằng wireshark
- Tổng cộng có 5 gói tin
- Tôi bắt đầu kiểm tra luồng dữ liệu TCP thì thấy định dạng của flag nhưng mỗi chữ có mỗi dấu cách nên không thể submit được `p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ 0 1 b 0 a 0 d 6 }`
- Chạy đoạn code python này để lại dấu cách ra 
chuoi = "Đây là một chuỗi có dấu cách"
chuoi_khong_dau_cach = chuoi.replace(" ", "")
print(chuoi_khong_dau_cach)
- Sau khi thế vào ta được flag như sau : `picoCTF{p4ck37_5h4rk_01b0a0d6}`