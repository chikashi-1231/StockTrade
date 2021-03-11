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
    # テクニカル分析のサイトから、5分のステータスを取得
    # 今現在建玉を持っているか取得
    if 建玉を持っている場合:
        # 建玉を持っている場合
        # 損益を比較
        # 利益が出ている場合で、利益が10%を超えたら利確を行う
            # そして5分のステータスが買いなら買い注文、売りなら売り注文、それ以外ならちょっと置いとく
        # 利益が出ている場合で、利益が10%を超えていなかったら損切に訂正注文を入れる
            # 既に入っている注文より利益でなかったら、訂正注文は入れない
        # 損失が出ている場合、とりあえず何もしない
    else:
        # 建玉を持っていない場合
        # 5分のステータスが買いなら買い注文、売りなら売り注文、それ以外ならちょっと置いとく
        # DBにデータを書き込み