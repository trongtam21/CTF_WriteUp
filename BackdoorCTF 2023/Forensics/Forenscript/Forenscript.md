## Đề 
> It's thundering outside and you are you at your desk having solved 4 forensics challenges so far. Just pray to god you solve this one. You might want to know that sometimes too much curiosity hides the flag.
## Tải file 
> Ở phần a.bin trên github
## Giải 
- Sau hi tải file về tôi dùng các lệnh cơ bản như strings, file, exiftool kiểm tra thì xuất hiện vấn đề là loại file không được xác định
- Sau khi dùng hexeditor để xem thì tôi thấy rằng file đã bị đảo các byte 
- Đây là phần đầu
```text
00000000  47 4E 50 89  0A 1A 0A 0D   0D 00 00 00  52 44 48 49                                                                                          GNP.........RDHI
00000010  46 0C 00 00  A5 04 00 00   00 00 06 08  3D AB 1F 00                                                                                          F...........=...
00000020  00 00 00 7C  47 52 73 01   CE AE 00 42  00 00 E9 1C                                                                                          ...|GRs....B....
00000030  41 67 04 00  00 00 41 4D   FC 0B 8F B1  00 00 05 61                                                                                          Ag....AM.......a
00000040  48 70 09 00  00 00 73 59   00 00 87 1D  8F 01 87 1D                                                                                          Hp....sY........
```
- Chú ý kĩ các byte đầu, đây ắt hẳn là PNG và IHDR bị đảo ngược
- Viết 1 script để chỉnh về ban đầu 
- Tôi tạo 1 file tên image.png để lưu file 
```text
with open('a.bin', 'rb') as file_r:
	#mo che do doc nhi phan
	with open('image.png', 'wb') as file_w:
	#mo che do ghi nhi phan
		while True:
			i = file_r.read(4)
			#doc lan luot 4 byte
			if not i:
				break
			file_w.write(i[::-1])
```
- Sau khi chạy tôi được 1 nội dung tên fake flag
- Kiểm tra tổng quát thêm phát nữa tôi thấy rằng có 1 file nén ẩn trong này 
```text
┌──(trongtam㉿kali)-[~/Downloads]
└─$ ls
KCSC_tuyen_thanh_vien_2023  _image.png.extracted  a.bin  image.png  run.py
                                                                                                                                                                       
┌──(trongtam㉿kali)-[~/Downloads]
└─$ cd _image.png.extracted 
                                                                                                                                                                       
┌──(trongtam㉿kali)-[~/Downloads/_image.png.extracted]
└─$ ls
5B  5B.zlib  EAEB  EAEB.zlib                          
````
- Kiểm tra lần lượt từng cái 
- Kiểm tra 1 hồi vẫn không có gì 
- Quay lại file image.png thì dumaaaaa có 1 tệp PNG nữa bên trong ở dòng 0000EA90 > INT là 60048
- Giờ phải viết scipt cắt xuất file ra
- Tôi sẽ tạo file ảnh nữa tên là image2.png
```text
batdau = 60048
ketthuc = 128183

with open('image.png', 'rb') as file_r:
	with open('image2.png', 'wb') as file_w:
		file_r.seek(batdau)
		#ham seek di con tro den vi tri cu the
		data = file_r.read(ketthuc - batdau)
		file_w.write(data)
```
- Sau khi kết thúc ta thu được flag 
> Flag : flag{scr1pt1ng_r34lly_t0ugh_a4n't_1t??}


