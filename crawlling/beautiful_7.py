from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://ko.wikipedia.org/wiki/%ED%95%98%EB%8A%98%EA%B3%BC_%EB%B0%94%EB%9E%8C%EA%B3%BC_%EB%B3%84%EA%B3%BC_%EC%8B%9C'
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

a_list = soup.select('#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li > a')
# #mw-content-text > div > ul > li a 라고 지정해도 파싱 됨

for a in a_list:
    name = a.string
    print('-', name)
