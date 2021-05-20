import requests

# robots.txt 파일 내용을 확인한 후 크롤링해야 함
urls = ['https://www.naver.com/', 'https://www.python.org/']
filename = 'robots.txt'

for url in urls:
    file_path = url + filename
    print('file_path:', file_path)
    res = requests.get(file_path)
    print(res.text)
    print('\n')

'''
file_path: https://www.naver.com/robots.txt
User-agent: *
Disallow: /
Allow : /$ 



file_path: https://www.python.org/robots.txt
# Directions for robots.  See this URL:
# http://www.robotstxt.org/robotstxt.html
# for a description of the file format.

User-agent: HTTrack
User-agent: puf
User-agent: MSIECrawler
Disallow: /

# The Krugle web crawler (though based on Nutch) is OK.
User-agent: Krugle
Allow: /
Disallow: /~guido/orlijn/
Disallow: /webstats/

# No one should be crawling us with Nutch.
User-agent: Nutch
Disallow: /

# Hide old versions of the documentation and various large sets of files.
User-agent: *
Disallow: /~guido/orlijn/
Disallow: /webstats/

'''