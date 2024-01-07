## Đề : 
> The keyword is hexadecimal, and removing an useless H.E.H.U.H.E. from the flag. The flag is in the format CTFlearn{*}
## Link : 
> https://ctflearn.com/challenge/download/883
## Giải :
- Đầu tiên em kiểm tra loại file bằng `file file`
- Kết quả cho ra `file: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=672d1ab79b5c1f063344be7b8edbda2219d8991d, for GNU/Linux 3.2.0, not stripped`

- `cat file` thì thấy đoạn `CTFlearnH�{fl4ggyfH�E�H�U�H�E�l4g}`
- Quay lại đề bài `removing an useless H.E.H.U.H.E. from the flag`. Đề bảo xoá phần dư thừa `H.E.H.U.H.E.` để đi đến flag
- Sau khi xoá em được đoạn mã `CTFlearn{fl4ggyfl4g}` và cũng chính là flag.