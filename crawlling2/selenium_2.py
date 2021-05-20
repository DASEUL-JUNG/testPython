from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)
driver.get('http://www.danawa.com/')

# 다나와 메인화면의 로그인 버튼을 누르는 작업 실행
login = driver.find_element_by_css_selector('li.my_page_service > a')

print('HTML 요소:', login)
print('태그 이름:', login.tag_name)
print('문자열:', login.text)
print('href 속성:', login.get_attribute('href'))

login.click()
driver.implicitly_wait(3)

# id/pw 입력하고 로그인하기 버튼 누르는 작업 실행
my_id = 'dasul1021'
my_pw = 'tkfqowk93*#'

driver.find_element_by_id('danawa-member-login-input-id').send_keys(my_id)
driver.implicitly_wait(2)
# driver.find_element_by_name('password').send_keys(my_pw)
driver.find_element_by_css_selector('input#danawa-member-login-input-pwd').send_keys(my_pw)
driver.implicitly_wait(2)
driver.find_element_by_css_selector('button.btn_login').click()
