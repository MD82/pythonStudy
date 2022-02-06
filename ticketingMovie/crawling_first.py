import requests

url = 'http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20220205'
html = requests.get(url)
print(html.text)