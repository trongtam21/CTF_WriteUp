## Đề
The password for the next level is stored in the file data.txt next to the word millionth
## Kết nối máy chủ
> ssh bandit7@bandit.labs.overthewire.org -p 2220 (password : z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S)
## Giải 
- Sau khi kết nối tôi thấy được 1 file tên data.txt
- Đọc file data.txt tôi thấy được hàng loạt chuỗi kí tự với form `word - string`
- Đề bảo password ở bên cạnh chữ `millionth` thì dùng grep 
```text
bandit7@bandit:~$ strings data.txt | grep millionth
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP

```
> Password : TESKZC0XvTetK0S9xNwm25STk5iWrBvP