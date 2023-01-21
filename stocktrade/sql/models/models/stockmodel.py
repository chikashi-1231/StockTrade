from abc import ABCMeta, abstractmethod

class Stock(metaclass=ABCMeta):
    """
    株の抽象クラス
    """
    def __init__(self) -> None:
        pass

class Growing_Stock(Stock):
    """
    成長株
    """

class Bargain_Stock(Stock):
    """
    割安株
    """

class Revival_Stock(Stock):
    """
    復活株
    """