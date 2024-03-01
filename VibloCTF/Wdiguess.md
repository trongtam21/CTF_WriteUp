## Đề 
> Attacker considers this file as treasure, why and what does it contain?
## Link challenge
> https://ctf.viblo.asia/puzzles/wdiguess-rqjsfadoot9
## Giải 
- Sau khi tải file em sử dụng lệnh file trước để kiểm tra
```
┌──(kali㉿kali)-[~/Downloads]
└─$ file lsass.DMP 
lsass.DMP: Mini DuMP crash report, 12 streams, Thu Nov  3 16:55:57 2022, 0x1826 type
``` 
- Em xác định được đây là file minidump, cộng thêm tên file có vẻ đáng ngờ nên em tìm hiểu luôn 
```
Local Security Authority Server Service (LSASS) là một tiến trình trong hệ điều hành Microsoft Windows chịu trách nhiệm thực thi chính sách bảo mật trên hệ thống. Nó xác minh người dùng đăng nhập vào máy tính hoặc máy chủ Windows, xử lý các thay đổi mật khẩu và tạo mã thông báo truy cập. Nó tạo mã thông báo bảo mật cho SAM (Trình quản lý tài khoản bảo mật), AD (Thư mục hoạt động) và NETLOGON. Nó sử dụng các gói xác thực được chỉ định trong HKLM\System\CurrentControlSet\Control\Lsa.
```
- Sau 1 vài lần search google, em sử dụng  PyPyKatz để phân tích tệp dmp trên linux
> pip3 install pypykatz
- Khi tải xuống và chạy lệnh em thu được flag
```
                                                                                                                                                                  
┌──(kali㉿kali)-[~/Downloads]
└─$ pypykatz lsa minidump lsass.DMP
INFO:pypykatz:Parsing file lsass.DMP
FILE: ======== lsass.DMP =======
== LogonSession ==
authentication_id 298761 (48f09)
session_id 1
username TommyXiaomi
domainname WIN-E986B90RO3G
logon_server WIN-E986B90RO3G
logon_time 2022-11-03T16:54:21.666492+00:00
sid S-1-5-21-1855374324-2022565409-2304591112-1000
luid 298761
        == MSV ==
                Username: TommyXiaomi
                Domain: WIN-E986B90RO3G
                LM: NA
                NT: 0ba7947eb506da39efbb5f133da3402e
                SHA1: a0e5c7735f1436b33effcbbfc459c06da974b529
                DPAPI: NA
        == MSV ==
                Username: NA
                Domain: NA
                LM: NA
                NT: 0ba7947eb506da39efbb5f133da3402e
                SHA1: a0e5c7735f1436b33effcbbfc459c06da974b529
                DPAPI: NA
        == WDIGEST [48f09]==
                username TommyXiaomi
                domainname WIN-E986B90RO3G
                password Flag{Ls4s5_duMp3r_M4st3R}
                password (hex)46006c00610067007b004c0073003400730035005f00640075004d007000330072005f004d00340073007400330052007d00000000000000
        == Kerberos ==
                Username: TommyXiaomi
                Domain: WIN-E986B90RO3G
        == WDIGEST [48f09]==
                username TommyXiaomi
                domainname WIN-E986B90RO3G
                password Flag{Ls4s5_duMp3r_M4st3R}
                password (hex)46006c00610067007b004c0073003400730035005f00640075004d007000330072005f004d00340073007400330052007d00000000000000

== LogonSession ==
authentication_id 298727 (48ee7)
session_id 1
username TommyXiaomi
domainname WIN-E986B90RO3G
logon_server WIN-E986B90RO3G
logon_time 2022-11-03T16:54:21.619692+00:00
sid S-1-5-21-1855374324-2022565409-2304591112-1000
luid 298727
        == MSV ==
                Username: NA
                Domain: NA
                LM: NA
                NT: 0ba7947eb506da39efbb5f133da3402e
                SHA1: a0e5c7735f1436b33effcbbfc459c06da974b529
                DPAPI: NA
        == MSV ==
                Username: TommyXiaomi
                Domain: WIN-E986B90RO3G
                LM: NA
                NT: 0ba7947eb506da39efbb5f133da3402e
                SHA1: a0e5c7735f1436b33effcbbfc459c06da974b529
                DPAPI: NA
        == WDIGEST [48ee7]==
                username TommyXiaomi
                domainname WIN-E986B90RO3G
                password Flag{Ls4s5_duMp3r_M4st3R}
                password (hex)46006c00610067007b004c0073003400730035005f00640075004d007000330072005f004d00340073007400330052007d00000000000000
        == Kerberos ==
                Username: TommyXiaomi
                Domain: WIN-E986B90RO3G
        == WDIGEST [48ee7]==
                username TommyXiaomi
                domainname WIN-E986B90RO3G
                password Flag{Ls4s5_duMp3r_M4st3R}
                password (hex)46006c00610067007b004c0073003400730035005f00640075004d007000330072005f004d00340073007400330052007d00000000000000

== LogonSession ==
authentication_id 119021 (1d0ed)
session_id 0
username ANONYMOUS LOGON
domainname NT AUTHORITY
logon_server 
logon_time 2022-11-03T16:53:52.229240+00:00
sid S-1-5-7
luid 119021

== LogonSession ==
authentication_id 997 (3e5)
session_id 0
username LOCAL SERVICE
domainname NT AUTHORITY
logon_server 
logon_time 2022-11-03T16:53:45.646028+00:00
sid S-1-5-19
luid 997
        == Kerberos ==
                Username: 
                Domain: 

== LogonSession ==
authentication_id 996 (3e4)
session_id 0
username WIN-E986B90RO3G$
domainname WORKGROUP
logon_server 
logon_time 2022-11-03T16:53:45.505628+00:00
sid S-1-5-20
luid 996
        == WDIGEST [3e4]==
                username WIN-E986B90RO3G$
                domainname WORKGROUP
                password None
                password (hex)
        == Kerberos ==
                Username: win-e986b90ro3g$
                Domain: WORKGROUP
        == WDIGEST [3e4]==
                username WIN-E986B90RO3G$
                domainname WORKGROUP
                password None
                password (hex)

== LogonSession ==
authentication_id 48828 (bebc)
session_id 0
username 
domainname 
logon_server 
logon_time 2022-11-03T16:53:41.792822+00:00
sid None
luid 48828

== LogonSession ==
authentication_id 999 (3e7)
session_id 0
username WIN-E986B90RO3G$
domainname WORKGROUP
logon_server 
logon_time 2022-11-03T16:53:41.465221+00:00
sid S-1-5-18
luid 999
        == WDIGEST [3e7]==
                username WIN-E986B90RO3G$
                domainname WORKGROUP
                password None
                password (hex)
        == Kerberos ==
                Username: win-e986b90ro3g$
                Domain: WORKGROUP
        == WDIGEST [3e7]==
                username WIN-E986B90RO3G$
                domainname WORKGROUP
                password None
                password (hex)
        == DPAPI [3e7]==
                luid 999
                key_guid f22e410f-f947-4e08-8f2a-8f65df603f8d
                masterkey 19c05880b67d50f8231cd8009836e3cdc55610e4877f8b976abd5ca15600d0e759934324c6204b56f02527039e7fc52a1dfb5296d3381aaa7c3eb610dffa32fa
                sha1_masterkey b859b2b52e7e49cf5c70069745c88853c4b23487
```
> Flag : Flag{Ls4s5_duMp3r_M4st3R}