import requests

url = "https://graph.facebook.com/v25.0/13XXXXXXXXX33/messages"
headers = {
    "Authorization": "Bearer <API-Key>",
    "Content-Type": "application/json",
}
data = {
    "messaging_product": "whatsapp",
    "to": "+91-XXXX-XXXX",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {"code": "en_US"},
    }
}
                  
response = requests.post(url, headers=headers, json=data, timeout=30)
print(response.json())