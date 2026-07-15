import requests

BOT_TOKEN = "8873362212:AAG-XXXXXXXXXXXXXXXXXXXXXX"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# the following two statements were written to get the chat id of the Telegram bot conversation
# response = requests.get(f"{BASE_URL}/getUpdates")
# print(response.json())

CHAT_ID = "5536041XXXx"

payload = {"chat_id": CHAT_ID,"text": "Hello from Python!"}
response = requests.post(f"{BASE_URL}/sendMessage",json=payload)

print(response.json())