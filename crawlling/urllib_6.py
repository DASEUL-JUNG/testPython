import urllib.request

url = 'http://192.168.1.9:8088/springBoard/img/showimg/cal_1.png'

savename = "./data/caltest.png"
# data 디렉토리 없으면 만들어놓기

urllib.request.urlretrieve(url, savename)
print('저장 완료되었습니다.')