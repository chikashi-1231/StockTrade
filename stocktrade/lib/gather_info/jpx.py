import re
import os, time, requests, urllib
import lxml.html
import pandas as pd
 
FILE_PATH = "EdinetcodeDlInfo.csv"
input_book = pd.ExcelFile('読み込むファイル名')
 
# 5桁の証券コードを4桁に変更（先頭4文字）
def scode_edit(val):
    return val[:4]
 
if __name__ == '__main__':

    # ＥＤＩＮＥＴコード,提出者名,証券コードを読み込む（合計3列）
    df = pd.read_csv(FILE_PATH, encoding="cp932", usecols=[0, 6, 11], names=('edinet_code', 'name', 'syoken_code'), dtype={"syoken_code": str}, skiprows=2)

    # 証券コードが欠損値（NaN）である行を削除
    df = df.dropna(how='any', axis=0)
    # 出力用のデータフレーム作成
    df_ex = df.copy()
    df_ex["security_code"] = df_ex["syoken_code"].apply(scode_edit)

    # csv出力
    df_ex.to_csv("output.csv", index=False)

jpx_url = "https://www.jpx.co.jp/markets/statistics-equities/misc/01.html"

class JPX():
    """
    東証上場銘柄一覧のExcelファイルを取得し、その内容をDBに格納する。
    """
    def __init__(self):
        pass

    def fetch(self):
        """
        東証上場銘柄一覧のExcelファイルを取得し、その内容をDataFrameにする
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }
        html = requests.get(jpx_url, headers=headers).text
        # [TODO] class="component-file"の部分をrequestsで取得
        dom = lxml.html.fromstring(html)
        excel_url = dom.xpath("//div[@class='component-file']/@src")
        response = requests.get(excel_url)
        return ""
    
    def upsertdb(self):
        # db.insert
        pass