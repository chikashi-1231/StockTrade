from abc import ABCMeta, abstractmethod

class Excellent_Stock(metaclass=ABCMeta):
    """
    株の抽象クラス
    """
    def __init__(self) -> None:
        pass

class Growing_Stock(Excellent_Stock):
    """
    成長株
    """

class Bargain_Stock(Excellent_Stock):
    """
    割安株
    """

class Revival_Stock(Excellent_Stock):
    """
    復活株
    """