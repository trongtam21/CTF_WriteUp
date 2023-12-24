## Đề :
> Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz
## Link 
> https://mercury.picoctf.net/static/4f3df7052b4121aff89af1a3f517afb1/dds1-alpine.flag.img.gz
## Hint 
1. Have you ever used `file` to determine what a file was?
2. Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
3. Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
4. Using your own computer, you could use qemu to boot from this disk!
## Giải 
- Đầu tiên tôi tải file về được 1 file `dds1-alpine.flag.img.gz`
- Sử dụng lệnh file để kiểm tra xem
- `dds1-alpine.flag.img.gz: gzip compressed data, was "dds1-alpine.flag.img", last modified: Tue Mar 16 00:19:57 2021, from Unix, original size modulo 2^32 134217728`
- Tiếp theo tôi tiến hành giải nén file `gzip -d dds1-alpine.flag.img.gz`
- Sau khi giải nén tôi được 1 file DOS/MBR
- Đọc dữ liệu trong file, chèn thêm lệnh tìm chuỗi pico vào thì ta có flag `strings dds1-alpine.flag.img | grep pico   `
> Flag : picoCTF{f0r3ns1c4t0r_n30phyt3_a011c142}
- Ngoài ra còn có thể dùng lệnh : `srch_strings dds1-alpine.flag.img | grep pico`