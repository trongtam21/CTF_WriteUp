- Đề : I've hidden a flag in this file. Can you find it? Forensics is fun.pptm 
- Link : https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensics%20is%20fun.pptm
- Dùng binwalk -e xem trong folder có chứa gì không.
- Truy cập vào thư mục "_Forensics is fun.pptm.extracted"
- Nhìn thấy thư mục 0.zip không biết có gì không? cứ giải nén ra rồi tính sau : unzip 0.zip
- Bây giờ 1 là bạn list qua hết từ đầu đến cuối xem có gì không 
- 2 là dùng lệnh command (t chọn cách 2)
- Dùng command thì mò thôi
- Grep -r pico (éo có gì) hoặc cũng có thể tìm "{"
- Find -D tree|grep flag (cũng chả có)
- Dừng lại 1 chút, có thể file ẩn sẽ có tên hidden hay hide gì đó 
- Tìm cả 2 "find -D tree|grep hidden" hoặc "find -D tree|grep hide"
- Sau 1 hồi thì cái 1 có kết quả trả về là "./0/ppt/slideMasters/hidden" và "./ppt/slideMasters/hidden"
- Xem dữ liệu cả 2 đều giống nhau "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q"
- Giờ dùng để loại bỏ khoảng trắng rồi decode chứ xoá từng cái chắc chết =)), nhanh hơn thì vứt lên chat GPT cho nó tự sửa
-" string = "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q"

new_string = ""

for character in string:
  if character != " ":
    new_string += character

print(new_string)"
- Decode ra được flag : picoCTF{D1d_u_kn0w_ppts_r_z1p5}
