## Đề 
> Did you ever hear the tragedy of Darth Plagueis The Wise? It’s written here in a magical way, but I can’t figure out how to read it. Can you help me?
## Link download 
> https://drive.google.com/file/d/1Yq5ckdzTmoUEnsyLzMJYTKLdz7JEw_ve/view?usp=sharing
## Giải 
- Sau khi tải xuống em nhận được 4464 file không có đuôi
- Để xác định được loại file em dùng đến file và exiftool nhưng không thành công 
- Khi dùng đến hexeditor em thấy được đoạn đầu tiên nó như thế này 
```text
00000000  44 50 4E 47  0D 0A 1A 0A   00 00 00 0D  49 48 44 52                                                                                         DPNG........IHDR
00000010  00 00 03 20  00 00 01 C1   08 06 00 00  00 91 F7 DF                                                                                         ... ............
00000020  66 00 00 20  00 49 44 41   54 78 5E EC  5D 09 FC 56                                                                                         f.. .IDATx^.]..V
```
- Có thể thấy rằng đây chính là định dạng của file png nhưng bị hỏng phần header `44 50 4E 47`
- Các file khác cũng như vậy nhưng byte đầu tiên khác nhau ở các file
```text
00000000  69 50 4E 47  0D 0A 1A 0A   00 00 00 0D  49 48 44 52                                                                                         iPNG........IHDR
00000010  00 00 03 20  00 00 01 C1   08 06 00 00  00 91 F7 DF                                                                                         ... ............
00000020  66 00 00 20  00 49 44 41   54 78 5E EC  5D 09 FC 56                                                                                         f.. .IDATx^.]..V
```
- em lần lượt sửa phần đầu của các file và đổi đuôi nhưng không thấy flag 
- Nhìn kĩ lại thì kích thước các file giống nhau, nếu chứa flag thì nó phải khác 
- Ý tưởng tiếp theo là hợp các byte đầu của mỗi file lại
- Để thực hiện được em phải viết 1 đoạn code python như sau 
```text
path_main = '/home/trongtam/Downloads/magic_plagueis_the_wise/'
for i in range(2, 4464):
	path = path_main + str(i)
	with open(path, 'rb') as file:
		byte_1 = file.read(1)
		#chuyen sang hex
		byte_1 = byte_1.hex()
		ascii = bytes.fromhex(byte_1).decode('ascii')
		print(ascii, end = '')
```
- Sau khi chạy ta được kết quả
```text
id you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but
not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from 
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but 
not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from 
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but 
not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from 
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but 
not himself.

UMDCTF{d4r7h_pl46u315_w45_m461c}

Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. a Dark Lord of 
the Sith, so powerful and so wise he could use the Force to influence the midichlorians to 
create life. He had such a knowledge of the dark side that he could even keep the ones he
cared about from dying. The dark side of the Force is a pathway to many abilities some
consider to be unnatural. He became so powerful. The only thing he was afraid of was losing
his power, which eventually, of course, he did. Unfortunately, he taught his apprentice
everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others
from death, but not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but
not himself.     
```
> Flag : UMDCTF{d4r7h_pl46u315_w45_m461c}
