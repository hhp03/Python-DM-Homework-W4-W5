from selenium import webdriver
import time

#使用Selenium设计爬虫，不再解析Url并模拟真实请求；而是直接通过Selenium模拟浏览器操作，打开网页，解析数据即可。
#我们发现网页上的数据每3秒左右会自动刷新一次，这说明数据并不是存在于网页源代码中，而是通过Ajax加载的动态网页
browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe") #使用selenium启动浏览器，打开url
browser.get("http://piaofang.maoyan.com/dashboard/tv-viewing")
time.sleep(1)

print("========实时电视剧热播排名======")
for movie_label in browser.find_elements_by_css_selector(
        "#app > div > div > div.dashboard-content > div.dashboard-list.dashboard-left.bg > div.movielist-container > div > div > table > tbody > tr"):
        print("排名:", movie_label.find_element_by_class_name("moviename-index").text)
        print("名称:", movie_label.find_element_by_class_name("moviename-name").text)
        print("电视台名称:", movie_label.find_element_by_class_name("moviename-info").text)
        print("实时直播关注度:", movie_label.find_element_by_class_name("realtime").text)
        print("市场占有率:", movie_label.find_element_by_class_name("last-col").text)
        print("\n")
print("============End===============")
