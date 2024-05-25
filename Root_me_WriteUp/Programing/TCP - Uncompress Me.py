import zlib
from pwn import *
import base64

conn = remote('challenge01.root-me.org', 52022)
while True:
    data = conn.recv().decode()
    print(data)
    data = data.split("'")[-2]
    print(data)
    base64_decode = base64.b64decode(data)
    print("base64_decode = ", base64_decode)
    zlib_decode = zlib.decompress(base64_decode)
    print("zlib_decode = ", zlib_decode)
    conn.sendline(zlib_decode)


