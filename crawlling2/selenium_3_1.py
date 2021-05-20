# naver 로그인 테스트
from selenium import webdriver

USER = ''
PASS = ''

driver = webdriver.Chrome('./driver/chromedriver.exe')
url_login = 'https://nid.naver.com/nidlogin.login'
driver.get(url_login)
print('로그인 페이지에 접근!')

e = driver.find_element_by_id('id')
e.clear()
e.send_keys(USER)
e = driver.find_element_by_id('pw')
e.clear()
e.send_keys(PASS)


form = driver.find_element_by_css_selector('input.btn_global[type=submit]')
form.submit()
print('로그인 버튼 클릭')

driver.get('https://order.pay.naver.com/home?tabMenu=SHOPPING')
products = driver.find_element_by_css_selector(".p_info_span")
print(products)
for product in products:
    print("--", product.text)