'''
author: 周粤婷
name:爬取知网期刊文章数据
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
#获取期刊基本信息
def journal_info(soup):
    infobox = soup.find(name="dd", attrs={"class": "infobox"})
    journal_name = infobox.find(name="h3", attrs={"class": "titbox"}).text
    journal_type = [i.text for i in infobox.find(name="p", attrs={"class": "journalType"}).findAll("span")]
    journal_name = re.sub("\n *", "\n", journal_name)
    journal_name = re.sub("^\n", "", journal_name)
    print(journal_name)
    print(journal_type)
#获取期刊的年和越
def issue_info(bs):
    year_issue = bs.find(name="dl", attrs={"class": "s-dataList clearfix cur"}).find(name="dt").find(name="em").text
    month_issue = bs.find(name="dl", attrs={"class": "s-dataList clearfix cur"}).find(name="dd").find(name="a",attrs={"class":"current"}).text
    print(year_issue+"年"+month_issue+"期")
#获取文章信息
def article(bs):
    print("栏目名称：")
    for column_label in bs.select("#CataLogContent > dt"):
        column_name = column_label.text
        print(column_name)
    for article_label in bs.select("#CataLogContent > dd"):
        article_name = article_label.select_one("dd > span > a").text
        author_name = article_label.select_one("dd > span.author").text
        page = article_label.select_one("dd > span.company").text
        article_name = re.sub("\n *", "\n", article_name)
        article_name = re.sub("^\n", "", article_name)
        author_name = re.sub('\S$','',author_name)
        print('文章标题：'+article_name)
        print('作者名称：'+author_name)
        print('页码：'+page+'\n')
if __name__=="__main__":
    browser = webdriver.Chrome(
        r"C:\Users\86158\AppData\Local\Programs\Python\Python38\Scripts\chromedriver.exe")
    browser.get("http://navi.cnki.net/knavi/JournalDetail?pcode=CJFD&pykm=XDCB&Year=&Issue=&Entry=")
    time.sleep(3)
    bs_first = BeautifulSoup(browser.page_source, "html.parser")
    journal_info(soup=bs_first)
    issue_info(bs=bs_first)
    article(bs=bs_first)
    for page in range(3):
        time.sleep(10)
        larrow_page = browser.find_element_by_xpath("//*[@id='larrow']")
        larrow_page.click()
        time.sleep(10)
        bs_update = BeautifulSoup(browser.page_source, "html.parser")
        issue_info(bs=bs_update)
        article(bs=bs_update)
    for year in range(2):
        change_year = browser.find_element_by_xpath('//*[@id="%d_Year_Issue"]/dt' % int(2019-year))
        change_year.click()
        time.sleep(10)
        bs_update = BeautifulSoup(browser.page_source, "html.parser")
        issue_info(bs=bs_update)
        article(bs=bs_update)
        for page in range(11):
            time.sleep(10)
            larrow_page = browser.find_element_by_xpath("//*[@id='larrow']")
            larrow_page.click()
            time.sleep(10)
            bs_update = BeautifulSoup(browser.page_source, "html.parser")
            issue_info(bs=bs_update)
            article(bs=bs_update)
    browser.close()

