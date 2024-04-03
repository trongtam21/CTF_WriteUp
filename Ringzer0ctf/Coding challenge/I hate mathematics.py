import requests
#nhan du lieu
html_content  = requests.get("http://challenges.ringzer0team.com:10032/")
# xu ly du lieu
math = html_content.text.split("----- BEGIN MESSAGE -----<br />")[-1]
math = math.split("=")[0].strip()
tinh = math.split()
#chuyen hex sang dec
hex_to_dec = int(tinh[2], 16)
#chuyen bin sang dec
bin_to_dec = int(tinh[4], 2)
#tinh 
sum = int(tinh[0]) + hex_to_dec - bin_to_dec


# Nhan du lieu tu dap an 
url = "http://challenges.ringzer0team.com:10032/?r=" + str(sum)
print(url)
result = requests.get(url)
print(result.text)