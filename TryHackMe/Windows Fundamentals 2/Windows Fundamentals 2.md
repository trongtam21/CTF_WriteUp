## Lab 
> https://tryhackme.com/room/windowsfundamentals2x0x
## Giải 
### Task 2  System Configuration
- Câu 1 : What is the name of the service that lists Systems Internals as the manufacturer?
- Dựa vào hộp thoại services để tìm 
- ![image](image/3.PNG)
> PsShutdown
- Câu 2 : Whom is the Windows license registered to?
- Để xem được Windows license em chuyển đến tool > launch
- ![image](image/4.PNG)
- ![image](image/5.PNG)
> Windows user
- Câu 3 : What is the command for Windows Troubleshooting?
- Để tìm được lệnh khắc phục sự cố ta phải vào` Troubleshooting` ở phần tool 
- ![image](image/2.PNG)
> C:\Windows\System32\control.exe /name Microsoft.Troubleshooting
- Câu 4 : What command will open the Control Panel? (The answer is  the name of .exe, not the full path)
- Để tìm được command để mở `Control Panel`, em vào hộp thoại `tool > system properties`
- ![image](image/1.PNG)
> control.exe
### Task 3 :  Change UAC Settings
- Câu 1 : What is the command to open User Account Control Settings? (The answer is the name of the .exe file, not the full path)
- ![image](image/6.PNG)
> UserAccountControlSettings.exe
### Task 4 :  Computer Management
- Câu 1 : 