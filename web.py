# coding: utf-8
import requests

link = "https://3g.dxy.cn/newh5/view/pneumonia?from=groupmessage&isappinstalled=0"
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}
r = requests.get(link, headers= headers)
r = r.content.decode('utf-8')

with open('dxy.txt', "a+") as f:
    f.write(r)
    f.close()
