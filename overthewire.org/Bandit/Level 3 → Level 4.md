## Đề 
> The password for the next level is stored in a hidden file in the inhere directory.
## Kết nối máy chủ 
> ssh bandit3@bandit.labs.overthewire.org -p 2220 (password : aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG)
## Giải 
- Để xem được những thư mục ẩn ta dùng lệnh `ls -a` hoặc `la`
- Sau khi kiểm tra tổng quan ta thấy 
```text
bandit:~$ ls
inhere
bandit3@bandit:~$ la
.bash_logout  .bashrc  inhere  .profile
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ la
.hidden
```
- Trong này có 1 file ẩn tên `.hidden`
```text
bandit3@bandit:~/inhere$ cat .hidden 
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```