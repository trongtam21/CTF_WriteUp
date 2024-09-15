from pwn import *
import time
server_ip = "172.104.49.143"
server_port = 1325
digit = 0
p = remote(server_ip, server_port)
while True:
    data = p.recvuntil("digit:")
    if "flag" in str(data) or "Flag" in str(data):
        break
    print(data)
    p.sendlines(str(digit))
    time.sleep(0)
    print("da gui ", digit)
    digit = digit+1