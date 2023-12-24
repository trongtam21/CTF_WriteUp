## Đề 
> Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it! 
## Link 
> https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making
## Giải 
- Đầu tiên tôi thử qua lần lượt các tool thì thấy đầu file có đoạn mã `�PB`
- Điều đó có nghĩa định dạng file chỗ này bị lỗi 
- Để sửa nó, tôi mở hexeditor lên và chuyển về định dạng hình ảnh `.PNG`
- `8950 4e47 0d0a 1a0a 0000 000d` đây là định dạng các byte đầu của file png 
- Quay lại file lúc nãy thì bây giờ file đã chuyển thành file ảnh.
- Có thể trong ảnh đó có những mã màu bị đè lên 
- Để xem được nó tôi truy cập vào `https://www.aperisolve.com/`. Nhưng trước khi up lên thì tôi phải đổi đuôi file sang png
- Tại phần `Superimposed` và `Red` trên trang web thì ta thu được flag
- flag : `picoCTF{w1z4rdry}`