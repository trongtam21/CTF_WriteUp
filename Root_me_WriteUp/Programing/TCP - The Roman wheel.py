from pwn import *
def rot13(text):
    result = []
    for char in text:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        # Check if the character is a lowercase letter
        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)
conn = remote('challenge01.root-me.org', 52021)
while True:
    # nhan du lieu
    data = conn.recv().decode()
    print(data)
    data = data.split("'")[-2]
    print(data)
    gui = rot13(data).encode('ascii')
    print(gui)
    # gui du lieu
    conn.sendline(gui)
