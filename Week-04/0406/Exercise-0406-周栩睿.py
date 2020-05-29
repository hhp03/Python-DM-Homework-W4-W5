from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
param_dict = {
    'year': 2020,
    'issue': '04',
    'pykm': 'XDCB',
    'pageIdx': 0,
    'pcode': 'CJFD',
}  # 参数列表
now_year = 2018
max_year = 2020
while now_year <= max_year:
    now_month = 1
    print("正在请求第", now_year, "年......")
    param_dict["year"] = now_year  # 将当前年填入到参数列表中
    while now_month<13:
        if now_month<10:
            k = str(now_month)
            now_month = k.zfill(2)
        else:
            now_month=now_month
        print("正在请求第", now_month, "月......")
        param_dict["issue"] = now_month  # 将当前月填入到参数列表中
        response = requests.get("http://new.gb.oversea.cnki.net/knavi/JournalDetail/GetArticleList?" + urlencode(param_dict),headers=headers)
        cnki = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        for words in cnki.select('dd'):
            name = words.select_one('span.name')
            print('标题：', name)
            author = words.select_one('span.author')
            print('作者：', author)
        now_month=int(now_month)
        now_month += 1  # 月份累加
    now_year += 1  # 年数累加

#待解决问题：每次都会卡在不同地方，我感觉是代码太复杂运行太慢，需要改进，但是现在好晚了我想睡觉，所以明天晚上再说吧嘻嘻