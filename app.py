"""
郵便番号7桁(0287111)を入力したら
岩手県八幡平市大更が出力される

python app.py
郵便番号<ハイフン無し>は？ 0287111
岩手県八幡平市大更
"""

import requests

# pos_code = input("郵便番号<ハイフン無し>は？")
pos_code = "0287111"

response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={pos_code}")

dic = response.json()
print(dic)

# print(f"{dic['results'][0]['address1']}{dic['results'][0]['address2']}{dic['results'][0]['address3']}")
pref_name = dic['results'][0]['address1']
city_name = dic['results'][0]['address2']
town_name = dic['results'][0]['address3']

print(f"{pref_name}{city_name}{town_name}")
