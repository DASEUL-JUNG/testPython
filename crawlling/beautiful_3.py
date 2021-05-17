from bs4 import BeautifulSoup

html = '''
<html><body>
    <ul>
        <li><a href="https://naver.com">naver</a></li>
        <li><a href="https://daum.net">daum</a></li>
    </ul>
    <a href="https://google.com">google</a>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')

for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, '>', href)

lis = soup.find_all('li')
for l in lis:
    print(l)
    print(l.string)
