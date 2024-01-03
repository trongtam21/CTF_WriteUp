## Đề 
> The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.
## Kết nối máy chủ 
> ssh bandit4@bandit.labs.overthewire.org -p 2220 (password : 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe)
## Giải 
- Vì mật khẩu trong folder inhere nên tôi kiểm tra tổng quan folder này trước 
```text
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ la
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ 
```
- Kiểm tra lần lượt ta thu được mật khẩu 
```text
bandit4@bandit:~/inhere$ strings ./-file00
HRrtZ
bandit4@bandit:~/inhere$ strings ./-file09
bandit4@bandit:~/inhere$ strings ./-file08
bandit4@bandit:~/inhere$ strings ./-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
bandit4@bandit:~/inhere$ strings ./-file06
bandit4@bandit:~/inhere$ strings ./-file05
bandit4@bandit:~/inhere$ strings ./-file04
eE}:
bandit4@bandit:~/inhere$ strings ./-file03
MUb4
bandit4@bandit:~/inhere$ strings ./-file02
```
> Password : lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
- Ngoài ra cũng có thể in hết ra 1 lượt
```text
bandit4@bandit:~/inhere$ strings ./-file0*
HRrtZ
MUb4
eE}:
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```