from bs4 import BeautifulSoup
import urllib.request as req

# 크롤링: 전체 다
# 스크레이핑: 일부만
#
# BeautifulSoup: HTML, XML 만 분석하는 도구
# 1. 스크레이핑하는 패키지
# 2. HTML, XML 분석
# 3. 자체로 다운로드하는 기능이 없음

url = 'http://192.168.1.9:8088/springBoard/crawling/beautiful_1.html'
res = req.urlopen(url)

# 파싱된 문서를 soup 에 저장
soup = BeautifulSoup(res, 'html.parser')

# soup 에 있는 태그 중 html 태그 선택
# html 태그에서 body 태그 선택
# body 태그에서 h1 태그 선택해서 h1 변수에 담음
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
p3 = p2.next_sibling.next_sibling
span = soup.html.body.span

print(type(span))

# 첫 번째의 next_sibling 에서는 </p>뒤에 있는 줄바꿈 또는 공백이 추출
# 이도 하나의 노드(엘리먼트)로 보기 떄문에
# next_sibling 을 한 번 더 사용해서 추출
print('h1 :', h1.string)
print('p1 :', p1.string)
print('p2 :', p2.string)
print('p3 :', p3.string)
print('span :', span.string)
