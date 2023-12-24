- Đề : Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there: https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg Can you help me? TIP: Decode the flag until you got a sentence.
- Tải hình ảnh xuống, trong ảnh là 1 nhân vật hoạt hình gì đấy tôi cũng không nhớ nữa =)))
- Đọc đề bài thấy có dòng decode là biết có dòng nào bị mã hoá rồi
- Đầu tiên tôi dùng `exiftool` để xem dữ liệu.
- Tôi đặc biệt chú ý tới dùng `keyword` với dòng `Current IPTC Digest` để đó tí tính sau.
- Rảnh tay tôi lại thử 1 lệnh strings xem sao.
- Bất ngờ nó cho tôi 1 đường dẫn `https://mega.nz/file/wZw2nAhS#i3Q0r-R8psiB8zwUrqHTr661d8FiAS1Ott8badDnZkoH`
- Và 1 số thông tin thú vị 
- $You_Still_Here/Nothing_Here_16/..txt
https://mega.nz/file/wZw2nAhS#i3Q0r-R8psiB8zwUrqHTr661d8FiAS1Ott8badDnZkoH
You_Still_Here/Nothing_Here_1
You_Still_Here/Nothing_Here_10
You_Still_Here/Nothing_Here_11
You_Still_Here/Nothing_Here_12
You_Still_Here/Nothing_Here_13
You_Still_Here/Nothing_Here_14
You_Still_Here/Nothing_Here_15
You_Still_Here/Nothing_Here_16
You_Still_Here/Nothing_Here_17
You_Still_Here/Nothing_Here_18
You_Still_Here/Nothing_Here_19
You_Still_Here/Nothing_Here_2
You_Still_Here/Nothing_Here_3
You_Still_Here/Nothing_Here_4
You_Still_Here/Nothing_Here_5
You_Still_Here/Nothing_Here_6
You_Still_Here/Nothing_Here_7
You_Still_Here/Nothing_Here_8
You_Still_Here/Nothing_Here_9
You_Still_Here.
- Tôi lại dùng binwalk để trích xuất file ẩn
- Truy cập vào folder `_Hey_You.png.extracted`
- Dựa theo thông tin ở trên tôi truy cập vào `Nothing_Here_16` nhưng kết quả éo có gì =)))
- còn 1 đường dẫn tôi chưa xem
- truy cập vào đường dẫn và tải file xuống
- Lại dùng `exiftool` không có thônh tin gì nên tôi thử `strings`
- Kết quả tôi thấy `YouWon(Almost).jpg`
- `binwalk  -e Only_Few_Steps.jpg` rồi truy cập vào `_Only_Few_Steps.jpg.extracted `
- `strings YouWon(Almost).jpg`
- Flag đây chứ đâu nữa : CTF{VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=)
- decode thôi Flag : Có cái nịt á, sau khi decode 1 lần thì có cái nịt. Ngay từ đề bài nó bảo decode đến khi nào ra flag thì thôi
- Flag : `CTF{M1NI0NS_ARE_C00L}`
