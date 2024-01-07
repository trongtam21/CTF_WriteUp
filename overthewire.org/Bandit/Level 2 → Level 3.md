## Đề 
> The password for the next level is stored in a file called spaces in this filename located in the home directory
## Kết nối máy chủ 
> ssh bandit2@bandit.labs.overthewire.org -p 2220 (password : rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi)
## Giải 
- Sau khi kiểm tra các tập tin tại thư mục cha, em thấy có 1 hoặc 4 tập tin tên `spaces in this filename`, do không biết nó là bao nhiêu tập tin nên phải dùng đến command ll
```text
bandit2@bandit:~$ ls spaces in this filename
bandit2@bandit:~$ ll
total 24
drwxr-xr-x  2 root    root    4096 Oct  5 06:19 ./
drwxr-xr-x 70 root    root    4096 Oct  5 06:20 ../
-rw-r--r--  1 root    root     220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root    root    3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root    root     807 Jan  6  2022 .profile
-rw-r-----  1 bandit3 bandit2   33 Oct  5 06:19 spaces in this filename
```
- Rõ ràng đây là 1 file
- Để đọc nó ta dùng cat nhưng vì chứa dấu cách nên phải bọc nó trong  dấu " "
> cat 'spaces in this filename'
> Password : aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
