from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"F:\python3.8.2\chromedriver-Windows")
browser.get("http://piaofang.maoyan.com/dashboard/tv-viewing")

print("========实时电视剧热播排名======")
for movie_label in browser.find_elements_by_css_selector(
            "#app > div > div > div.dashboard-content > div.dashboard-list.dashboard-left.bg > div.movielist-container > div > div > table > tbody > tr"):
    print("排名:", movie_label.find_element_by_class_name("moviename-index").text)
    print("名称:", movie_label.find_element_by_class_name("moviename-name").text)
    print("信息:", movie_label.find_element_by_class_name("moviename-info").text)
    print("信息:", movie_label.find_element_by_class_name("realtime").text)
    print("信息:", movie_label.find_element_by_class_name("last-col").text)
print("============End===============")