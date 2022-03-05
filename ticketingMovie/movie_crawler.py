from inspect import BlockFinder
import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '5174003066:AAGVQu9i9H0A6t6nbxxU_qKeRVuY9XHzZ4g')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220308'

def job_function():
    html = requests.get(url)
    # print(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')

    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        
        bot.sendMessage(chat_id= 5295011140,text=title + ' IMAX가 열렸습니다.')
        sched.pause()
        #print(title + ' IMAX가 열렸습니다')
    else :
        bot.sendMessage(chat_id= 5295011140,text='IMAX가 아직 열리지 않았습니다')
        #print('IMAX가 열리지 않았습니다')

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()