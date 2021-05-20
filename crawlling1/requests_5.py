import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
res = requests.get(url)
html_src = res.text

soup = BeautifulSoup(html_src, 'html.parser')

target_img = soup.find(name='img', attrs={'alt': 'Seoul-Metro-2004-20070722.jpg'})
print('target_img:', target_img)
print()

target_img_src = target_img.get('src')
print('이미지 파일 경로:', target_img_src)
print()

target_img_res = requests.get('http:' + target_img_src)
out_file_path = './data/download_image.jpg'

with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_res.content)
    print('이미지 파일 저장 완료!')
