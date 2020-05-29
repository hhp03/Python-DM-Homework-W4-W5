#师哥QAQ 我不知道为什么换行符去不掉 就留在那了
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
import time

headers = {
    "Accept": "*/*",
    "AcceptEncoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "navi.cnki.net",
    "Referer": "https://navi.cnki.net/knavi/JournalDetail?pcode=CJFD&pykm=XDCB",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}  # Headers
param_dict = {
    'year': 2018,
    'issue': '01',
    'pykm': 'XDCB',
    'pageIdx': 0,
    'pcode': 'CJFD'
}
now_month=1
now_year=2018
max_year=2020

while now_year < max_year:
    for i in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        print('正在爬取%d年%d期' % (now_year, now_month))
        param_dict['issue'] = i
        param_dict["year"] = now_year
        response = requests.get("https://navi.cnki.net/knavi/JournalDetail/GetArticleList?" + urlencode(param_dict), headers=headers)
        if now_month < 12:
            now_month += 1
        else:
            now_month = 1
        time.sleep(3)
        bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        for label in bs.select("dd"):
            name = label.select_one('span.name').text
            name =  name.replace("/n","").replace(" ","").replace("/r","")
            author = label.select_one('span.author').text
            print(author," ",name)
    now_year += 1
else:
    for i in ['01','02','03','04','05']:
        print('正在爬取%d年%d期' % (now_year, now_month))
        param_dict['issue'] = i
        param_dict["year"] = now_year
        response = requests.get("https://navi.cnki.net/knavi/JournalDetail/GetArticleList?" + urlencode(param_dict), headers=headers)
        if now_month < 12:
            now_month += 1
        else:
            now_month = 1
        time.sleep(3)
        bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        for label in bs.select("dd"):
            name = label.select_one('span.name').text
            name =  name.replace("/n","").replace(" ","").replace("/r","")
            author = label.select_one('span.author').text
            print(author," ",name)
