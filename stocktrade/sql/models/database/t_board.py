from sqlalchemy import Column, Integer, String, DateTime, Sequence
from sql.setting.setting import ENGINE, Base
from datetime import datetime
import sys


class Board(Base):
    """
    時価情報・板情報
    """
    __tablename__ = 't_board'
    # 銘柄コード
    SymbolID = Column(Integer, Sequence('symbol_id_seq'), primary_key=True)
    # 銘柄名
    Name = Column(String(255), nullable=False)
    # 市場コード
    Exchange = Column(Integer)
    # 現値
    CurrentPrice = Column(Integer)
    # 現値時刻
    CurrentPriceTime = Column(DateTime, default=datetime.now, nullable=False)
    # 現値前値比較
    CurrentPriceChangeStatus = Column(Integer)
    # 現値ステータス
    CurrentPriceStatus = Column(Integer)
    CreatedTime = Column(DateTime, default=datetime.now, nullable=False)
    UpdatedTime = Column(DateTime, default=datetime.now, nullable=False)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)