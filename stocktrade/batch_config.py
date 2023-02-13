#!/usr/bin/env python3

from abc import ABC, abstractclassmethod
import sys, datetime
from typing import Any
import yaml
from logging import Logger, config, getLogger

class IConfig(ABC):
    @abstractclassmethod
    def get_logger(self, inputLogger) -> Logger:
        pass

    @abstractclassmethod
    def load(self, item:str) -> Any:
        pass

class Config(IConfig):

    def __init__(self, env = "develop"):
        self.env = env
        try:
            with open(f".conf/{self.env}.yaml") as file:
                self.config = yaml.safe_load(file)
        except Exception as e:
            print('Exception occurred while loading YAML...', file=sys.stderr)
            print(e, file=sys.stderr)
            sys.exit(1)

    def get_logger(self, inputLogger = "defaultLogger"):
        # ログのファイル名の設定
        log_category = "error" if inputLogger == "errorLogger" else ""
        self.config["log"]["handlers"]["fileHandler"]["filename"] = \
            f"./logs/{self.env}/stocktrade-{log_category}{format(datetime.date.today(), '%Y%m%d')}.log"
        config.dictConfig(self.config["log"])
        logger = getLogger(inputLogger)
        return logger

    def load(self, item:str):
        return self.config[item]