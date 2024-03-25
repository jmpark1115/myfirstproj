import requests

API_URL = "https://api.telegram.org/bot"

def get_updates():
    url = API_URL + chat_token + "/getUpdates"
    resp = requests.get(url)
    return resp.json()

def sendMessage(message):
    url = API_URL + chat_token + "/sendMessage"
    params = {
              "chat_id": chat_id,
              "text": message
    }
    resp = requests.post(url, params=params)
    content = resp.json()
    return content

chat_id    = ''
chat_token = ''
resp = get_updates() # chat_id 구하기
print(resp)
result = sendMessage("welcome to my telegram message service !!")
print(result)
