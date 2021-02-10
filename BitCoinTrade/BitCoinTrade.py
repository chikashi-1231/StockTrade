import requests
import json

# 取引所のステータス取得
endPoint = 'https://api.coin.z.com/public'
path     = '/v1/status'

resStatus = requests.get(endPoint + path)
resStatusJson = resStatus.json()
print(resStatusJson)

# 取引所が空いてるときには、取引を行う
if resStatusJson["data"]["status"] == "OPEN":
    # 今現在建玉を持っているか取得
    # テクニカル分析のサイトから、5分の
    
