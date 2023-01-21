from sql.database import *
from sql.models.models.stockmodel import *
import pandas as pd
import time

class Fundamental():
    """
    ファンダメンタル分析
    """
    def __init__(self) -> None:
        pass
    def find_growing(self):
        """
        成長株の分析
        """
        # # DBの企業一覧から、データを持ってくる
        # performance = db.t_performence.where(t -> (t.SymbolID == company.SymbolID) && t.決算日 > datetime.now - 10 year)
        # dataFrame = pd.DataFrame
        # (
        #     {
        #         "symbol_id": performance.SymbolID,
        #         "year": performance.year,
        #         "sales": performance.sales,# 売上高
        #         "ordinary_income": performance.ordinary_income # 経常利益
        #     }
        # )
        # # 過去10年の売上高、経常利益が常に増加傾向にあることをチェック
        # dataFrame = dataFrame.sort_values("symbol_id").sort_values("year", ascending=True)
        # dataFrame = dataFrame(dataFrame.groupby("symbol_id")["sales"].is_monotonic_increasing)
        # dataFrame = dataFrame(dataFrame.groupby("symbol_id")["ordinary_income"].is_monotonic_increasing)

        # # 売上高、経常利益の増加スピードが鈍化していないかチェック

        # # DBへ成長株としてInsertを行う
        # db.insert()

    def find_bargain(self):
        """
        割安株の分析
        """
        # db.insert()

    def find_revival(self):
        """
        復活株の分析
        """
        # db.insert()