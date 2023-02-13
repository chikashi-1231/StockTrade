from abc import ABC
from sql.models.database import *
from sql.models.models.stockmodel import *
from injector import inject
from ..batch_config import IConfig

class Analyze(ABC):
    @inject
    @abstractmethod
    def __init__(self, conf:IConfig):
        self.conf = conf
        self.logger = self.conf.get_logger(self, "defaultLogger")
        self.errlogger = self.conf.get_logger(self, "errorLogger")

class Fundamental_Analyze(Analyze):
    """
    ファンダメンタル分析
    """
    def __init__(self, conf: IConfig):
        super().__init__(conf)

    def find_growing(self):
        """
        成長株の分析
        """
        self.logger.info("")
        pass
        
    def find_bargain(self):
        """
        割安株の分析
        """
        self.logger.info("")
        pass

    def find_revival(self):
        """
        復活株の分析
        """
        self.logger.info("")
        pass

class Technical_Analyze(Analyze):
    def __init__(self, conf: IConfig):
        super().__init__(conf)