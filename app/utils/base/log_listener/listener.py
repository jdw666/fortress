import requests
import os

filename = './log/example.log'
cmd = "ls > " + filename
os.system(cmd)
content = open(filename, "r", encoding="utf-8")
url = "http://dev.www.yixzm.cn"
data = {"message": content}
res = requests.post(url=url, data=data)
print(res.text)