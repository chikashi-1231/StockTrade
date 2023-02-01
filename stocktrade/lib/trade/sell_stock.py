import logging
from sql.models.models.stockmodel import *
from sql.models.models.trademodel import *
from sql.models.enums.enum_trade import *
from abc import ABCMeta, abstractmethod

class AB_Sell_Stock(metaclass=ABCMeta):
    """
    株を売る抽象クラス
    """
    def __init__(self) -> None:
        # ログの書き込み
        # 現在保有している株の取得
            # DBの保有株テーブル(t_holding_stock)から現在保有している株の情報を取得
            # Listの作成
                # ・銘柄コード
                # ・買ったときの株価
        # 保有している株の、現在価格を取得(API)
        pass

    def deal(prof_loss: Enum, info: SellingStock) -> None:
        pass

class Dev_Sell(AB_Sell_Stock):
    """
    株を売る(develop環境)
    """
    def __init__(self) -> None:
        pass

    def deal(prof_loss: Enum, info: SellingStock):
        # 売却用のAPIの実行は行わない
        # DBの更新
            # 売り注文(t_reserve_sell)のInsert
            # 売り約定(t_execute_sell)のInsert
                # 売却価格(SoldPrice) = 現在価格
        # ログの書き込み
        return

class Staging_Sell(AB_Sell_Stock):
    """
    株を売る(staging環境)
    """
    def __init__(self) -> None:
        pass

    def deal(prof_loss: Enum, info: SellingStock):
        # 売却用のAPIの実行は行わない
        # DBの更新
            # 売り注文(t_reserve_sell)のInsert
            # 売り約定(t_execute_sell)のInsert
                # 売却価格(SoldPrice) = 現在価格
        # ログの書き込み
        return

class Prod_Sell(AB_Sell_Stock):
    """
    株を売る(production環境)
    """
    def __init__(self) -> None:
        pass

    def deal(prof_loss: Enum, info: SellingStock):
        # 売却用のAPIの実行
        # DBの更新
            # 売り注文(t_reserve_sell)のInsert
            # 売り約定(t_execute_sell)のInsertは行わない ※約定しなければ売却したことにならない為
        # ログの書き込み
        return


