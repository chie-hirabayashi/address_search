import requests

response = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

print(response)
print(response.text)
