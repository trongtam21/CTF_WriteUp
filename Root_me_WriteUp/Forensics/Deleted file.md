## Đề 
> Your cousin found a USB drive in the library this morning. He’s not very good with computers, so he’s hoping you can find the owner of this stick!

The flag is the owner’s identity in the form `firstname_lastname`
## Link 
> http://challenge01.root-me.org/forensic/ch39/ch39.gz
## Giải 
- Đầu tiên em tải file về và giải nén nó ra 
- Sau khi giải nén em được 1 file có tên usb.image 
- Em kiểm tra file bằng lệnh fls trên cmd 
```text
┌──(trongtam㉿kali)-[~/Downloads]
└─$ fls usb.image 
r/r 3:  USB         (Volume Label Entry)
r/r * 5:        anonyme.png
v/v 1013699:    $MBR
v/v 1013700:    $FAT1
v/v 1013701:    $FAT2
V/V 1013702:    $OrphanFiles
```
- Vì chưa thành thục khi phân tích đĩa trên linux bằng lệnh nên em sử dụng công cụ FTK imager
- Sau khi mở lên ta sẽ có 1 file anonyme.png
- Để biết được người tạo, em sẽ xem phần metadata với exiftool
```text
┌──(trongtam㉿kali)-[~/Downloads]
└─$ exiftool ftk_a0ec0156-0ee3-4c6c-a1ce-b5c578c7d99f.png 
ExifTool Version Number         : 12.65
File Name                       : ftk_a0ec0156-0ee3-4c6c-a1ce-b5c578c7d99f.png
Directory                       : .
File Size                       : 246 kB
File Modification Date/Time     : 2023:12:13 17:30:32+07:00
File Access Date/Time           : 2023:12:13 17:30:45+07:00
File Inode Change Date/Time     : 2023:12:13 17:30:33+07:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 400
Image Height                    : 300
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Gamma                           : 2.2
White Point X                   : 0.3127
White Point Y                   : 0.329
Red X                           : 0.64
Red Y                           : 0.33
Green X                         : 0.3
Green Y                         : 0.6
Blue X                          : 0.15
Blue Y                          : 0.06
Background Color                : 255 255 255
XMP Toolkit                     : Image::ExifTool 11.88
Creator                         : Javier Turcot
Image Size                      : 400x300
Megapixels                      : 0.120
```
> Password : javier_turcot
