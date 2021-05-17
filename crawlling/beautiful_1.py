from bs4 import BeautifulSoup

# 크롤링: 전체 다
# 스크레이핑: 일부만
#
# BeautifulSoup: HTML, XML 만 분석하는 도구
# 1. 스크레이핑하는 패키지
# 2. HTML, XML 분석
# 3. 자체로 다운로드하는 기능이 없음

html = """
<html><body>
    <h1>스크래핑이란</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# 파싱된 문서를 soup 에 저장
soup = BeautifulSoup(html, 'html.parser')

# soup 에 있는 태그 중 html 태그 선택
# html 태그에서 body 태그 선택
# body 태그에서 h1 태그 선택해서 h1 변수에 담음
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 첫 번째의 next_sibling 에서는 </p>뒤에 있는 줄바꿈 또는 공백이 추출
# 이도 하나의 노드(엘리먼트)로 보기 떄문에
# next_sibling 을 한 번 더 사용해서 추출
print('h1 :', h1.string)
print('p1 :', p1.string)
print('p2 :', p2.string)
