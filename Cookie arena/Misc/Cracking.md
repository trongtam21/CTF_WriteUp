## Đề 
> Use office2john and John the Ripper to crack Office document password (docxs or xlsx format,..)
## Link 
> https://battle.cookiearena.org/challenges/miscellaneous/cracking/download
## Giải 
- Lúc đầu tôi tưởng john chỉ để crack file nén thôi, chứ không nghĩ nó thể crack cả file office
- Tải file về và giải nén ra ta được file `cracking.docx`
- Khi mở ra thì cần mật khẩu
- Tôi sẽ dùng john để crack 
> office2john Cracking.docx > hash.txt
- Tôi lưu hash vô file hash.txt
- Tôi sử dụng wordlist rockyou.txt để crack
```text
┌──(trongtam㉿kali)-[~/Downloads/Cracking]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Office, 2007/2010/2013 [SHA1 256/256 AVX2 8x / SHA512 256/256 AVX2 4x AES])
Cost 1 (MS Office version) is 2013 for all loaded hashes
Cost 2 (iteration count) is 100000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
princess         (Cracking.docx)     
1g 0:00:00:00 DONE (2023-12-25 21:23) 2.941g/s 94.11p/s 94.11c/s 94.11C/s 123456..butterfly
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
``` 
- Có thể thấy mật khẩu là `princess`
- Giờ thì mở file cracking.docx và lấy flag thôi
> Flag : CHH{m0i_thu_d3u_nen_dc_b4o_m4t}