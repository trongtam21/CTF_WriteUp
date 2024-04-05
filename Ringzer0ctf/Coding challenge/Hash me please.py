import hashlib
import requests
# nhan du lieu ve 
html_content = requests.get("http://challenges.ringzer0team.com:10013/").text
#print(html_content)
#xu ly du lieu hash
data = html_content.split("----- BEGIN MESSAGE -----")[-1].strip()
data =  data.split("<br />")[1].strip()
#print(data)
# tao hash
hash = hashlib.sha512(data.encode()).hexdigest()
#print("HASH : " + str(hash))

# gui request
url = "http://challenges.ringzer0team.com:10013/?r=" + str(hash)
#print("url : " + str(url))
send = requests.get(url).text
print(send)
