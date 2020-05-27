from selenium import webdriver
browser=webdriver.Chrome(executable_path='D:\chromedriver\chromedriver_win32\chromedriver.exe')
browser.get('http://piaofang.maoyan.com/dashboard/web-heat')
for movie_label in browser.find_elements_by_css_selector("#app > div > div > div.dashboard-content > div.dashboard-list.dashboard-left.bg > div.movielist-container > div > table > tbody > tr"):
    print("排名:", movie_label.find_element_by_class_name("moviename-index").text)
    print("名称:", movie_label.find_element_by_class_name("moviename-name").text)