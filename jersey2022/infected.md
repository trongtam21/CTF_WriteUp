## Đề 
> A host on the network was infected with a remote access trojan. A memory image of the host can be found here.
The flag is the process name followed by the PID. Format jctf{processname.exe:1234}
## Link challenge 
> https://drive.google.com/drive/folders/1lFkHr1uDy6nBl9zqA6njsLQVqtoJOG04
## Solution
- Đầu tiên khi tải file về em dùng psslist để xem có process nào đáng chú ý không 
- Điều đáng chú ý có rất nhiều process `svchost.exe` đang chạy và có 1 vài cái process rất lạ nữa `vm3dservice.ex, fontdrvhost.ex, ...`
- Dựa vào đề, máy chủ bị chèn trojan vào. Em sẽ dựa vào plugin `malfind` để tìm các mã ẩn đáng ngờ được chèn vào 
```
Lệnh malfind giúp tìm mã/DLL ẩn hoặc được chèn trong bộ nhớ chế độ người dùng, dựa trên các đặc điểm như thẻ VAD (bộ nhớ ảo) và quyền của trang.

Lưu ý: malfind không phát hiện các DLL được đưa vào một tiến trình bằng cách sử dụng CreateRemoteThread->LoadLibrary. Các tệp DLL được chèn bằng kỹ thuật này không bị ẩn và do đó bạn có thể xem chúng bằng dlllist . Mục đích của malfind là định vị các tệp DLL mà các phương pháp/công cụ tiêu chuẩn không nhìn thấy
```
> python2 vol.py -f /home/kali/Downloads/infected.mem --profile=Win10x64_19041 malfind
```
Process: MsMpEng.exe Pid: 3896 Address: 0x1c6a3a60000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: PrivateMemory: 1, Protection: 6

0x000001c6a3a60000  56 57 53 55 41 54 41 55 41 56 41 57 48 83 ec 28   VWSUATAUAVAWH..(
0x000001c6a3a60010  4c 8d 3c 24 48 8b e9 48 8d b1 98 38 00 00 ff e2   L.<$H..H...8....
0x000001c6a3a60020  49 8d 67 28 41 5f 41 5e 41 5d 41 5c 5d 5b 5f 5e   I.g(A_A^A]A\][_^
0x000001c6a3a60030  c3 00 00 40 00 80 00 00 00 48 89 e9 48 b8 00 b6   ...@.....H..H...




Process: MsMpEng.exe Pid: 3896 Address: 0x1c6c15e0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: PrivateMemory: 1, Protection: 6

0x000001c6c15e0000  cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc   ................
0x000001c6c15e0010  cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc   ................
0x000001c6c15e0020  cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc   ................
0x000001c6c15e0030  cc 08 00 42 00 00 00 00 05 48 8b 45 20 48 89 c2   ...B.....H.E.H..




Process: MsMpEng.exe Pid: 3896 Address: 0x1c6c2810000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: PrivateMemory: 1, Protection: 6

0x000001c6c2810000  cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc   ................
0x000001c6c2810010  cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc   ................
0x000001c6c2810020  cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc   ................
0x000001c6c2810030  cc 09 00 34 00 09 00 01 05 ba fc ff ff ff 03 55   ...4...........U



Process: svchost.exe Pid: 7756 Address: 0xd00000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: PrivateMemory: 1, Protection: 6

0x0000000000d00000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x0000000000d00010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x0000000000d00020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x0000000000d00030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................



Process: svchost.exe Pid: 7756 Address: 0x24e0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: PrivateMemory: 1, Protection: 6

0x00000000024e0000  4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00   MZ..............
0x00000000024e0010  b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00   ........@.......
0x00000000024e0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x00000000024e0030  00 00 00 00 00 00 00 00 00 00 00 00 f0 00 00 00   ................


```
- Ngoài ra còn phần assembly code mà nó dài quá không thêm vô
- Sau khi phân tích em thấy được process `svchost.exe` pid là 7756 có 1 vài vấn đề
- Check với pslist pid này là tiến trình con của `cmd.exe`
- `0xffff858a8912d340 cmd.exe                1852   1196      2        0      1      0 2022-02-12 12:34:03 UTC+0000`
- `0xffff858a893fd080 svchost.exe            7756   1852      4        0      1      1 2022-02-12 12:52:03 UTC+0000` 
> Đây chính là flag ta cần tìm :  jctf{svchost.exe:7756}
