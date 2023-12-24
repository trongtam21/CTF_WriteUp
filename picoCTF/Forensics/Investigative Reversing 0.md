## Đề :
> We have recovered a binary and an image. See what you can make of it. There should be a flag somewhere.
## Link :
> https://jupiter.challenges.picoctf.org/static/70fd416f817ab1e59beaf19dc2b586cd/mystery
> https://jupiter.challenges.picoctf.org/static/70fd416f817ab1e59beaf19dc2b586cd/mystery.png
## Hint :
1. Try using some forensics skills on the image
2. This problem requires both forensics and reversing skills
3. A hex editor may be helpful
## Giải :
- Đầu tiên tôi tải 2 file rồi mở ra xem có gì 
- Đối với file `.png` tôi kiểm tra bằng `exiftool` và `zsteg` thì kết quả có 1 vài điểm lưu ý như sau :
  > Warning                         : [minor] Trailer data after PNG IEND chunk
- Có 1 vài dữ liệu sau file png
  > 00000000: 70 69 63 6f 43 54 4b 80  6b 35 7a 73 69 64 36 71  |picoCTK.k5zsid6q|
    00000010: 5f 64 31 64 65 65 64 61  61 7d                    |_d1deedaa}      |
imagedata           .. text: "PPP@@@@@@@@@@@@"
- Vì có dữ liệu ẩn nên tôi dùng binwalk 
- Trong file `5B.zlib` có 1 đoạn sau : `picoCTK.k5zsid6q_d1deedaa}`
- Dựa theo bảng mã ascii thì K=>F (số trong bảng mã sẽ giảm 5). Giữ lại `_d1deedaa}` không cần đổi theo dữ liệu từ `zsteg`
- Lần lượt chuyển dựa trên quy tắc đó ta được flag : `picoCTF{f0und_1t_d1deedaa}}
