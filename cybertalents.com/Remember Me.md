## Description 
> After acquiring memory from attacker pc we found there is no internet browser except internet explorer . Can you get internet history? 
## Link challenge 
> https://cybertalents.com/challenges/forensics/remember-me
## Solution
- Sau khi tải file memory dump xuống em phân tích nó bằng volatility
- Như 1 thói quen, dùng pslist để scan các process trước 
- Vì description có mô tả rằng ta cần phải đọc được history browser của `internet explorer` nên em sử dụng plugin iehistory
- `iehistory       Reconstruct Internet Explorer cache / history`
- Tại lịch sử tìm kiếm liên tục là những chuỗi base64 
```
Process: 1424 explorer.exe
Cache type "URL " at 0x1d85880
Record length: 0x180
Location: Visited: John the ripper@http://www.bing.com/search?format=rss&q=ZmxhZ3tLZWVwX3VzaW5nX3ZvbGF0aWxpdHl9&qs=ds&form=QBRE
Last modified: 2020-01-20 16:39:29 UTC+0000
Last accessed: 2020-01-20 16:39:29 UTC+0000
File Offset: 0x180, Data Offset: 0x0, Data Length: 0xe0
**************************************************
Process: 1424 explorer.exe
Cache type "URL " at 0x1d85a00
Record length: 0x180
Location: Visited: John the ripper@http://www.bing.com/search?q=bing&src=IE-SearchBox&FORM=IE8SRC
Last modified: 2020-01-20 16:39:40 UTC+0000
Last accessed: 2020-01-20 16:39:40 UTC+0000
File Offset: 0x180, Data Offset: 0x0, Data Length: 0xc0
**************************************************
Process: 1424 explorer.exe
Cache type "URL " at 0x1d85b80
Record length: 0x200
Location: Visited: John the ripper@https://www.google.com/search?q=ZmxhZ3tLZWVwX3VzaW5nX3ZvbGF0aWxpdHl9&hl=ar&gbv=1&source=lnms&tbm=vid&sa=X&ved=0ahUKEwjo5-3uzpLnAhUhyIUKHci4BkUQ_AUIBSgB
Last modified: 2020-01-20 16:39:40 UTC+0000
Last accessed: 2020-01-20 16:39:40 UTC+0000
File Offset: 0x200, Data Offset: 0x0, Data Length: 0x11c
**************************************************
Process: 1424 explorer.exe
Cache type "URL " at 0x1d85d80
Record length: 0x200
Location: Visited: John the ripper@https://www.google.com/search?q=ZmxhZ3tLZWVwX3VzaW5nX3ZvbGF0aWxpdHl9&hl=ar&gbv=1&tbm=isch&source=lnms&sa=X&ved=0ahUKEwicxM7wzpLnAhUPyYUKHV8bByYQ_AUIBigC
Last modified: 2020-01-20 16:39:40 UTC+0000
Last accessed: 2020-01-20 16:39:40 UTC+0000
File Offset: 0x200, Data Offset: 0x0, Data Length: 0x11c
**************************************************

```
- Decode ra để lấy flag 
```
┌──(kali㉿kali)-[~/volatility]
└─$ echo "ZmxhZ3tLZWVwX3VzaW5nX3ZvbGF0aWxpdHl9" | base64 -d
flag{Keep_using_volatility}    
```

