## Đề 
> We found this file. Recover the flag.
## Link 
> https://mercury.picoctf.net/static/d0129ad98ba9258ab59e7700a1b18c14/tunn3l_v1s10n
## Hint 
> Weird that it won't display right...
## Giải 
- Đầu tiên để giải bài này ta phải xác định 1 số thông tin cụ thể như loại file, đuôi, siêu dữ liệu ....
- Điều này ta có thể kiểm tra tại trang web `https://www.aperisolve.com/` khi nó là những file có đuôi được hỗ trợ 
- Ở đây file của ta chưa có đuôi nên bắt buộc ta phải kiểm tra bằng command line 
- `exiftool tunn3l_v1s10n`
```text
ExifTool Version Number         : 12.65
File Name                       : tunn3l_v1s10n
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2023:11:06 15:12:30+07:00
File Access Date/Time           : 2023:11:06 15:13:56+07:00
File Inode Change Date/Time     : 2023:11:06 15:12:30+07:00
File Permissions                : -rw-r--r--
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Unknown (53434)
Image Width                     : 1134
Image Height                    : 306
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Red Mask                        : 0x27171a23
Green Mask                      : 0x20291b1e
Blue Mask                       : 0x1e212a1d
Alpha Mask                      : 0x311a1d26
Color Space                     : Unknown (,5%()
Rendering Intent                : Unknown (826103054)
Image Size                      : 1134x306
Megapixels                      : 0.347
```
- Tại phần `MIME Type                       : image/bmp` ta có thể dễ dàng xác định được file chính là bmp 
- Đổi đuôi file thành .bmp rồi bắt đầu sửa file thông qua hexeditor
- Vì phần đầu của file bị hỏng nên tôi sửa phần đầu trước 
- Dựa vào google tôi sửa phần đầu của file thành `42 4d 7e 00 00 00 00 00 00 00 3e 00 00 00 28 00` thì xuất hiện 1 fake flag 
- Nhưng thay vào đó tại viền của ảnh ta thấy nó còn 1 phần nữa
- Thứ tiếp theo là ta phải thay đổi kích thước tệp tại byte thứ 23 và 24 của tệp tin 
- 3201(hex) => F401(hex) [tương ứnG với chiều cao 500]
- Vẫn chưa có gì nên tôi tăng tiếp lên 1200(dec) tương ứnG kí tự trog hex là B004(hex)
- Ta sẽ có flag : `picoCTF{qu1t3_a_v13w_2020}`
  