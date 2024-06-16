pip3 install pycryptodome
## Lab 
> https://tryhackme.com/room/autopsy2ze0
## Giải
### What is the MD5 hash of the E01 image?
- Để trả lời được câu hỏi này ta truy cập vào file `HANSAN2.txt`
- ![image](image/1.PNG)
- Kéo xuống, lần lượt thu được các thông tin về file cần phân tích
> 3f08c518adb3b5c1359849657a9b2079
### What is the computer account name?
- Thông tin account được lưu tại 
- ![image](image/2.PNG)
> DESKTOP-0R59DJ3	
### List all the user accounts. (alphabetical order)
- Lấy tất cả các user của hệ thống tại 
- ![image](image/3.PNG)
> H4S4N,joshwa,keshav,sandhya,shreya,sivapriya,srini,suba
### Who was the last user to log into the computer?
- Để xác định được người cuối cùng đăng nhập vào máy tính, em sẽ tiến hành kiểm tra thời gian truy cập 
- ![image](image/4.PNG)
> sivapriya	
### What was the IP address of the computer?
- IP của máy em tìm thấy tại path `Program Files (x86) > Look@LAN > irunin.ini`, đây là nơi lưu các thông tin về local network
- ![image](image/5.PNG)
> 192.168.130.216
### What was the MAC address of the computer? (XX-XX-XX-XX-XX-XX)
- Địa chỉ mac chính là giá trị của LAN IC
- ![image](image/5.PNG)
> 08-00-27-2c-c4-b9
### What is the name of the network card on this computer?
- Để lấy được name của card mạng em sẽ dựa vào các hives của registry
-  Đường dẫn chứa các thôg tin hệ thống nằm ở sofware
- Truy cập tại `ROOT/Microsoft/Windows NT/CurrentVersion/NetworkCards/2`
- ![image](image/7.PNG)
- ![image](image/8.PNG)
>Intel(R) PRO/1000 MT Desktop Adapter
### What is the name of the network monitoring tool?
- Để biết được em sẽ xem phần chương trình đã chạy , sau đó tìm các phần mềm liên quan
- ![image](image/9.PNG)
> LOOK@LAN	
### A user bookmarked a Google Maps location. What are the coordinates of the location?
- Muốn biết vị trí đã đánh dấu ta cần try cập web bookmarked để xem 
- ![image](image/6.PNG)
> 12°52'23.0"N 80°13'25.0"E
### A user has his full name printed on his desktop wallpaper. What is the user's full name?
- Em sẽ kiểm tra ảnh trên máy trước
- ![image](image/11.PNG)
- Tại folder Downloads của user joshwa có 1 ảnh khả nghi, vì quá nhỏ nên em phải extract ra mới xem được chữ
- ![image](image/12.PNG)
- ![image](image/13.PNG)
> anto joshwa
### A user had a file on her desktop. It had a flag but she changed the flag using PowerShell. What was the first flag?
- Đầu tiên em truy cập vào lịch sử PowerShell trước 
- Em sẽ kiểm tra lần lượt lịch sử PS từng user tại địa chỉ `Users > 'username' > AppData > Roaming > Microsoft > Windows > PowerShell` thì tại user shreya ta có được flag 
- ![image](image/10.PNG)
> flag{HarleyQuinnForQueen}
### The same user found an exploit to escalate privileges on the computer. What was the message to the device owner?
- Để tìm được tin nhắn em bắt đầu từ bằng cách tìm lần lượt từng user (bắt đầu từ user shreya vì có sử dụng powershell)
- Đúng như dự đoán flag ở desktop 
- ![image](image/14.PNG)
> Flag{I-hacked-you}
### 2 hack tools focused on passwords were found in the system. What are the names of these tools? (alphabetical order)
- Nếu là công cụ hack thì khả năng cao sẽ bị windows Defender phát hiện
- ![image](image/15.PNG)
- ![image](image/16.PNG)
> Lazagne,Mimikatz
### There is a YARA file on the computer. Inspect the file. What is the name of the author?
- Mục tiêu sẽ là 1 file YARA, em kiểm tra tại các user. Tại user H4S4N sẽ có 1 file zip 
- ![image](image/17.PNG)
- Vào trong file zip ta có 1 file .yar
- ![image](image/18.PNG)
- ![image](image/19.PNG)
> Benjamin DELPY (gentilkiwi)
### One of the users wanted to exploit a domain controller with an MS-NRPC based exploit. What is the filename of the archive that you found? (include the spaces in your answer) 
- Hãy xem [exploit MS-NRPC là](https://cehvietnam.com/2020/10/29/ceh-v11-lab-zero-logon-attack/) gì ?
- Em nhận thấy rằng mục tài liệu gần đây có 1 file rất đáng nghi 
- ![image](image/20.PNG)
> 2.2.0 20200918 Zerologon encrypted.zip



