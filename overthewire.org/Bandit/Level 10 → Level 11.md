## Đề 
> The password for the next level is stored in the file data.txt, which contains base64 encoded data
## Kết nối máy chủ 
> ssh bandit10@bandit.labs.overthewire.org -p 2220 (password : G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s)
## Giải 
- Sau khi mở file data.txt thì thấy 1 đoạn chuỗi `VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==`
- Đây chính là mã háo base64
- Decode nó để lấy password
```text
bandit10@bandit:~$ echo 'VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==' | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```
- Hoặc `base64 -d data.txt` để decode luôn file 