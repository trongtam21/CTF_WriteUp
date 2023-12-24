## Đề 
> We found this packet capture. Recover the flag that was pilfered from the network.
## Link
> https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap
## Giải 
- Sau khi tải file pcap về tôi bắt đầu phân tích 
- Đầu tiên phân tích cái tệp tin được trao đổi, nhưng không có gì 
- Tiếp theo tôi kiểm tra luồng dữ liệu 
> TCP : Không có gì 
> UDP : Có 1 vài flag giả, và điểm chú ý là có start và end 
- Kiểm tra 2 gói start và end thì thấy lenght là 60 và port là 22, Nhưng thông tin gói đầu bắt đầu và kết thúc bằng 5000
- Ở gói tiếp theo của gói start là 5112 nếu 112 đổi qua ascii thì nó là p
- Lấy 3 chữ số cuối sau đó đổi nó qua ascii
- Filter đến port 22 trước 
- Tôi sẽ dùng tshark để lưu nó vào 1 tệp cho dễ xử lý
```text
┌──(trongtam㉿kali)-[~/Downloads]
└─$ tshark -r capture.pcap -Y "udp.port == 22" > file.txt    
```
- Tôi sẽ dùng 1 đoạn code py để tách 3 chữ số cuối ra
```text
file = open("file.txt")
strings = ""
for line in file:
	#print(line[52:55]) debug
	strings = strings + chr(int(line[52:55]))
print(strings)
```
- Kết quả 
> icoCTF{p1LLf3r3d_data_v1a_st3g0}
- Do chữ p đằng trước bị thụt vô 1 hàng nên dữ liệu đầu ra không chính xác, nhưng cứ thêm p vào là được 
> Flag : picoCTF{p1LLf3r3d_data_v1a_st3g0}
