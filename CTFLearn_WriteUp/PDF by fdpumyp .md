- Để : 

Hi, just as we talked during a break, you have this file here and check if something is wrong with it. That's the only thing we found strange with this suspect, I hope there will be a password for his external drive

Bye
- Link : https://ctflearn.com/challenge/download/957
- Đầu tiên tôi tải về được 1 file pdf có tên là dontopen.pdf
- MỞ file ra dòng chữa này xuất hiện : CAN'T TOUCH THIS
- tôi dùng `exiftool` để kiểm tra dữ liệu của file thì không thấy gì.
- Tiếp theo tôi dùng   `strings` thấy có dòng `== SECRET DATA DONT LOOK AT THIS ==`
- Sau đó là 3 dòng như sau `external:Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==   pin:1234    password:MTIzMVdST05HOWlzamRuUEFTU1dPUkQ=`
- Sau khi decode dòng external theo phương pháp mã hoá base64 thì ra đoạn strings này `CTFlearn{)_1l0w3y0Um00my123}` và nó cũng chính là flag chúng ta đang tìm ✔
- Ngoài ra còn có 1 cách khác để decode base64 ngay trên cmd luôn, khỏi phải qua web.
  - DECODE/ENCODE STRING   
    - echo -n 'STRING' | base64 --decode
    - echo -n 'my-string' | base64
  - DECODE/ENCODE FILE
    - bas64 /path/to/file > output.txt
    - base64 --decode /path/to/file > output.txt
- Theo như trên thì để decode đoạn mã hoá `Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==` thì cmd sẽ là 
- `echo -n 'Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==' | base64 --decode`
  