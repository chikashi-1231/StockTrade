from abc import ABC, abstractmethod

class Excellent_Stock(ABC):
    """
    優良株の抽象クラス
    """
    def __init__(self, simbolid):
        self.simbolid = simbolid
        pass
    
    @property
    def simbolid(self):
        return self.simbolid
    
    @simbolid.setter
    def simbolid(self):
        return

class Growing_Stock(Excellent_Stock):
    """
    成長株
    """
    def __init__(self, simbolid):
        super().__init__(simbolid)
    
class Bargain_Stock(Excellent_Stock):
    """
    割安株
    """
    def __init__(self, simbolid):
        super().__init__(simbolid)

class Revival_Stock(Excellent_Stock):
    """
    復活株
    """
    def __init__(self, simbolid):
        super().__init__(simbolid)