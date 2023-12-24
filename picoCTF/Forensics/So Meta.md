## Đề 
> Find the flag in this picture.
# Link 
> https://jupiter.challenges.picoctf.org/static/89b371a46702a31aa9931a2a2b12f8bf/pico_img.png
## Hint  
> What does meta mean in the context of files?
> Ever heard of metadata?
## Cách 1 
- Đầu tiên tôi nhìn thấy hint có đề cập đến metadata nên tôi dùng `exiftool` để xem 
- Tại dòng : Artist tôi tìm thấy flag : `picoCTF{s0_m3ta_eb36bf44}`
## Cách 2 
- Tôi sử dụng `strings` để xem dữ liệu file png `strings pico_img.png`
- Tôi tìm thấy flag tại 2 dòng cuối cùng : `picoCTF{s0_m3ta_eb36bf44}`
## Cách 3 
- Vì đây chính là file png nên ta có thể dùng thêm `zsteg`. Sau khi dùng `zsteg pico_img.png` thì tôi thấy có dòng : `meta Artist         .. text: "picoCTF{s0_m3ta_eb36bf44}"` và đó cũng chính là flag.
