## Đề 
> The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
## Kết nối máy chủ 
> ssh bandit9@bandit.labs.overthewire.org -p 2220 (password : EN632PlfYiZbn3PhVK3XOGSlNInNE00t)
## Giải 
- Sau khi kết nối, ta thu được file data.txt
- Dùng strings để đọc thì ta thấy được password
- Còn nếu tìm như đề cho thì thêm grep '==' vào 
> strings data.txt | grep '=='
```text
bandit9@bandit:~$ strings data.txt | grep '==='
x]T========== theG)"
========== passwordk^
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```
> Password : G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s