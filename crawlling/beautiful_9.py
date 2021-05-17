from bs4 import BeautifulSoup

fp = open('beautisoup_frvege.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

# 2번째 ul 태그의 4번째 li 태그
print(soup.select_one('ul:nth-of-type(2) > li:nth-of-type(4)').string)
print(soup.select_one('#vg-list > li:nth-of-type(4)').string)
print(soup.select('#vg-list > li[data-lo="us"]')[1].string)
print(soup.select('#vg-list > li.black')[1].string)

cond = {'data-lo': 'us', 'class': 'black'}
print(soup.find('li', cond).string)

print(soup.find(id='vg-list').find('li', cond).string)
