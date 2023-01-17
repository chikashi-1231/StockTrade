import logging
import sys
import psycopg2
from psycopg2 import Error
from batch_config import Config

class PostgresDB:
    def __init__(self, env):
        logger = logging.getLogger()

        conf = Config(env)
        connectionStr = f"{conf.load('database')}://{conf.load('user')}:{conf.load('password')}" \
        f"@{conf.load('host')}:{conf.load('port')}/{conf.load('dbname')}"

        try:
            connector =  psycopg2.connect(connectionStr)
            self.cursor = connector.cursor()
        except(Exception, Error) as err:
            logger.exception("PostgreSQLへの接続時のエラーが発生しました",err)
            sys.exit(1)
