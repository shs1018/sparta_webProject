from bs4 import BeautifulSoup
from selenium import webdriver
import time

from pymongo import MongoClient

client = MongoClient('여기에 URL 입력')
db = client.dbsparta

driver = webdriver.Chrome('chromedriver')

driver.get("https://www.pinterest.co.kr/HueMemo/%EC%98%A4%EB%8A%98%EC%9D%98-%EB%AA%85%EC%96%B8thought-of-the-day/")

req = driver.page_source  # 데이터를 피싱 용이한 html로
soup = BeautifulSoup(req, 'html.parser')

block_list = soup.select('#boardfeed\:320177923447578825 > div > div:nth-child(1) > div')
site_list = []

for i in range(10):  # 10번 반복
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")  # 가장 위부터 어느정도 아래까지만 - @
    for block in block_list:
        site_addr = block.select_one('a')['href']
        site_list.append(site_addr)  # /pin/3298432897
    time.sleep(2)  # 시간차를 준다


#들어가서 메인이미지만 긁어오는 과정 필요함

for i in site_list:
    driver.get("https://www.pinterest.co.kr" + i)

    req2 = driver.page_source  # 데이터를 피싱 용이한 html로
    soup = BeautifulSoup(req2, 'html.parser')

    block_list2 = soup.select("")
    site_lst2 = []


driver.quit()
