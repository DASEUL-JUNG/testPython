import urllib.request



url = "http://uta.pw/shodou/img/28/214.png"
savename = "./data/test01.png"
# data 디렉토리 없으면 만들어놓기

urllib.request.urlretrieve(url, savename)
print('저장 완료되었습니다.')