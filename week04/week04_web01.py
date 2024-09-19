import urllib.request
import urllib.parse

api = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

station_id = input("지역코드 : ")
values = {'stnId':station_id}

url = api + '?' + urllib.parse.urlencode(values)
# print(url)

urls = urllib.request.urlopen(url).read()
print(urls)
