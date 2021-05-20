import re
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
res = requests.get(url)
html_src = res.text

soup = BeautifulSoup(html_src, 'html.parser')

links = soup.find_all('a')
print('하이퍼링크 개수:', len(links))
print('첫 3개의 원소', links[:3])

wiki_links = soup.find_all(name='a', href=re.compile('/wiki/'), limit=3)
print('/wiki/ 문자열이 포함된 하이퍼 링크:', wiki_links)

external_links = soup.find_all(name='a', attrs={'class': 'external text'}, limit=3)
print('class 속성으로 추출한 하이퍼링크:', external_links)
