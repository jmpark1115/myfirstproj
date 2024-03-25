"""
빗썸의 시세를 5초마다 조회한다.
조회한 결과를 텔레그램으로 알려준다.
"""
import requests
import time
import datetime

API_URL = "https://api.telegram.org/bot"
chat_id = ''
chat_token = ''

print("빗썸과 코인원의 시세를 조회합니다")

def seek_coin_value(coin='BTC'):
    url = "https://api.bithumb.com/public/ticker/" + coin +'_KRW'
    res = requests.get(url)
    ticker = res.json()
    coinValue = float(ticker['data']['closing_price'])
    return coinValue

def sendMessage(message):
    url = API_URL + chat_token + "/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    resp = requests.post(url, params=params)
    content = resp.json()
    return content

for i in range(10):
    coinValue = seek_coin_value('BTC')
    if coinValue:
        currentTime = datetime.datetime.now()
        # 현재 일시를 yyyy-mm-dd HH:MM:SS 형식으로 표기
        formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
        sendMessage("[{}] {:,.0f}" .format(formattedTime, coinValue))
    time.sleep(5)


