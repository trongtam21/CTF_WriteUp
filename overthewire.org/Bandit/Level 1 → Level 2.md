## Đề 
> The password for the next level is stored in a file called - located in the home directory
## Kết nối máy chủ 
> ssh bandit1@bandit.labs.overthewire.org -p 2220 (password : NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL)
## Giải 
- Đầu tiên, nhìn zô đề bài tôi thấy đoạn file `-` nằm trong thư mục chính.
- Phải di chuyển đến thư mục chính trước 
```text
bandit1@bandit:~$ cd ..
bandit1@bandit:/home$ ls
bandit0   bandit13  bandit18  bandit22  bandit27      bandit29-git  bandit31-git  bandit6   drifter1   drifter15  drifter6     formulaone1  krypton1  krypton6
bandit1   bandit14  bandit19  bandit23  bandit27-git  bandit3       bandit32      bandit7   drifter10  drifter2   drifter7     formulaone2  krypton2  krypton7
bandit10  bandit15  bandit2   bandit24  bandit28      bandit30      bandit33      bandit8   drifter12  drifter3   drifter8     formulaone3  krypton3  ubuntu
bandit11  bandit16  bandit20  bandit25  bandit28-git  bandit30-git  bandit4       bandit9   drifter13  drifter4   drifter9     formulaone5  krypton4
bandit12  bandit17  bandit21  bandit26  bandit29      bandit31      bandit5       drifter0  drifter14  drifter5   formulaone0  formulaone6  krypton5
```
- Vì đang làm bandit1 nên kiểm tra folder bandit1 chứ đâu nữa
- Có 1 file `-` nhưng không đọc được bằng lệnh cat thông thường  
- Dựa vào trang [web](https://unix.stackexchange.com/questions/16357/usage-of-dash-in-place-of-a-filename) có thể đọc thông qua lệnh cat ./-
> cat ./-
> Password :  rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi