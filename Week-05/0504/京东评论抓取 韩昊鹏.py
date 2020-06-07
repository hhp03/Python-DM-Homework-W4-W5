import time
from urllib.parse import urlencode
import requests
import json

url = "https://club.jd.com/comment/productPageComments.action?"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
param_dict = {
    'callback': "fetchJSON_comment98",
    "productId": 3598302,
    "score": 0,
    "sortType": 5,
    "page": 1,
    "pageSize": 10,
    "isShadowSku": 0,
    "rid": 0,
    "fold": 1
}
a = int(input("请输入您获取的页码总数:"))
x = 0
while x < a:
    param_dict['page'] = x
    response = requests.get(url + urlencode(param_dict), headers=headers)
    time.sleep(3)
    #新增
    response=response.text
    #截取{ 与 }之间的json数据
    begin=response.find("{")
    end=response.rfind("}")
    jsondata=response[begin:end+1]
    #新增结束
    data_dict = json.loads(jsondata)
     #在comments数组中进行遍历
    for item in data_dict["comments"]:
        print(item["content"])
    x = x + 1

#例子a是4，现在这样抓到了第一页到第四页数据 x=0对应第一页 x=3对应第四页
