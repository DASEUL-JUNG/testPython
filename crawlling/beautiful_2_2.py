from bs4 import BeautifulSoup
import urllib.request as req

# tomcat 서버로 실행한 html 파일 읽어오기
url = 'http://192.168.1.9:8088/springBoard/crawling/beautiful_2.html'
res = req.urlopen(url)

# 파싱된 문서를 soup 에 저장
soup = BeautifulSoup(res, 'html.parser')

title = soup.find(id="title")
body = soup.find(id="body")
s = soup.find(id="s")

# 첫 번째의 next_sibling 에서는 </p>뒤에 있는 줄바꿈 또는 공백이 추출
# 이도 하나의 노드(엘리먼트)로 보기 떄문에
# next_sibling 을 한 번 더 사용해서 추출
print('#title :', title.string)
print('#body :', body.string)
print('#s :', s.string)
