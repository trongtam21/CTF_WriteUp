## Đề 
- Extract the flag from the Gandalf.jpg file. You may need to write a quick script to solve this.
## Link 
- https://ctflearn.com/challenge/download/936
## Giải
- Đầu tiên em phải tải file và bắt đầu tìm kiếm em thấy 1 đoạn mã hoá base64
```text
+Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=
+xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p
+h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU
```
- Decode dòng đầu tiên thì ta có được `CTFlearn{xor_is_your_friend}`
- Submit thì không đúng, nghĩa là đây chính là hint của bài
- Sử dụng xor thì phải có trên 2 nguồn dữ liệu
- Trùng hợp là còn 2 đoạn string chưa sử dụng
- Em tạo 1 đoạn code python xor chúng
- 
```text
import base64

string1 = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
string2 = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

a = string1
A = base64.b64decode(a)
#gán string1 cho a rồi decode nó sau đó gán cho A
print(A)
b = string2
B = base64.b64decode(b)
print(B)
#gán string2 cho b rồi decode nó sau đó gán cho B
c = []
l = len(A)

i = 0
while i < l:
  c.append(chr(A[i] ^ B[i]))
  i += 1

print(c)
```
- Chạy code là ta có được `['C', 'T', 'F', 'l', 'e', 'a', 'r', 'n', '{', 'G', 'a', 'n', 'd', 'a', 'l', 'f', '.', 'B', 'i', 'l', 'b', 'o', 'B', 'a', 'g', 'g', 'i', 'n', 's', '}']`
- Giờ dùng python xoá 1 vài kí tự không cần thiết 
```tex
my_list=['C', 'T', 'F', 'l', 'e', 'a', 'r', 'n', '{', 'G', 'a', 'n', 'd', 'a', 'l', 'f', '.', 'B', 'i', 'l', 'b', 'o', 'B', 'a', 'g', 'g', 'i', 'n', 's', '}']
for i in range(0, len(my_list)):
    print(my_list[i], end = '') # end = '' để in trên cùng 1 dòng 
```
- Flag là : `CTFlearn{Gandalf.BilboBaggins}`