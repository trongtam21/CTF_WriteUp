## Description 
> After Karen started working for 'TAAUSAI,' she began to do some illegal activities inside the company. 'TAAUSAI' hired you as a soc analyst to kick off an investigation on this case.
You acquired a disk image and found that Karen uses Linux OS on her machine. Analyze the disk image of Karen's computer and answer the provided questions.
## Link challenge 
> https://cyberdefenders.org/blueteam-ctf-challenges/insider/
## Solution 
- Sau khi tải và giải nén tệp zip với mật khẩu là `cyberdefenders.org` em thu được 1 file ad1, giờ thì trả lời các câu hỏi thôi.
- Load lên FTK image, em nhận ra rằng có 3 folder `/boot /root /var`
- **What distribution of Linux is being used on this machine?**
- Lướt qua 1 vòng thấy rằng `/boot` chứa `chứa các tập tin cấu hình khởi động linux` trong đó chứa thông tin của bản phân phối linux đang được sử dụng 
- ![image](image/4.PNG)
> A : kali

- **What is the MD5 hash of the apache access.log?**
- Câu hỏi liên quan đến log ta kiểm tra tại folder /var/log vì nơi đây chứa các log của hệ thống, tại apache2/access.log em xuất md5 của nó bằng cách chuột phải chọn `export file hash list` và đọc file csv (hoặc có thể export file rồi dùng cmd với lệnh md5sum [filename])
> A : d41d8cd98f00b204e9800998ecf8427e

- ***It is believed that a credential dumping tool was downloaded? What is the file name of the download?***
- Em check phần download thì thấy 1 tệp `mimikatz_trunk.zip`
> A : mimikatz_trunk.zip

- ***There was a super-secret file created. What is the absolute path?***
- Tại phần `.bash_history` có 1 vài điều thú vị như sau 
<details>
<summary>
- Xem file .bash_history
</summary>

```
msfconsole
systemctl status postgresql
systemctl enable postgresql
systemctl start postgresql
msfconsole
msfdb init
msfconsole
shutdown now
touch snky snky > /root/Desktop/SuperSecretFile.txt
cat snky snky > /root/Desktop/SuperSecretFile.txt 
msfconsole 
clear
history
clear
history
whoami
hack
do hack
do hack please
i am a hacker
how to hack
pwd
ls
ls -la
touch delete-me.txt
rm delete-me.txt 
ls
cd Documents/
mkdir myfirsthack
cd myfirsthack/
touch hellworld.sh
vim hellworld.sh 
chmod +x hellworld.sh 
./hellworld.sh 
touch firstscript
vim firstscript 
chmod +x firstscript 
./firstscript 
vim firstscript 
cp firstscript firstscript_fixed
ls
vim firstscript
vim firstscript_fixed 
./firstscript_fixed 
flag<this is a flag>
ifconfig
cd ..
cd..
cd ..
cd /var/log/
ls
cd ..
cd ~
ls
pwf
pwd
top
wall -h
wall yolo
ls
pwd
cd ..
ls
cd home/
ls
cd /root
ls
cd ../root
cd ../root/Documents/myfirsthack/../../Desktop/
sl
ls
cd ../Documents/myfirsthack/
netstat
echo bob.txt
touch bob.txt 
echo "If you're still reading this file, scream cake."
echo "Seriously, we'll give you a hint to answer question if you scream cake."
sudo visudo
ls
sudo ifng
ifconfi
apt get moo
sudo apt get moo
sudo apt install moo
sudo apt-install moo
sudo apt-get install moo
lol Castro just failed at all these commands. Someone pat him on the back. 
I tried okay
history > history.txt
binwalk didyouthinkwedmakeiteasy.jpg 
clear
history
exit
touch keys.txt
pwd

```
</details>
- Có thể thấy rằng 1 file SuperSecretFile được tạo ra tại dòng 

```
shutdown now
touch snky snky > /root/Desktop/SuperSecretFile.txt
cat snky snky > /root/Desktop/SuperSecretFile.txt 
msfconsole 
```
- 1 file SuperSecretFile.txt được tạo ra tại `/root/Desktop/SuperSecretFile.txt`
> A : /root/Desktop/SuperSecretFile.txt

- **What program used didyouthinkwedmakeiteasy.jpg during execution?**
- Tiếp tục quan sát file .bash_history
- Tại dòng `binwalk didyouthinkwedmakeiteasy.jpg ` có thể thấy rằng công cụ được sử dụng là binwalk
> A : binwalk

- **What is the third goal from the checklist Karen created?**
- Tại Desktop ta có 1 danh sách của Karen

```
Check List:

- Gain Bob's Trust
- Learn how to hack
- Profit

```
> A : Profit

- **How many times was apache run?**
- Dựa vào câu hỏi chắc chắn ta phải kiểm tra log apache tại `/var/log/apache2` nhưng 3 file apache2 đều có dung lượng là 0 byte nên rất có thể apache chưa chạy lần nào 
- Để thử phán đoán brute force đáp án (0=> 9)
> A : 0

- **It is believed this machine was used to attack another. What file proves this?**
- Tại /root có 1 ảnh tên `irZLAohL.jpeg`, trong ảnh chứa 1 lệnh cmd đang chạy tệp aylmao.exe. Đọc description ta thấy rằng nó tạo ra 1 lưu lượng độc hại để nhà bảo mật đánh giá mạng.
> A: irZLAohL.jpeg

- **Within the Documents file path, it is believed that Karen was taunting a fellow computer expert through a bash script. Who was Karen taunting?**
- Đây là nội dung file fistscript 
```
echo "Showing you your current path"
pwd
echo "Show my default route"
ip route | grep --color default
echo "Show network connections w/ port 80"
netstat | grep --color 80
echo "Heck yeah! I can write bash too Young"
```
> A: Young

- **A user su'd to root at 11:26 multiple times. Who was it?**
- Với câu hỏi này chỉ cần kiểm tra phần log auth.log là có đáp án 
- Tìm kiếm theo dấu thời gian là 11:26
- `Mar 20 11:26:22 KarenHacker su[4074]: + ??? root:postgres`
> A : postgres




- **Based on the bash history, what is the current working directory?**
- Quay lại tệp bash history, để biết đang làm việc tại thư mục nào chỉ cần quan tâm đến các lệnh `cd`

```
cd ../Documents/myfirsthack/
netstat
echo bob.txt
touch bob.txt 
echo "If you're still reading this file, scream cake."
echo "Seriously, we'll give you a hint to answer question if you scream cake."
sudo visudo
ls
sudo ifng
ifconfi
apt get moo
sudo apt get moo
sudo apt install moo
sudo apt-install moo
sudo apt-get install moo
lol Castro just failed at all these commands. Someone pat him on the back. 
I tried okay
history > history.txt
binwalk didyouthinkwedmakeiteasy.jpg 
clear
history
exit
touch keys.txt
pwd
```
- Thấy rằng user di chuyển đến /Documents/myfirsthack/ rồi không di chuyển nữa
> A : /root/Documents/myfirsthack/