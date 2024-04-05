import hashlib
import requests
import binascii
# nhan du lieu ve 
html_content = requests.get("http://challenges.ringzer0team.com:10014/").text
#print(html_content)
#xu ly du lieu hash
data = html_content.split("----- BEGIN MESSAGE -----")[-1].strip()
data_bin =  data.split("<br />")[1].strip()
#print(data)
# convert bin to ascii
def binary_to_ascii(data_bin):
    # Chia chuỗi nhị phân thành các nhóm 8 bit (1 byte) mỗi nhóm
    bytes_list = [data_bin[i:i+8] for i in range(0, len(data_bin), 8)]

    # Chuyển đổi từng byte thành ký tự ASCII và nối chúng lại thành một chuỗi
    ascii_str = ''.join(chr(int(byte, 2)) for byte in bytes_list)

    return ascii_str
ascii = binary_to_ascii(data_bin)
#print(ascii)
# tao hash

hash = hashlib.sha512(ascii.encode()).hexdigest()
#print("HASH : " + str(hash))

# gui request
url = "http://challenges.ringzer0team.com:10014/?r=" + str(hash)
#print("url : " + str(url))
send = requests.get(url).text
print(send)
