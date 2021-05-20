from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 통계지표 검색어를 입력하여 CSV 파일로 저장
def download_bok_statistics_by_keyword():

    item_found = 0
    while not item_found:
        # 검색어 초기화
        keyword = ''
        while len(keyword) == 0:
            keyword = str(input('검색할 항목 입력하세요.: '))

        # 웹 드라이버 실행
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.implicitly_wait(3)
        driver.get('http://ecos.bok.or.kr/jsp/vis/keystat/#/key')
        time.sleep(5)
        # body > div.HSwrap.ng - scope > div.HScontainer > div > div > div: nth - child(4) > div > div:nth - child(
            # 1) > div.HSthemeA > table > tbody > tr: nth - child(1) > th > span > a
        items1 = driver.find_element_by_css_selector('a[class="ng-binding"]')
        items2 = driver.find_element_by_css_selector('a[class="a-c1-list ng-binding"]')
        items3 = driver.find_element_by_css_selector('a[class="a-c4-list ng-binding"]')
        driver.implicitly_wait(3)

        items = items1[1:] + items2 + items3