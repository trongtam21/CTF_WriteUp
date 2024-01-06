## Đề 
> You'll need Brute Force to solve this. Knowing Python should help too. Oh! And Base64 encryption of course! Find the flag!
## Link 
> https://mega.nz/#!vf43RCyC!NNpuYjB3d-gevhsHXefwAAAmzk4tJHxUZr0GnrSDI_c Hash: e82a4b4a0386d5232d52337f36d2ab73
## Giải 
- Khi tải file từ link trên về ta được 1 ảnh đuôi jpg 
- Thử lần lượt qua các cách thông thường thì thấy có nhiều folder giấu bên trong 
- Để extract nó ra ta dùng binwak 
> binwalk -e legotroopers.jpg
- Sau khi truy cập vào ta thấy rất nhiều folder con giấu bên trong, việc tìm bằng tay hầu như là không thể
- Ngoài ra còn có file nén 1926.zip có gắn mật khẩu
- Ta cần tìm mật khẩu từ các folder đó 
> find -D tree 
- Lệnh này để liệt kê thư mục ra cho mình thấy 
- Không có folder nào có tên đặc biệt, có thể nó là các kí tự trong file 
> find -D tree | grep pico
- Cũng không có gì =))
> find -D tree | grep pass
```text
_legotroopers.jpg.extracted/folders/73/43/p:The password is: "ctflag*****" where * is a number.
_legotroopers.jpg.extracted/folders/73/43/p:Encrypt the password using MD5 and compare it to the given hash!
_legotroopers.jpg.extracted/folders/73/43/p:As I said, you're gonna have to brute force the password!
_legotroopers.jpg.extracted/folders/73/47/p:The password is: "ctflag*****" where * is a number.
_legotroopers.jpg.extracted/folders/73/47/p:Encrypt the password using MD5 and compare it to the given hash!
_legotroopers.jpg.extracted/folders/73/47/p:As I said, you're gonna have to brute force the password!
```
- Nhìn vào đây ta thấy mật khẩu giải nén là ctflag..... với số đằng sau 
- Ta sẽ brute force theo hint này 
- Đầu tiên phải tạo wordlist cái đã
```text
strings = "ctflag"
for i in range(0, 100000):
    # chạy i từ 0 đến 99999
    i = str(i)
    n = 5-len(i)
    strings2 = "0"*n + str(i)
    # in ra 0 trong trường hợp có số 0 đằng trước. VD : 000043
    strings_du = strings + strings2
    print(strings_du)
```
- Chạy rồi lưu có vào file wordlist.txt
> python3 bruteforce.py > wordlist.txt
- Rồi thì thử mật khẩu với john 
> zip2john 1926.zip > 1926
> john 1926 --wordlist=/home/trongtam/Downloads/wordlist.txt
```text
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ctflag48625      (1926.zip/flag.zip)     
1g 0:00:00:00 DONE (2023-11-07 21:00) 25.00g/s 1228Kp/s 1228Kc/s 1228KC/s ctflag40960..ctflag49151
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
- Mật khẩu sau khi chạy là : `ctflag48625`
- Giải nén và decode để nhận flag 
- Flag : `FLAG{may_the_brute_force_be_with_you}`