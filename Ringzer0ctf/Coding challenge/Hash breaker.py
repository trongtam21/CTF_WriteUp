import hashlib
import requests
 
# cawl data in web 
html_content = requests.get("http://challenges.ringzer0team.com:10056/").text
#print(html_content)
check = html_content.split("----- BEGIN HASH -----<br />")[-1]
check = check.split("<br />")[0].strip()
# get random number 
for value in range(999, 99999):
    value = str(value)
    hash = hashlib.sha1(value.encode()).hexdigest()
    if hash == check:
        print(value)
        break
# send request 
url = "http://challenges.ringzer0team.com:10056/?r=" + value
send = requests.get(url).text
print(send)

