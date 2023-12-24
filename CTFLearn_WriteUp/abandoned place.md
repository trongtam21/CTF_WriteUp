## Đề :
> the flag is outside of the pic, try to find it. another hint: dimensions, dimensions, everything is in dimensions.
## Link 
> https://ctflearn.com/challenge/download/1000
## Giải 
- Ngay từ cái hint nó đã bảo mình chú ý về kích thước 
- Tôi bắt đầu bằng cách kiểm tra dữ liệu metadata bằng `exiftool `
- Chú ý kích thước 1 tí thấy ảnh có kích thước là `2016x900`
- Theo như hint đề bài thì họ bắt mình đổi kích thước bức ảnh 
- Ý tưởng của tôi là đổi kích thước ảnh bằng `hexeditor `
- Mà để thực hiện được nó thì ta phải dổi kích thước ảnh cái đã
- Mỗi phần height và weight thì sẽ có 4 byte 
- Bắt đầu đổi thì kết quả thu được 2016 : `7E0` vì lấy 4 byte nên ta thêm số không vào trước cho đủ `07E0`
- 900 : `384` vì lấy 4 byte nên ta thêm số không vào trước cho đủ `0384`
- Tôi sẽ đổi chỗ của nó cho nhau 
- Mở hexeditor lên và tìm hex của 2016 là 07e0 trước, thay nó bằng 0384
- Tiếp theo thay 0384 bằng 07e0
- Mở lại file ảnh thì ta thấy được flag : `CTFlearn{urban_exploration}`