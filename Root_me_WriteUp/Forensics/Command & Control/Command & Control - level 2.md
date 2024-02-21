## Đề 
Congratulations Berthier, thanks to your help the computer has been identified. You have requested a memory dump but before starting your analysis you wanted to take a look at the antivirus’ logs. Unfortunately, you forgot to write down the workstation’s hostname. But since you have its memory dump you should be able to get it back!

The validation flag is the workstation’s hostname.
## Link chall
> https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-2
## Giải 
- Để xác định được tên máy ý tưởng của em là dựa vào các registry được lưu tại `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName`
- Thứ nhất em in ra các key của registry xem thử nó có gì
```
┌──(kali㉿kali)-[~/volatility3]
└─$ python3 vol.py -f /home/kali/Downloads/ch2.dmp windows.registry.printkey                                                        
Volatility 3 Framework 2.5.2
Progress:  100.00               PDB scanning finished                        
Last Write Time Hive Offset     Type    Key     Name    Data    Volatile

2013-01-12 16:37:53.000000      0x8b20c008      Key     [NONAME]        A               False
2013-01-12 16:38:21.000000      0x8b20c008      Key     [NONAME]        MACHINE         False
2013-01-12 16:40:23.000000      0x8b20c008      Key     [NONAME]        USER            False
2013-01-12 00:58:47.000000      0x8b21c008      Key     \REGISTRY\MACHINE\SYSTEM        ControlSet001           False
2009-07-14 04:53:14.000000      0x8b21c008      Key     \REGISTRY\MACHINE\SYSTEM        ControlSet002           False
...
```
- Tại 2 offset dưới em thấy được 1 số đường dẫn registry mà ban đầu đã xác định
- Tiếp theo em dùng option --key để tìm `ControlSet001\Control\ComputerName\ComputerName` và tìm tên máy 
```
┌──(kali㉿kali)-[~/volatility3]
└─$ python3 vol.py -f /home/kali/Downloads/ch2.dmp windows.registry.printkey --key "ControlSet001\Control\ComputerName\ComputerName" --offset 0x8b21c008
Volatility 3 Framework 2.5.2
Progress:  100.00               PDB scanning finished                        
Last Write Time Hive Offset     Type    Key     Name    Data    Volatile

2013-01-12 00:58:30.000000      0x8b21c008      REG_SZ  \REGISTRY\MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName        (Default)       "mnmsrvc"    False
2013-01-12 00:58:30.000000      0x8b21c008      REG_SZ  \REGISTRY\MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName        ComputerName    "WIN-ETSA91RKCFP"     False
```
- Có thể thấy được giá trị của ComputerName là `WIN-ETSA91RKCFP`
> Flag : WIN-ETSA91RKCFP
