## Đề 
> The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.
## Giải
- Ở đây họ bảo kết nối ssh đến user bandit và port 2220 nên tôi tìm cách cách nối 
- Sau khi tìm 1 hồi thì tôi đã tìm được cách kết nối ssh tại [link](https://linuxopsys.com/topics/ssh-command)
> ssh bandit0@bandit.labs.overthewire.org -p 2220 (cái này lấy ở level 0)
```text
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme]
cat: readme]: No such file or directory
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit0@bandit:~$ 
```
> Password : NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL