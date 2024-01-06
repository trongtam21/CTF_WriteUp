## Đề : 
> This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark.
## Link : 
> https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4
## Giải 
- Sau khi tải theo đường dẫn trên em thu được 1 file có tên là flag (4)
- Vì không có đuôi nên em vào cmd kiểm tra loại file trước `pcapng capture file - version 1.0` đây đúng là file pcapng rồi
- Xác định được loại file rồi thì em dùng wireshark để mở thôi
- Mở lên đầu tiên thứ em tìm là đoạn kí tự flag 
- `tcp contains "flag"` nhưng không có gì
- Tiếp theo em kiểm tra luồng dữ liệu
- Bắt đầu luồng tcp, khi kiểm tra đến luồng thứ 5 thì em bắt gặp được đoạn này : `GET /?msg=ZmxhZ3tBRmxhZ0luUENBUH0= HTTP/1.1`
- Có 1 yêu cầu GET được gửi 
- Sau đó là 1 đoạn mã có vẻ là mã hoá 
- em dùng `kt.gy` để xem có gì thú vị không 
- Theo như decode theo phương thức base64 thì ta có flag `flag{AFlagInPCAP}`