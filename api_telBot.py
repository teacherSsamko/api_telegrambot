import urllib.request
import json

import telegram


# API 요청 
url = '' #api 요청 url
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    # response_body = json.loads(response_body) # json 처리
else:
    error_msg = f'Error Code: {rescode}'

# API로 받은 내용을 처리하는 코드



msg = '' # 처리한 내용을 담아서 보낼 변수


# TelegramBot으로 Message 보내기
telegram_token = '' # telegramBot token
telegram_id = '' # telegram chat_id
tel_bot = telegram.Bot(token=telegram_token)
tel_bot.sendMessage(chat_id=telegram_id, text=msg)