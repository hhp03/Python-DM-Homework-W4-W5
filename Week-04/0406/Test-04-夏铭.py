#问题：会一直爬到2020年12月
import time
import re
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
url="https://navi.cnki.net/knavi/JournalDetail/GetArticleList?"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
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
while now_year <= max_year:
    for i in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        print('正在请求%a年%a月' % (now_year, now_month))
        param_dict['issue'] = i
        param_dict["year"] = now_year
        response = requests.get(url + urlencode(param_dict), headers=headers)
        if now_month < 12:
            now_month += 1
        else:
            now_month = 1
        time.sleep(3)
        bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        for label in bs.select("dd"):
                name = label.select_one('span.name').text
                name = re.sub("^\s*|\s*$", "", name)  # 清除空格
                print('标题：', name)
                author = label.select_one('span.author').text
                print('作者：', author)
    now_year += 1




