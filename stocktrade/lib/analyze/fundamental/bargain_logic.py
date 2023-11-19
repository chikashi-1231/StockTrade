from sql.models.models.stockmodel import *
from . import Common_Fund_Analyze

class Fund_Bergain_Analyze(Common_Fund_Analyze):
    """
    割安株のファンダメンタル分析
    """
    def __init__(self):
        pass
    
    def extract(self):
        """
        ファンダメンタル分析を行い、割安株を抽出する
        """
        pass