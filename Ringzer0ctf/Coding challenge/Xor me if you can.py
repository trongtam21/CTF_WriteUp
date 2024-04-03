import requests
import base64
html_content = requests.get("http://challenges.ringzer0team.com:10016/").text
# xu ly du lieu
strings1 = html_content.split("----- BEGIN XOR KEY -----")[1]
strings1 = strings1.split("<br />")[1].strip()
print("strings1 : " + str(strings1))

strings2 = html_content.split("----- BEGIN CRYPTED MESSAGE -----")[1]
strings2 = strings2.split("<br />")[1].strip()
print("strings2 : " + str(strings2))
decoded_message = base64.b64decode(strings2).decode('utf-8')
print("strings2 decode : " + str(decoded_message))
for i in range(0, len(strings1)):
    result = ""
    result = result + chr(ord(strings1[i]) ^ ord(decoded_message[i]))
print(result) 