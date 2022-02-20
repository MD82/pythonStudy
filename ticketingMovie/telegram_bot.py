import telegram

bot = telegram.Bot(token = '5174003066:AAGVQu9i9H0A6t6nbxxU_qKeRVuY9XHzZ4g')

#for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id= 5295011140,text="테스트입니다.")