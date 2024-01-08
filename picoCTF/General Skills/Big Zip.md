## Đề 
> Unzip this archive and find the flag.
## Link 
> https://artifacts.picoctf.net/c/503/big-zip-files.zip
## Hint 
> Can grep be instructed to look at every file in a directory and its subdirectories?
- Đầu tiên em tải file zip về rồi giải nén nó ra.
- Ối trời ôi, nhiều file vcl.
- Tiếp theo em dùng `find -D tree` để nó hiện ra cây thư mục.
- Cũng nhiều đấy, sau khi quan sát 1 lượt. Em lại dùng tiếp 1 lệnh grep pico xem thử có file nào tên vậy không 
- `find -D tree | grep pico`, vẫn không có file nào có chữ pico cả.
- Không có ở tên file thì chắc có trong nội dung rồi. Nếu tìm trong nội dung thì ta dùng lệnh `find -D tree | grep -r pico`
- sau 1 hồi thì ta thu được flag: `picoCTF{gr3p_15_m4g1c_ef8790dc}` tại `folder folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt`
