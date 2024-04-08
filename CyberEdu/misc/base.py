import re
from pwn import *

# Kết nối máy chủ
server_ip = "34.89.210.219"
server_port = 31788
conn = remote(server_ip, server_port)

# Nhận dữ liệu
lanthu = 0
while True:
    lanthu += 1
    received_data = conn.recvline().decode().strip()  # Receive and strip newline character
    
    # Xử lý hex
    if lanthu == 1:
        print(received_data)
        dec = received_data.split("<<")[-1]
        dec = int(dec.split(">>")[0])
        hex_str = hex(dec)  # Chuyển đổi sang chuỗi hexa, loại bỏ '0x' ở đầu
        # Gửi dữ liệu lên
        conn.sendline(hex_str)
    # Xử lý ASCII
    elif lanthu == 2:
        print(received_data)
        hex_str = received_data.split("<<")[-1]
        hex_str = hex_str.split(">>")[0]
        ascii_str = ''.join([chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)])
        print(ascii_str)
        # Gửi dữ liệu lên
        conn.sendline(ascii_str)
    elif lanthu == 3:
        print(received_data)
        #xu ly hex loai bo so 01 
        oct =  received_data.split("<<")[-1]
        oct = oct.split(">>")[0]
        #chuyen qua ascii 
        ascii_str = ''.join([chr(int(oct_digit, 8)) for oct_digit in oct.split()])
        print(ascii_str)
        #gui du lieu
        conn.sendline(ascii_str)
    print(received_data)
    # DCTF{55cdfe07fae36a30c2c8d0738fdcd3f7718e4898f8585b142f7eaf2f269a0deb}