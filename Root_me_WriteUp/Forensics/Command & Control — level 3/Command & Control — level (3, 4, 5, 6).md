# Command & Control — level 3
## Đề 
> Berthier, the antivirus software didn’t find anything. It’s up to you now. Try to find the malware in the memory dump. The validation flag is the md5 checksum of the full path of the executable.
## Link challenge
> https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-3
## Giải
- Sau khi tải và giải nén, em sử dụng công cụ volatility để phân tích, như thường lệ em sử dụng plugin imageinfo để xem profile 
```
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/kali/Downloads/ch2.dmp)
                      PAE type : PAE
                           DTB : 0x185000L
                          KDBG : 0x82929be8L
          Number of Processors : 1
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0x8292ac00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2013-01-12 16:59:18 UTC+0000
     Image local date and time : 2013-01-12 17:59:18 +0100
```
- Tiếp theo em xem danh sách tiến trình hoạt động thì có 1 điểm lưu ý 
- ![image](image/1.PNG)
- Có thể thấy `cmd.exe` là tiến trình cha của `iexplore.exe` và `iexplore.exe` là tiến trình cha của `explorer.exe`
- Tiếp tục em xem consolelog của nó 
```
explorer.exe pid:   2548
Command line : C:\Windows\Explorer.EXE
************************************************************************
iexplore.exe pid:   2772
Command line : "C:\Users\John Doe\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\iexplore.exe" 
************************************************************************
cmd.exe pid:   3152
Command line : "C:\Windows\system32\cmd.exe" 
************************************************************************
cmd.exe pid:   1616
Command line : cmd.exe
************************************************************************
iexplore.exe pid:   1136
Command line : "C:\Program Files\Internet Explorer\iexplore.exe" 
************************************************************************
iexplore.exe pid:   3044
Command line : "C:\Program Files\Internet Explorer\iexplore.exe" SCODEF:1136 CREDAT:71937
************************************************************************
```
- Phân tích sâu hơn bằng consoles
- ![image](image/2.PNG)
- Có thể thấy cmd đang thực thi tcprelay.exe
- Vì flag yêu cầu mã hoá md5 đường dẫn gốc của file nên em encrypt đường dẫn `C:\Users\John Doe\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\iexplore.exe`
> Flag : 49979149632639432397b3a1df8cb43d
# Command & Control level 4
## Đề 
> Berthier, thanks to this new information about the processes running on the workstation, it’s clear that this malware is used to exfiltrate data. Find out the ip of the internal server targeted by the hackers!
## Link challenge 
> https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-4
## Giải 
- Vì challenge này liên quan đến việc tìm kiếm các ip và port nên em sẽ dùng plugin chính là netscan
- ![image](image/4.PNG)
- Ta thu được ip máy chủ là `192.168.1.66`
- Trước tiên ta đã có được 1 vài thông tin liên quan từ challenge trước, cmd.exe đang sử dụng tcprelay.exe và ip được bắt đầu bằng `192.168`
- Tiếp theo em dump các process đáng ngờ từ pid 2772 ra để dễ dàng kiểm tra 
```
┌──(kali㉿kali)-[~/volatility]
└─$ python2 vol.py -f /home/kali/Downloads/ch2.dmp --profile=Win7SP1x86_23418 memdump -p 2772 -D /home/kali/Downloads/dump
Writing iexplore.exe [  2772] to 2772.dmp
```
- Tiếp theo em tìm kiếm theo những thông tin đã có 
- ![image](image/3.PNG)
> 192.168.0.22:3389

# Command & Control - level 5
## Đề 
> Berthier, the malware seems to be manually maintened on the workstations. Therefore it’s likely that the hackers have found all of the computers’ passwords.
Since ACME’s computer fleet seems to be up to date, it’s probably only due to password weakness. John, the system administrator doesn’t believe you. Prove him wrong!

Find john password.
## Link challenge 
> https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-5
## Giải
- Để giải được challenge này em sử dụng plugin hashdump của công cụ vol3 
```
┌──(kali㉿kali)-[~/volatility3]
└─$ python3 vol.py -f /home/kali/Downloads/ch2.dmp windows.hashdump
Volatility 3 Framework 2.5.2
Progress:  100.00               PDB scanning finished                        
User    rid     lmhash  nthash

Administrator   500     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
Guest   501     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
John Doe        1000    aad3b435b51404eeaad3b435b51404ee        b9f917853e3dbf6e6831ecce60725930
                                                                                                                                                                      
┌──(kali㉿kali)-[~/volatility3]
└─$ python3 vol.py -f /home/kali/Downloads/ch2.dmp windows.hashdump > hash
```
- Tiếp theo em sẽ sử dụng john để bruteforce mật khẩu
```
┌──(kali㉿kali)-[~/volatility3]
└─$ sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash --format=NT
Using default input encoding: UTF-8
Loaded 2 password hashes with no different salts (NT [MD4 128/128 AVX 4x3])
Remaining 1 password hash
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
passw0rd         (John Doe)     
1g 0:00:00:00 DONE (2024-02-18 01:19) 50.00g/s 67200p/s 67200c/s 67200C/s dragons..phoebe
Warning: passwords printed above might not be all those cracked
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed. 
```
> Pass : passw0rd





