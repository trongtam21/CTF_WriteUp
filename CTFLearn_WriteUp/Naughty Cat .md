## Đề
> I think my cat is hiding something...
## Link 
> https://ctflearn.com/challenge/download/890
## Giải 
- Sau khi tải file về tôi nhận được 1 con mèo 
- Thử lần lượt qua các phương pháp đơn giản như exiftool, strings, cat, ... 
```text
Warning                         : [minor] Trailer data after PNG IEND chunk
> Với exiftool 
```
```text
y0u_4r3_cl0s3.rar
Cat!
f1n4lly.txt0
K_Vk
 gY 
purrr_2.mp3

> Với strings 
```
- Ở đây tôi thấy có nhiều file ẩn 
- Extract nó ra bằng binwalk 
- Ta được 5 file 
```text
28E4B.rar  29  29.zlib  purrr_2.mp3  y0u_4r3_cl0s3.rar
```
- Kiểm tra định dạng cho chắc 
- File  y0u_4r3_cl0s3.rar không phải file rar =)))
- Đổi phần hex lại 
- Đối chiếu hex của file 28E4B.rar  qua 
- `52 61 72 21 ` 
- Sau khi chỉnh xong kiểm tra phát nữa `file y0u_4r3_cl0s3.rar `
- Giờ thì giải nén 
- Mật khẩu =)))
- Chắc nó có liên quan đến file mp3
- Ta có 1 web  `https://academo.org/demos/spectrum-analyzer/` chuyển file âm thanh sang dạng dữ liệu đọc
- Khi kết nối file vào ta được mật khẩu (Hơi khó nhìn tí) `sp3ctrum_1s_y0ur_fr13nd`
- Giải nén ta được đoạn strings `ZjByM241MWNzX21hNXQzcg==`
> echo "ZjByM241MWNzX21hNXQzcg==" | base64 -d
> f0r3n51cs_ma5t3r
- Flag : flag{f0r3n51cs_ma5t3r}