# request, BeautifulSoup 사용

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
res = requests.get(url)
html_src = res.text

soup = BeautifulSoup(html_src, 'html.parser')

print('type(soup):', type(soup))
print()

print('soup.head:', soup.head)
print()


print('soup.body:', soup.body)
print()

print('title 태그 요소:', soup.title)
print('title 태그 이름:', soup.title.name)
print('title 태그 문자열:', soup.head.title.string)

print(soup.div)
