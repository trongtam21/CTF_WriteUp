## Đề 
- This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from here.
## Link 
- https://artifacts.picoctf.net/c/80/Flag.pdf
## Hint 
- Remember that some file types can contain and nest other files
## Giải 
- Sau khi tải tôi được 1 file pdf 
- Dựa vào cái đề và cái hint nên có 1 dự cảm không lành về loại của file
- Kiểm tra nó thì đúng là nó không phải file pdf mà là 1 file shell
```text
┌──(trongtam㉿kali)-[~/Downloads]
└─$ file Flag.pdf          
Flag.pdf: shell archive text                                
```
- Chạy nó nhưng chạy không được 
```text
┌──(trongtam㉿kali)-[~/Downloads]
└─$ ./Flag.pdf 
zsh: permission denied: ./Flag.pdf
```
- Chưa đủ quyền nên tôi dùng chmod để cấp quyền cho nó 
> chomd +x Flag.pdf
- Sau khi chạy thành công thì ta được 1 file flag
- Tiếp tục kiểm tra loại file 
- `flag: current ar archive` Đây là file nén ar
- Đổi đuôi file rồi giải nén nó 
> mv flag flag.ar
> ar -x flag.ar
- Ta lại tiếp tục được 1 file flag 
- Kiểm tra loại file : `flag: cpio archive`
- Đổi đuôi file và giải nén 
> mv flag flag.cpio
- Không hiểu sao file này extract không được nên tôi extract bằng cách nhấn vào file và kéo ra
- Tiếp tục kiểm tra loại file mới extract flag: `bzip2 compressed data, block size = 900k`
> mv flag flag.bz2
> bzip2 -d flag.bz2
- Lại là 1 file flag
- Lần này là file `flag: gzip compressed data, was "flag", last modified: Thu Mar 16 01:40:15 2023, from Unix, original size modulo 2^32 328`
>  mv flag flag.gz
> gzip -d flag.gz 
- Cứ tiếp tục như thế cho đến khi thu được 1 file ascii text
```text
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33633739633562617d0a
```
- Đổi từ hexa qua dec ta được flag 
> Flag : picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
