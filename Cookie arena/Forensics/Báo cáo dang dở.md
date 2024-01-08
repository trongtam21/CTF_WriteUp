## Đề 
> Hòa đang làm báo cáo bài tập lớn để nộp cho thầy giáo thì bỗng nhiên máy tính của anh ấy bị tắt đột ngột do mất điện mà anh ấy thì chưa kịp lưu báo cáo một lần nào. Tuy nhiên sau đó, thay vì viết báo cáo mới thì Hòa đã chọn cách dành ra 4h đồng hồ để khôi phục báo cáo ban đầu từ tệp crash dump nhưng cuối cùng vẫn thất bại. Hòa thực sự đang cần trợ giúp
## Link 
> https://drive.google.com/file/d/19OCHSjzHmzFBoSLYB90nkrZLnREpZ1nG/view?usp=drive_link
> pass : cookiehanhoan
## Giải 
- Sau khi tải và giải nén em thu được file `memory.dmp`
- Em lựa chọn sử dụng công cụ volatility3 để phân tích
- Trước tiên em tiến hành kiểm tra các process đang chạy
> python3 /home/trongtam/volatility3/vol.py -f MEMORY.DMP windows.pstree.PsTree
```text
Volatility 3 Framework 2.5.2
Progress:  100.00               PDB scanning finished                                
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime

4       0       System  0xfa80024bb840  90      512     N/A     False   2023-05-31 18:18:24.000000      N/A
* 268   4       smss.exe        0xfa8002c5e400  2       30      N/A     False   2023-05-31 18:18:24.000000      N/A
356     340     csrss.exe       0xfa80037e7060  9       451     0       False   2023-05-31 18:18:26.000000      N/A
440     340     wininit.exe     0xfa8003a68060  3       79      0       False   2023-05-31 18:18:26.000000      N/A
* 528   440     services.exe    0xfa8003ab7810  7       207     0       False   2023-05-31 18:18:26.000000      N/A
** 768  528     svchost.exe     0xfa8003bd3b30  9       292     0       False   2023-05-31 18:18:27.000000      N/A
** 2564 528     SearchIndexer.  0xfa80045344a0  13      616     0       False   2023-05-31 18:18:34.000000      N/A
** 1544 528     VGAuthService.  0xfa8003f23b30  3       85      0       False   2023-05-31 18:18:28.000000      N/A
** 1288 528     svchost.exe     0xfa8004087060  5       103     0       False   2023-05-31 18:18:29.000000      N/A
** 2956 528     OSPPSVC.EXE     0xfa8003fcab30  3       129     0       False   2023-05-31 18:20:19.000000      N/A
** 400  528     svchost.exe     0xfa8003cb24b0  12      542     0       False   2023-05-31 18:18:27.000000      N/A
** 1684 528     vmtoolsd.exe    0xfa8003f6f200  9       293     0       False   2023-05-31 18:18:28.000000      N/A
** 924  528     svchost.exe     0xfa8003c52b30  16      377     0       False   2023-05-31 18:18:27.000000      N/A
*** 1340        924     dwm.exe 0xfa8003e38b30  5       124     1       False   2023-05-31 18:18:28.000000      N/A
** 672  528     svchost.exe     0xfa8003b6e3c0  10      356     0       False   2023-05-31 18:18:27.000000      N/A
*** 1316        672     WmiPrvSE.exe    0xfa8004b03060  10      211     0       False   2023-05-31 18:18:29.000000      N/A
*** 2844        672     WmiPrvSE.exe    0xfa80045b8530  10      239     0       False   2023-05-31 18:18:49.000000      N/A
** 1916 528     svchost.exe     0xfa8003f83b30  12      321     0       False   2023-05-31 18:20:29.000000      N/A
** 952  528     svchost.exe     0xfa8003c613a0  42      1036    0       False   2023-05-31 18:18:27.000000      N/A
** 1472 528     taskhost.exe    0xfa8003ea8410  8       145     1       False   2023-05-31 18:18:28.000000      N/A
** 856  528     svchost.exe     0xfa8003ce3b30  15      364     0       False   2023-05-31 18:18:27.000000      N/A
** 2136 528     dllhost.exe     0xfa8004b05b30  15      207     0       False   2023-05-31 18:18:29.000000      N/A
** 1116 528     spoolsv.exe     0xfa8003d6f250  15      338     0       False   2023-05-31 18:18:27.000000      N/A
** 732  528     vmacthlp.exe    0xfa8003b9fb30  3       56      0       False   2023-05-31 18:18:27.000000      N/A
** 868  528     svchost.exe     0xfa8003c18060  20      480     0       False   2023-05-31 18:18:27.000000      N/A
*** 2484        868     audiodg.exe     0xfa8003c83b30  6       136     0       False   2023-05-31 18:26:32.000000      N/A
** 2792 528     svchost.exe     0xfa8003c86920  5       74      0       False   2023-05-31 18:20:18.000000      N/A
** 2288 528     msdtc.exe       0xfa8004480b30  14      154     0       False   2023-05-31 18:18:30.000000      N/A
** 1148 528     svchost.exe     0xfa8003d91b30  19      316     0       False   2023-05-31 18:18:27.000000      N/A
* 564   440     lsass.exe       0xfa8003aeab30  9       570     0       False   2023-05-31 18:18:26.000000      N/A
* 572   440     lsm.exe 0xfa8003aec810  10      144     0       False   2023-05-31 18:18:26.000000      N/A
460     448     csrss.exe       0xfa8003a67060  10      231     1       False   2023-05-31 18:18:26.000000      N/A
520     448     winlogon.exe    0xfa8003ab6700  3       111     1       False   2023-05-31 18:18:26.000000      N/A
1372    1304    explorer.exe    0xfa8003e64960  39      1058    1       False   2023-05-31 18:18:28.000000      N/A
* 1928  1372    vmtoolsd.exe    0xfa800407db30  6       186     1       False   2023-05-31 18:18:29.000000      N/A
* 1736  1372    WINWORD.EXE     0xfa8003a6e060  13      443     1       False   2023-05-31 18:20:18.000000      N/A
1076    2228    taskmgr.exe     0xfa8004103b30  9       121     1       False   2023-05-31 18:27:43.000000      N/A
                                                                                                                                
```
- Vì đề liên quan đến bài tập lớn nên ta tập trung vào các process liên quan thôi
- Ở đây ta thấy process `WINWORD.EXE`với pid là `1736`
- Để dump file ra xem có gì không
- Ta có 2 sự lựa chọn
```text
windows.dumpfiles.DumpFiles
                        Dumps cached file contents from Windows memory samples.
windows.handles.Handles
                        Lists process open handles.

```
> python3 /home/trongtam/volatility3/vol.py -f MEMORY.DMP windows.dumpfiles.DumpFiles --pid 1736
- Sau khi dump file em thu được rất nhiều file *.image
- Kiểm tra 1 lượt thì có 1 số file office
```text
┌──(trongtam㉿kali)-[~/Downloads/arenas2-forensics-bao-cao-dang-do]
└─$ file file.0xfa8004639390.0xfa8003d7b6d0.DataSectionObject.~WRD0000.tmp.dat
file.0xfa8004639390.0xfa8003d7b6d0.DataSectionObject.~WRD0000.tmp.dat: Composite Document File V2 Document, Little Endian, Os: Windows, Version 6.1, Code page: 1252, Author: admin, Template: Normal, Revision Number: 1, Name of Creating Application: Microsoft Office Word, Total Editing Time: 06:00, Create Time/Date: Sun Apr 30 18:20:00 2023, Number of Pages: 3, Number of Words: 136, Number of Characters: 778, Security: 0
```
- Giờ vấn đề là làm sao đọc được nó   
- Dùng `strings file.0xfa8004639390.0xfa8003d7b6d0.DataSectionObject.~WRD0000.tmp.dat` xem thử.
```text
IEND
[Content_Types].xmlPK
_rels/.relsPK
word/drawings/drawing1.xmlPK
word/drawings/_rels/drawing1.xml.relsPK
word/media/image2.pngPK
word/media/image1.pngPK
```       
- Em thấy trong này có 1 vài file ẩn nên dùng binwalk để xuất nó ra    
> binwalk -e file.0xfa8004639390.0xfa8003d7b6d0.DataSectionObject.~WRD0000.tmp.dat
- Sau khi extract em tiến hành check xem có gì không 
- Em thấy 2 ảnh, 1 ảnh logo KMA, 1 ảnh Cookie han hoan chứa flag
> Flag : CHH{4ut0R3c0v3r_s4v3_my_l1f3}
                                                                                
