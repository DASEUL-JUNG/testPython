from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
            <ul class="items">
                <li>유니트 게임 이팩트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인 정석</li>
            </ul>
        </div>
    </body>
</html>
"""

# soup.select_one(선택자): CSS 선택자로 요소 하나를 추출
# soup.select(선택자): CSS 선택자로 요소 여러개를 리스트로 추출

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one('div#meigen > h1').string
print('h1 :', h1)

li_lit = soup.select('div#meigen > ul.items > li')
for li in li_lit:
    print('li :', li.string)
