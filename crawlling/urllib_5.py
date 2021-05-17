import sys
import urllib.request
import urllib.parse

# 명령행 인수 받기
if len(sys.argv) <= 1:
    print("USAGE: urllisb_5 <Region Number>")
    sys.exit()
RegionNumber = sys.argv[1]

# 대문자로 변수 선언 - 상수 의미
API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

# stnId: 기상정보 지역 변수 이름
# 전국: 108
# 서울/경기도: 109
# 강원도: 105
# 충청북도: 131
# 충청남도: 133
# 전라북도: 146
# 전라남도: 156
# 경상북도: 143
# 경상남도: 159
# 제주특별자치도: 184
values = {'stnId':RegionNumber}
params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url : ", url)

data = urllib.request.urlopen(url).read()
text = data.decode("UTF-8")
print(text)