import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220205'
html = requests.get(url)
# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
# print(soup.select_one('.sect-showtimes > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > strong:nth-child(1)'))
title_list = soup.select('div.info-movie')

for i in title_list:
    print(i.select_one('a > strong').text.strip())
