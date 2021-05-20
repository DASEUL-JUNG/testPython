# urllib.request, BeautifulSoup 사용

import urllib.request as req
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

print('type(soup):', type(soup))
print()

print('soup.head:', soup.head)
print()


print('soup.body:', soup.body)
print()

print('title 태그 요소:', soup.title)
print('title 태그 이름:', soup.title.name)
print('title 태그 문자열:', soup.head.title.string)
