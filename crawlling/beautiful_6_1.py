from bs4 import BeautifulSoup
import urllib.request as req
import datetime

# 파일 이름: 날짜
# 환율 정보를 txt 파일로 저장

url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

price = soup.select_one('div.head_info > span.value').string
print('usd/krw =', price)

t = datetime.date.today()
frame = './data/' + t.strftime('%Y-%m-%d-%A') + '.txt'

with open(frame, 'w', encoding='utf-8') as f:
    f.write(price)
