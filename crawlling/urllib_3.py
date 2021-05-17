import urllib.request

url = "http://api.aoikujira.com/ip/ini"
print("url :", url)

# 해당 url의 HTTPResponse 객체를 가져옴
res = urllib.request.urlopen(url)
print("res : ", res)

# HTTPResponse 객체를 읽어옴
data = res.read()
print("data :", data)
# print(type(data))

# bytes 객체를 str로 변환
text = data.decode("UTF-8")
print("text : ", text)
# print(type(text))