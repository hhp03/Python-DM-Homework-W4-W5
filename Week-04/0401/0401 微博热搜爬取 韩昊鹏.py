import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get("https://s.weibo.com/top/summary")
    bs = BeautifulSoup(response.text, 'lxml')   #response.text返回的类型是str
#response.content返回的类型是bytes，通过decode()方法将bytes类型转为str类型
    #后面的‘lxml’是将获取的网页以lxml的形式展开，展开后的结果是网页的html源代码
    for keyword_label in bs.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):
        print(keyword_label.text)

