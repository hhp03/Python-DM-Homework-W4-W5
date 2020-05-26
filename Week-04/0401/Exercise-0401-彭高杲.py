import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get("https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6")
    bs = BeautifulSoup(response.content.decode(),'lxml')
    i = 1
    print("===========微博热搜榜===========")
    for keyword in bs.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        print(str(i),keyword.text)
        i += 1
    print("=============打印完成============")