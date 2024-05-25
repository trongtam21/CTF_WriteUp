from pwn import *
import base64
conn = remote('challenge01.root-me.org', 52023)
while True:
    data = conn.recv()
    print("=======du lieu nhan duoc=========")
    print(data)
    print("=================================")
    base64_encode = data.split(b"'")[-2].decode()
    decoded_bytes = base64.b64decode(base64_encode).decode()
    print(decoded_bytes)
    # gui du lieu len
    conn.sendline(decoded_bytes)