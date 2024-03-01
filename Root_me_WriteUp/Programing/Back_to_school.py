from pwn import *
from math import sqrt

conn = remote('challenge01.root-me.org', 52002)

while True:
	data = conn.recvuntil(b'and').decode()
	#xu ly so thu nhat
	data = data[:-4].split()[-1]
	#xu ly so thu 2
	data2 = conn.recvuntil(b'=').decode().split()[-2]
	#tinh
	tinh = sqrt(int(data)) * int(data2)
	#lam tron 
	tinh = round(tinh, 2)
	print(tinh)
	conn.sendline(str(tinh).encode())
