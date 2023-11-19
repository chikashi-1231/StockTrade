from sql.models.models.stockmodel import *

class Common_Fund_Analyze(ABC):
    """
    優良株のファンダメンタル分析の共通クラス
    """
    def __init__(self):
        pass
    
    # def get_performance(self):
    #     """
    #     DBの企業一覧から、データを持ってきてデータセットにして渡す
    #     """
    #     performance = db.t_performence.where(t -> (t.SymbolID == company.SymbolID) && t.決算日 > datetime.now - 10 year)
    #     dataFrame = pd.DataFrame
    #     (
    #         {
    #             "symbol_id": performance.SymbolID,
    #             "year": performance.year,
    #             "sales": performance.sales,# 売上高
    #             "ordinary_income": performance.ordinary_income # 経常利益
    #         }
    #     )
    #     return dataFrame
    
    # @abstractmethod
    # def extract(self):
    #     pass

    # def upsert_db(self):
    #     # DBへ成長株としてInsertを行う
    #     db.insert()