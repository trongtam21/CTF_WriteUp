## Đề 
> The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)
## Kết nối máy chủ 
> ssh bandit12@bandit.labs.overthewire.org -p 2220 (password : JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv)
## Giải 
- Sau khi kết nối chúng ta phải xem nó có gì bên trong, ở bên trong là 1 đoạn các kí tự hexa và ascii.
- Lúc đầu tôi nghĩ đó là 1 file bin hay gì đó nhưng nó chỉ là 1 file ascii 
```text
bandit12@bandit:~$ file data.txt
data.txt: ASCII text
```
- Theo đề tôi sẽ copy và đưa nó vào /tmp/ để xử lý vì tại thư mục hiện tại tôi dùng các lệnh như mv không được
```text
/tmp – Thư mục chứa các tập tin tạm
Thư mục chứa các tập tin tạm được tạo bởi hệ thống và người dùng.
Các tập tin trong thư mục này bị xóa khi hệ thống khởi động lại.
```
- lấy vị trí hiện tại trước để xíu di chuyển (/home/bandit12/data.txt)
```text
bandit12@bandit:/tmp$ mkdir abc
mkdir: cannot create directory ‘abc’: File exists
bandit12@bandit:/tmp$ mkdir abc.a
bandit12@bandit:/tmp$ ls
ls: cannot open directory '.': Permission denied
bandit12@bandit:/tmp$ cd abc.a
bandit12@bandit:/tmp/abc.a$ ls
bandit12@bandit:/tmp/abc.a$ 
```
- Như đã thấy ở `/tmp` mình không có quyền dùng lệnh ls, chỉ khi ở `/tmp/abc.a` mới tạo mới được dùng 
- Giờ sẽ copy nó từ `/home/bandit12/data.txt` sang `/tmp/abc.a`
> cp /home/bandit12/data.txt /tmp/abc.a
- Vì file data.txt chính là hexdump nên ta phải chuyển ngược về bin để xem thử đây là file gì 
```text
bandit12@bandit:/tmp/abc.a$ xxd -r data.txt
�h44�z��A����@=�h4hh�▒▒��4�i��1����▒��hd����9���1����������;,�
�����2�3d*58�~  �S�▒ZP^��luY��Br$�FP!%�s��h�?�)[=�h��O(B��2A���)�tZc��:�pã)�A�ˈ�0���΅A�yjeϢx,�(����z�E�+"�2�/�-��e"���^����t�j���$�d�@�dJơ'7\���$��m1c��#>�aԽ�EV��F�OCӐc@M�C���]��Y2^h8���D=��~      O�I��NDpF�+�|b#Jv�#�J��d�LފW$�Û�▒y�`
                                                                    �\& ���[�@*w�M�0θ��nr��C��`e$b�
                                                                                                   ~�{���
                                                                                                         ��`�<����a��?e:T���e�T4±b����)�@���x=
bandit12@bandit:/tmp/abc.a$ xxd -r data.txt data.bin                                                                                                                                          
bandit12@bandit:/tmp/abc.a$ file data.bin
data.bin: gzip compressed data, was "data2.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 170798638
```
- Có thể thấy đây là file gzip, đôi đuôi file thành .gz
>  mv data.bin data.gz
- Giải nén 
```txt
bandit12@bandit:/tmp/abc.a$ gzip -d data.gz

gzip: data.gz: decompression OK, trailing garbage ignored
```
- Ta được 1 file data
- Kiểm tra loại file thì thấy nó là bzip 
- Đuổi đuôi giải nén tiếp =))
- Liên tục giải nén và đổi tên ta sẽ được password
```text
bandit12@bandit:/tmp/abc.a$ ls
data.bz
bandit12@bandit:/tmp/abc.a$ bzip2 -d data.bz
bandit12@bandit:/tmp/abc.a$ ls
data
bandit12@bandit:/tmp/abc.a$ file data
data: gzip compressed data, was "data4.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/abc.a$ mv data data.gz
bandit12@bandit:/tmp/abc.a$ gzip -d data.gz
bandit12@bandit:/tmp/abc.a$ mv data data.tar
bandit12@bandit:/tmp/abc.a$ tar -xf data.tar
bandit12@bandit:/tmp/abc.a$ ls
data5.bin  data.tar
bandit12@bandit:/tmp/abc.a$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/abc.a$ mv data5.bin data5.bin.tar
bandit12@bandit:/tmp/abc.a$ tar -xf data5.bin.tar
bandit12@bandit:/tmp/abc.a$ ls
data5.bin.tar  data6.bin  data.tar
bandit12@bandit:/tmp/abc.a$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/abc.a$ mv data6.bin data6.bin.bz
bandit12@bandit:/tmp/abc.a$ bzip2 -d data6.bin.bz
bandit12@bandit:/tmp/abc.a$ ls
data5.bin.tar  data6.bin  data.tar
bandit12@bandit:/tmp/abc.a$ file data6.bin
data6.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/abc.a$ mv dat6.bin data6.tar
mv: cannot stat 'dat6.bin': No such file or directory
bandit12@bandit:/tmp/abc.a$ mv dat6.bin data6.bin.tar
mv: cannot stat 'dat6.bin': No such file or directory
bandit12@bandit:/tmp/abc.a$ mv data6.bin data6.bin.tar
bandit12@bandit:/tmp/abc.a$ tar -xf data6.bin.tar
bandit12@bandit:/tmp/abc.a$ ls
data5.bin.tar  data6.bin.tar  data8.bin  data.tar
bandit12@bandit:/tmp/abc.a$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/abc.a$ mv data8.bin data8.gz
bandit12@bandit:/tmp/abc.a$ gzip -d data8.gz
bandit12@bandit:/tmp/abc.a$ ls
data5.bin.tar  data6.bin.tar  data8  data.tar
bandit12@bandit:/tmp/abc.a$ file data8
data8: ASCII text
bandit12@bandit:/tmp/abc.a$ cat data8
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```
> Password : wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
