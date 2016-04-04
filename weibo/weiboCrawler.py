#-*-coding:utf8-*-

import requests
from lxml import etree

cook = {"Cookie": "_T_WM=79b292d9b2b5db69326129538710051a; SUB=_2A257-QqdDeTxGeRN71oQ-CnLzT6IHXVZBZbVrDV6PUJbstBeLVjikW1LHesJGwkoTCoMg8veZGhzSMf22LlDyg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhecUJLDareKqh1KH5IHm8D5JpX5o2p; SUHB=0y0ILbfZc1ZCFc; SSOLoginState=1459452621; gsid_CTandWM=4uBGCpOz5IlntWK4kswQv9QRZci"}
url = 'http://weibo.cn/u/2073743251?page=' #此处请修改为微博网址
# html = requests.get(url).content
# print html
for i in range(20,40):
    html = requests.get(url+str(i), cookies = cook).content
    # html = requests.get(url, cookies = cook).text

    # html = bytes(bytearray(html, encoding='utf-8'))
    selector = etree.HTML(html)
    content = selector.xpath('//span[@class="ct"]')
    for each in content:
        text = each.xpath('string(.)')
        b = 1
        print text
