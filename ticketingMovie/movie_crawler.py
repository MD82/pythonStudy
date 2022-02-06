import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220215'
html = requests.get(url)
# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')

if(imax):
    print('IMAX가 열렸습니다')
else :
    print('IMAX가 열리지 않았습니다')