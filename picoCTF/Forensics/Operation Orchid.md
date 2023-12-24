## Đề 
> Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
## Link 
> https://artifacts.picoctf.net/c/214/disk.flag.img.gz
## Giải 
- Sau khi tải file tôi kiểm tra loại file bằng lệnh file trước 
```text
file disk.flag.img 
disk.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0xc,223,19), startsector 2048, 204800 sectors; partition 2 : ID=0x82, start-CHS (0xc,223,20), end-CHS (0x19,159,6), startsector 206848, 204800 sectors; partition 3 : ID=0x83, start-CHS (0x19,159,7), end-CHS (0x32,253,11), startsector 411648, 407552 sectors
```
- Tiếp theo tôi kiểm tra phân vùng đĩa bằng lệnh `mmls disk.flag.img `
```text
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
```
- Tiếp tục kiểm tra phân vùng Linux (0x83) bằng lệnh `fls disk.flag.img -o 411648`, KiểM tra cái dưới vì cái trên tôi đã kiểm tra rồi và nó không có gì hết 
```text
d/d 460:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 81: proc
d/d 82: dev
d/d 83: tmp
d/d 84: lib
d/d 87: var
d/d 96: usr
d/d 106:        bin
d/d 120:        sbin
d/d 466:        media
d/d 470:        mnt
d/d 471:        opt
d/d 472:        root
d/d 473:        run
d/d 475:        srv
d/d 476:        sys
d/d 2041:       swap
V/V 51001:      $OrphanFiles
```
- Như thường lệ, vô thư mục root kiểm tra trước rồi tính sau(Vì những thứ quan trọng thường ở đây)
> fls disk.flag.img -o 411648 472
```text
r/r 1875:       .ash_history
r/r * 1876(realloc):    flag.txt
r/r 1782:       flag.txt.enc
```
- Kiểm tra và lấy ra lần lượt từng file 1 
> icat disk.flag.img -o 411648 1875
```text
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```
- Như đã thấy họ tạo 1 file `flag.txt` rồi mã hoá ssl đưa ra file `flag.txt.enc`
- Giờ việc ta cần làm là decode thôi
> icat disk.flag.img -o 411648 1876 > flag.txt
> icat disk.flag.img -o 411648 1782 > flag.txt.enc
> openssl aes256 -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567 -d
- Flag : `picoCTF{h4un71ng_p457_1d02081e}`