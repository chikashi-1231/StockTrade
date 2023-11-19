from sql.models.models.stockmodel import *
from . import Common_Fund_Analyze

class Fund_Growing_Analyze(Common_Fund_Analyze):
    """
    成長株のファンダメンタル分析
    """
    def __init__(self):
        pass
    
    def extract(self):
        """
        ファンダメンタル分析を行い、成長株を抽出する
        """
        # 過去10年の売上高、経常利益が常に増加傾向にあることをチェック
        dataFrame = dataFrame.sort_values("symbol_id").sort_values("year", ascending=True)
        dataFrame = dataFrame(dataFrame.groupby("symbol_id")["sales"].is_monotonic_increasing)
        dataFrame = dataFrame(dataFrame.groupby("symbol_id")["ordinary_income"].is_monotonic_increasing)

        # 売上高、経常利益の増加スピードが鈍化していないかチェック