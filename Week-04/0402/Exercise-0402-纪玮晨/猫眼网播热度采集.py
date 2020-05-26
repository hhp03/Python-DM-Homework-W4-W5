from selenium import webdriver
browser = webdriver.Chrome(executable_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get("http://piaofang.maoyan.com/dashboard/web-heat")

find = browser.find_elements_by_css_selector("#app > div > div > div.dashboard-content > div.dashboard-list.dashboard-left.bg > div.movielist-container > div > table > tbody > tr")#定位到tr，不要继续定位到td

for i in find:
	print("排名：",i.find_element_by_class_name("moviename-index").text)
	print("名称：",i.find_element_by_class_name("moviename-name").text)
	print("信息：",i.find_element_by_class_name("moviename-info").text)
	print("热度：",i.find_element_by_class_name("heat-text").text)
	print("播放量：",i.find_element_by_class_name("last-col").text)