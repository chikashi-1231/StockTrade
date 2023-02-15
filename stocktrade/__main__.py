from injector import Injector, InstanceProvider
from batch_config import IConfig, Config
from bin.analyze import *

def load_config(binder):
    binder.bind(IConfig, Config)

def main():
    injector = Injector(load_config)
    fund_analyze = injector.get(Fundamental_Analyze)
    fund_analyze.fundamental()
    # バッチ実行時の引数から、実行するバッチ処理を選択する
    # ログを記録
    return


if __name__ == "__main__":
    main()