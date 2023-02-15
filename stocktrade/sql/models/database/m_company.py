from sqlalchemy import Column, Integer, String, DateTime, Sequence
from sql.setting.setting import ENGINE, Base
from datetime import datetime
import sys


class Company(Base):
    """
    会社のマスタ情報
    """
    __tablename__ = 'm_company'
    # 銘柄コード
    SymbolID = Column(Integer, Sequence('symbol_id_seq'), primary_key=True)
    # 銘柄名
    Name = Column(String(255), nullable=False)
    # 市場コード
    Exchange = Column(Integer)
    # 業種コード
    BisCategory = Column(Integer)
    # 時価総額
    TotalMarketValue = Column(Integer)
    # 発行済み株式数（千株）
    TotalStocks = Column(Integer)
    # 売買単位
    TradingUnit = Column(Integer)
    # 決算期日
    FiscalYearEndBasic = Column(Integer)
    # 呼値グループ
    PriceRangeGroup = Column(String(25), nullable=False)
    CreatedTime = Column(DateTime, default=datetime.now, nullable=False)
    UpdatedTime = Column(DateTime, default=datetime.now, nullable=False)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)