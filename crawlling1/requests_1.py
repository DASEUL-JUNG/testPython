import requests

url = 'https://www.python.org/'

# header 가져오기
res = requests.get(url)
print('1\n', res)

# body 가져오기
html = res.text
print('2\n', html)
