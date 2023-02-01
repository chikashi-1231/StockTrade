from sql.models.database import *
from sql.models.models.stockmodel import *
from sql.models.enums.enum_trade import *
import pandas as pd
import time

def trade():
    # 取引余力の確認
    # 株を買う
        # 成長株の取引
            # DBの優良株テーブル(t_excellent_stock)から成長株を取得
        # 割安株の取引
            # DBの優良株テーブル(t_excellent_stock)から割安株を取得
        # 復活株の取引
            # DBの優良株テーブル(t_excellent_stock)から復活株を取得
    # 株を売る
        # AB_Sell_Stockクラスをインスタンス化。コンストラクタで下記の処理が行われる
            # 現在保有している株の取得
                # DBの保有株テーブル(t_holding_stock)から現在保有している株の情報を取得
                # Listの作成
                    # ・銘柄コード
                    # ・買ったときの株価
            # 保有している株の、現在価格を取得(API)
        # 損切り
            # 買った時の価格より、現在価格が5%以上下がっていたら損切りを行う
                # 損切りを行う株のListを作成(lossStockList: SellingStock)
                    # ・銘柄コード
                    # ・売却数
                    # ・（売却価格）
            # dealのメソッドを実行(Enumで、ProfitLossの損切りを引数にする)
                # AB_Sell_Stock.deal(ProfitLoss.損切り, lossStockList)
        # 利確
            # 買った時の価格より、現在価格が10%以上上がっていたら利確を行う
                # 利確を行う株のListを作成(ProfitStockList: SellingStock)
                    # ・銘柄コード
                    # ・売却数
                    # ・（売却価格）
            # dealのメソッドを実行(Enumで、ProfitLossの利確を引数にする)
                # AB_Sell_Stock.deal(ProfitLoss.損切り, ProfitStockList)
    return