import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
res = requests.get(url)
html_src = res.text

soup = BeautifulSoup(html_src, 'html.parser')

first_img = soup.find(name='img')
print('first_img:', first_img)
print()

target_img = soup.find(name='img', attrs={'alt': 'Seoul-Metro-2004-20070722.jpg'})
print('target_img:', target_img)
