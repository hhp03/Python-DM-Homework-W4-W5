import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    response=requests.get("https://s.weibo.com/top/summary")
    #BeautifulSoup最主要的功能是从网页抓取数据，Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码
    top=BeautifulSoup(response.content.decode(),'lxml')
    for keyword in top.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        print(keyword.text)