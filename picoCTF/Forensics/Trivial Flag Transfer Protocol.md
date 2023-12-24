## Đề 
> Figure out how they moved the flag.
## Link 
> https://mercury.picoctf.net/static/88553d672efbccbc5868002f4c6eb737/tftp.pcapng
## Hint 
> What are some other ways to hide data?
## Giải 
- Như thường lệ, đầu tiên tôi mở file và xem các gói tin. Hầu hết các gói tin đều là TFTP
- Xem các tập tin được gửi đi trong phần `File > Export Object > TFTP` thì tôi thấy có 6 tập tin 
- Lưu chúng về và mở lần lượt
- `instructions.txt` Thì 1 đoạn mã hiện ra `GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA`
- Có thể nó đã được mã hoá 
- Decode thông qua R0T 13 thì được đoạn như sau : `TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN`
> `TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DIS GUISE OUR FLAG TRANSFER. FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN`
- `plan` cũng tương tự 
- Giải mã bằng R0T 13 thì tôi được `I USED THE PROGRAM AND HID IT WITH- DUEDILIGENCE. CHECK OUT THE PHOTOS`
- Nó bảo mình kiểm tra ảnh 
- Đối với ảnh tôi kiểm tra nó bằng steghide 
- Nhưng mà dùng steghide là phải có mật khẩu 
- Đọc lại mấy cái hint thì có thể mật khẩu là `DUEDILIGENCE`
- giải nó bằng mật khẩu đó xem thử sao `steghide extract -sf picture1.bmp -p  DUEDILIGENCE`  `steghide extract -sf picture2.bmp -p  DUEDILIGENCE`  `steghide extract -sf picture3.bmp -p  DUEDILIGENCE`
- Sau khi thử hết 3 cái thì ảnh số 3 thành công và nó extract ra 1 file `flag.txt`
- Mở file ra thì ta có flag : `picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`