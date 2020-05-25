import requests
import bs4
if __name__ == '__main__':
    URL='https://s.weibo.com/top/summary'
    responce=requests.get(URL)
    content=bs4.BeautifulSoup(responce.content.decode(),'lxml')     #content-decode-lxml
    for i in content.select("#pl_top_realtimehot > table > tbody > tr > td.td-02 > a"):         #括号内是硬性要求
        print(i.text)   #要加text才会显示文本格式