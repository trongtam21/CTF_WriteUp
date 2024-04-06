import requests
import hashlib

# lay du lieu ve 
html_content = requests.get("http://challenges.ringzer0team.com:10057/").text
hash_check = html_content.split("----- BEGIN HASH -----")[-1]
hash_check = hash_check.split("<br />")[1].strip()
#print(hash_check)
salt = html_content.split(" ----- BEGIN SALT -----<br />")[-1]
salt = salt.split("<br />")[0].strip()
#print(salt)

# kiem tra mat khau 
for i in range(0, 10000):
    #tao hash 
    i = str(i)
    salt_i = i + salt
    hash = hashlib.sha1(salt_i.encode()).hexdigest()
    if hash == hash_check:
        #print(i)
        break
# gui request 
url = "http://challenges.ringzer0team.com:10057/?r=" + i
send = requests.get(url).text
print(send)
