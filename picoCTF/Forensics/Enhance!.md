## Đề 
> Download this image file and find the flag.
## Link 
> https://artifacts.picoctf.net/c/101/drawing.flag.svg
## Giải 
- Như mọi khi tôi sẽ kiểm tra loại file và metadata trước 
> "drawing.flag.svg: SVG Scalable Vector Graphics image"
> ExifTool Version Number         : 12.65
File Name                       : drawing.flag.svg
Directory                       : .
File Size                       : 4.1 kB
File Modification Date/Time     : 2023:10:13 17:33:33+07:00
File Access Date/Time           : 2023:10:13 17:33:37+07:00
File Inode Change Date/Time     : 2023:10:13 17:33:33+07:00
File Permissions                : -rw-r--r--
File Type                       : SVG
File Type Extension             : svg
MIME Type                       : image/svg+xml
Xmlns                           : http://www.w3.org/2000/svg
Image Width                     : 210mm
Image Height                    : 297mm
View Box                        : 0 0 210 297
SVG Version                     : 1.1
ID                              : svg8
Version                         : 0.92.5 (2060ec1f9f, 2020-04-08)
Docname                         : drawing.svg
Metadata ID                     : metadata5
Work Format                     : image/svg+xml
Work Type                       : http://purl.org/dc/dcmitype/StillImage
- Cũng không có gì để xem
- Tiếp theo tôi kiểm tra bằng `strings ` thì thấy nó được cấu tạo từ những đoạn mã html 
- Tại dòng dưới cùng tôi thấy `c 3 d _ 2 4 3 7 4 6 7 5 }` nó giống như 1 phần của flag
- Tìm xem 1 vài chỗ nữa vẫn như vậy
- Nó đều nằm trong cặp "tspan"
- Bắt đầu tìm nó trên linux `strings drawing.flag.svg | grep tspan `
  >  id="text3723"><tspan
         id="tspan3748">p </tspan><tspan
         id="tspan3754">i </tspan><tspan
         id="tspan3756">c </tspan><tspan
         id="tspan3758">o </tspan><tspan
         id="tspan3760">C </tspan><tspan
         id="tspan3762">T </tspan><tspan
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         id="tspan3752">c 3 d _ 2 4 3 7 4 6 7 5 }</tspan></text>

- Flag đã thấy nhưng giờ ta phải xử lý 1 vài chỗ 
- `strings drawing.flag.svg | grep "</tspan" | cut -d '>' -f2 | cut -d '<' -f1 | tr -d '\n' | tr -d ' '`
- Trong đó `cut -d '>' f2` là xoá phần trước '>'
- `cut -d '<' -f1` là xoá phần sau '<'
- `tr -d '\n'` là xoá phần xuống hàng 
- `tr -d ' '` là xoá dấu cách 
- Flag : `picoCTF{3nh4nc3d_24374675}`
