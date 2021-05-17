from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 class="tclass" id="title">스크래핑이란</h1>
    <p id="body">웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# 파싱된 문서를 soup 에 저장
soup = BeautifulSoup(html, 'html.parser')

print('soup.prettify :', soup.prettify())

# BeautifulSoup 에서는
# HTML 구조의 루트 요소인 <html>에서부터
# . : 마침표, 링크 연산자를 사용해서 값에 접근할 수 있음
# soup.html.body.h1 과 같은 형태
title1 = soup.html.body.h1
print('title1 :', title1)
print('type(title1) :', type(title1))
print('type(title1.attrs) :', type(title1.attrs))
print("'id' in title1.attrs :", 'id' in title1.attrs)
print("title[id] :", title1['id'])

for key in title1.attrs.keys():
    print('key :', key)
    print('title1['+key+'] :', title1[key])


title = soup.find(id="title")
body = soup.find(id="body")

# 첫 번째의 next_sibling 에서는 </p>뒤에 있는 줄바꿈 또는 공백이 추출
# 이도 하나의 노드(엘리먼트)로 보기 떄문에
# next_sibling 을 한 번 더 사용해서 추출
print('#title :', title.string)
print('#body :', body.string)
