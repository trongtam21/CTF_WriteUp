## Description 
> There is a cyberwar coming. are you ready to decrypt the enemy secrets
## Link challenge
> https://cybertalents.com/challenges/forensics/xmen-files
## Solution
- Sau khi tải file xmendump về máy, mở ra em thu được 1 đoạn hex. Nhìn vào thì đoán đây chín là hex của file zip
```
00000000: 504b 0304 0a00 0000 0000 9996 b350 0000  PK...........P..
00000010: 0000 0000 0000 0000 0000 0500 1c00 786d  ..............xm
00000020: 656e 2f55 5409 0003 4263 c45e 5263 c45e  en/UT...Bc.^Rc.^
00000030: 7578 0b00 0104 0000 0000 048f 0000 0050  ux.............P
00000040: 4b03 040a 0009 0000 0099 96b3 50c8 b55a  K...........P..Z
00000050: 6f27 0000 001b 0000 000d 001c 0078 6d65  o'...........xme
00000060: 6e2f 666c 6167 2e74 7874 5554 0900 0342  n/flag.txtUT...B
00000070: 63c4 5e42 63c4 5e75 780b 0001 0400 0000  c.^Bc.^ux.......
00000080: 0004 8f00 0000 e640 cdf1 cce4 1ae1 2781  .......@......'.
00000090: e916 45d9 a9c0 f403 56fd 3643 009d 0448  ..E.....V.6C...H
000000a0: de8a bfbe faac 4832 f417 7b7f eb50 4b07  ......H2..{..PK.
000000b0: 08c8 b55a 6f27 0000 001b 0000 0050 4b01  ...Zo'.......PK.
000000c0: 021e 030a 0000 0000 0099 96b3 5000 0000  ............P...
000000d0: 0000 0000 0000 0000 0005 0018 0000 0000  ................
000000e0: 0000 0010 00f8 4100 0000 0078 6d65 6e2f  ......A....xmen/
000000f0: 5554 0500 0342 63c4 5e75 780b 0001 0400  UT...Bc.^ux.....
00000100: 0000 0004 8f00 0000 504b 0102 1e03 0a00  ........PK......
00000110: 0900 0000 9996 b350 c8b5 5a6f 2700 0000  .......P..Zo'...
00000120: 1b00 0000 0d00 1800 0000 0000 0100 0000  ................
00000130: f881 3f00 0000 786d 656e 2f66 6c61 672e  ..?...xmen/flag.
00000140: 7478 7455 5405 0003 4263 c45e 7578 0b00  txtUT...Bc.^ux..
00000150: 0104 0000 0000 048f 0000 0050 4b05 0600  ...........PK...
00000160: 0000 0002 0002 009e 0000 00bd 0000 0000  ................
00000170: 00                                       .

```
- Em sử dụng script của python để chỉ lấy các kí tự hexa
```
with open("xmendump", "r") as file:
	for line in file:
		print(line[10:-19])
```
- Tiếp theo sử dụng cybercheff để dựng lên file zip thì bị khoá bởi mật khẩu.
- Tiếp tục bẻ khoá bằng john thì mật khẩu là `password`
- Mở ra ta được flag
> flag{w0lv3rin3_hey_it5_m3}