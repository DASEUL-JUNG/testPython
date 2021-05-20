# 다나와 사이트 - 내 계정의 관심 상품 목록 가져오기
from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://www.danawa.com/')

# 다나와 메인화면의 로그인 버튼 누르는 작업
login = driver.find_element_by_css_selector('li.my_page_service > a')
login.click()
driver.implicitly_wait(10)

# id/pw 입력하고 로그인하기 버튼 누르는 작업 실행
my_id = 'dasul1021'
my_pw = 'tkfqowk93*#'

driver.find_element_by_id('danawa-member-login-input-id').send_keys(my_id)
driver.implicitly_wait(10)
# driver.find_element_by_name('password').send_keys(my_pw)
driver.find_element_by_css_selector('input#danawa-member-login-input-pwd').send_keys(my_pw)
driver.implicitly_wait(10)
driver.find_element_by_css_selector('button.btn_login').click()
driver.implicitly_wait(10)

# 관심상품 목록 HTML 페이지 가져오기
wishlist = driver.find_element_by_css_selector('li.interest_goods_service > a').click()
driver.implicitly_wait(10)
html_src = driver.page_source
driver.close()
print(html_src[:500])
print()

# 관심상품 목록 HTML 페이지를 BeautifulSoup으로 파싱
from bs4 import BeautifulSoup
import urllib.request as req
import re
# url = 'http://www.danawa.com/myPage/wishList.php'
# res = req.urlopen(url)
soup = BeautifulSoup(html_src, 'html.parser')
#wishProductListArea
wish_table = soup.select('#wishProductListArea')
print(wish_table)
# wish_table = soup.select('table.tbl wish_tbl')[0]
wish_items = wish_table.select('tbody tr')
# wish_table = soup.select_one('#wishProductListArea > table').string

# for item in wish_items:
#     title = item.find('div', {'class': 'tit'}).text
#     price = item.find('span', {'class': 'price'}).text
#     # http: // prod.danawa.com / info /?pcode = 12660491
#     link = item.find('a', href=re.compile("prod.danawa.com/info/")).get('href')
#     print(title)
#     print(price)
#     print(link)
#     print()




