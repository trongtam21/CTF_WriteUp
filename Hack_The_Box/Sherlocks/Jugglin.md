## Description
> Forela Corporation heavily depends on the utilisation of the Windows Subsystem for Linux (WSL), and currently, threat actors are leveraging this feature, taking advantage of its elusive nature that makes it difficult for defenders to detect. In response, the red team at Forela has executed a range of commands using WSL2 and shared API logs for analysis.

## Solution
- Bài này cung cấp cho chúng ta 2 file apmx64. Theo như tìm hiểu đây là file liên quan đến API Monitor , một phần mềm giám sát và kiểm soát các lệnh call API được thực hiện bởi các ứng dụng và dịch vụ.
- Tại đây ta sẽ có 2 cách là sử dụng công cụ API Monitor hoặc cách khác là giải nén và đọc data trong từng file (Ưu tiên cách 1 hơn vì ta có thể nhìn được tổng quan về các API được gọi)
### 1. What was the initial command executed by the insider?
- Mở file `Insider.apmx64` với API Monitor. Ta thấy có 2 process đang chạy : wsl và windows powershell
- ![image](https://hackmd.io/_uploads/Sy72Ww2-Jl.png)
- Bắt đầu với process wsl trước, nhìn vào thread ta thấy có 3 thread wsl được tạo
- ![image](https://hackmd.io/_uploads/HJheLOh-ye.png)
- Thử kiểm tra với 1 thread có số thứ tự là 2
```
Trong API của Windows, hàm WriteFile được sử dụng để ghi dữ liệu vào một tệp hoặc một đối tượng (như pipe hoặc cổng nối mạng) từ bộ đệm trong bộ nhớ.
Hàm ReadFile trong API của Windows được sử dụng để đọc dữ liệu từ một tệp, pipe, hoặc đối tượng I/O khác vào bộ đệm trong bộ nhớ.
```
- Quan sát hàm WriteFile, ta thấy có 1 vài kí tự được ghi vào,  ví dụ như:
```
#	Time of Day	Thread	Module	API	Return Value	Error	Duration
4	8:48:01.148 PM	2	wsl.exe	WriteFile ( 0x0000000000000054, 0x0000026828467bc0, 1, 0x00000079cfaff830, 0x00000079cfaff8e0 )	TRUE		0.0002643
```
- Với dòng trên ta thấy dữ liệu `0x0000000000000054` được ghi vào bộ đệm `0x0000026828467bc0`, ở đây ta đã được hỗ trợ trích xuất sẵn các kí tự 
- ![image](https://hackmd.io/_uploads/Sk5u3u3Zyg.png)
- Tương tự với các hàm WriteFile khác ta thu được command đầu tiên mà insider thực thi là `whoami`
- ![image](https://hackmd.io/_uploads/Bk2had3-Jl.png)
- ![image](https://hackmd.io/_uploads/B1F6p_nZyl.png)
- ![image](https://hackmd.io/_uploads/S1XRad3bke.png)
- ![image](https://hackmd.io/_uploads/S1O1C_nWJg.png)
- ![image](https://hackmd.io/_uploads/r1UyAOnWJx.png)
### 2. Which string function can be intercepted to monitor keystrokes by an insider?
- Dựa ào nguồn này : https://www.hackthebox.com/blog/tracking-wsl-activity-with-api-hooking ta thấy 1 vài thông tin liên quan 
- ![image](https://hackmd.io/_uploads/rJeC-sTZ1x.png)
> RtlUnicodeToUTF8N, WideCharToMultiByte
### 3. Which Linux distribution the insider was interacting with? 
- Ngay sau khi chạy lệnh whoami đầu ra của lệnh là kali 
- ![image](https://hackmd.io/_uploads/B18f_6pZ1e.png)

> kali 

### 4. Which file did the insider access in order to read its contents?
- Tương tự như câu hỏi thứ 1 ta tiếp tục theo dõi các hàm WriteFile, ta thấy sau khi dùng lệnh `cd desktop`, insider tiến hành `cat flag.txt` để đọc nội dung của nó (bắt đầu từ số thứ tự 208).
- ![image](https://hackmd.io/_uploads/HkS-Ac2bJl.png)
- ![image](https://hackmd.io/_uploads/rJGM053Wye.png)
- ![image](https://hackmd.io/_uploads/rk0fC93WJe.png)
- ![image](https://hackmd.io/_uploads/Hky4R92bye.png)
- ![image](https://hackmd.io/_uploads/Hy6V05n-Jg.png)
- ![image](https://hackmd.io/_uploads/HyuB092b1e.png)
- ![image](https://hackmd.io/_uploads/SkX8C9nZ1g.png)
- ![image](https://hackmd.io/_uploads/S1evAchZke.png)
- ![image](https://hackmd.io/_uploads/B19vCq3Zkg.png)
- ![image](https://hackmd.io/_uploads/SyHuRq3-1e.png)
- ![image](https://hackmd.io/_uploads/HJp_0chWyx.png)

> flag.txt

### 5. Submit the first flag.

- Cuộn xuông đến số thứ tự thứ 270 ta tìm thấy output (đây là dữ liệu sau khi `cat flag.txt`)
- ![image](https://hackmd.io/_uploads/r1dOeinWye.png)

> HOOK_tH1$_apI_R7lUNIcoDet0utf8N

### 6. Which PowerShell module did the insider utilize to extract data from their machine?

- Cuộn xuống đến dòng số 282, ta thấy 8 byte được viết
```
#	Time of Day	Thread	Module	API	Return Value	Error	Duration
282	8:57:56.202 PM	2	wsl.exe	WriteFile ( 0x0000000000000054, 0x0000026828467bc0, 8, 0x00000079cfaff830, 0x00000079cfaff8e0 )	TRUE		0.0003133
```
- ![image](https://hackmd.io/_uploads/HyPNZi3-kl.png)
- Đây chính là 1 lệnh powershell. Ta sẽ tìm chuỗi này bằng CMD trong file data đã giải nén
- ![image](https://hackmd.io/_uploads/Skt1zohbyl.png)
- Ta thấy rằng 1 lệnh powershell sử dụng Invoke-WebRequest gửi file confidential.txt đến http://3.6.165.8

> Invoke-WebRequest

### 7. Which string function can be intercepted to monitor the usage of Windows tools via WSL by an insider?

> RtlUTF8ToUnicodeN

### 8. The insider has also accessed 'confidential.txt'. Please provide the second flag for submission.

- Tiếp tục tìm với CMD, ta thấy 1 lệnh cat cat: 'C:confidential.txt' được thực hiện nhưng không thành công
- ![image](https://hackmd.io/_uploads/rJgmSo3bkg.png)
- Cuộn xuống ta tiếp tục thấy cat tại `/mnt/c/a/confidential.txt` thì có flag
- ![image](https://hackmd.io/_uploads/rynqHi2bJe.png)
- ![image](https://hackmd.io/_uploads/S1NRHinZ1e.png)

> H0ok_ThIS_@PI_rtlutf8TounICOD3N

### 9. Which command executed by the attacker resulted in a 'not found' response?
- Đến với file `Attacker.apmx64`, ta phân tích tương tự file insider.apmx64.
- ![image](https://hackmd.io/_uploads/BJJY8j3Zyg.png)
- ![image](https://hackmd.io/_uploads/SJvbDs2Wyg.png)

> lsassy

### 10. Which link was utilized to download the 'lsassy' binary?
- ![image](https://hackmd.io/_uploads/BywVDj2W1l.png)
> http://3.6.165.8/lsassy
### 11. What is the SHA1 hash of victim 'user' ?
- ![image](https://hackmd.io/_uploads/By3Dwjn-kl.png)

> e8f97fba9104d1ea5047948e6dfb67facd9f5b73

### 12. When an attacker utilizes WSL2, which WIN32 API would you intercept to monitor its behavior?
- Từ các phân tích của các câu trả lời phía trên ta có thể dễ dàng quan sát các API WriteFile để theo dõi hành vi của kẻ tấn công.

> WriteFile

## Resource 
- https://www.hackthebox.com/blog/tracking-wsl-activity-with-api-hooking
## Result

- ![image](https://hackmd.io/_uploads/HJ5j9a6Wkx.png)
