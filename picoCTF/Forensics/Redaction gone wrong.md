## Đề 
> Now you DON’T see me. This report has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
## Hint 
> How can you be sure of the redaction?
## Link 
> How can you be sure of the redaction?
## Giải 
- Sau khi tải file và mở file tôi thấy file pdf đã bị bôi đen 1 số chữ
- Có 2 cách làm cho bài này 
- ` Cách 1 `
- Dù được bôi đen nhưng vẫn sao chép và biết được trong đó có văn bản gì.
- Xem văn bản được viết bên trong thì có flag : `picoCTF{C4n_Y0u_S33_m3_fully}`
- ` Cách 2 ` 
- Ở cách này chúng ta sẽ giải bằng tool
- Có 1 tool chuyển từ file pdf sang file text là `pdftotext`
- Sau khi dùng tool nó sẽ chuyển sang file văn bản và ta sẽ đọc được văn bản bên trong 
- flag : `picoCTF{C4n_Y0u_S33_m3_fully}`