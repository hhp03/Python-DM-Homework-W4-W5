'''
Python数据采集案例(1)：微博热搜榜采集
'''
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get('https://s.weibo.com/top/summary')
    bs = BeautifulSoup(response.content.decode(), 'html.parser')
    for keyword_label in bs.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        print(keyword_label.text)
