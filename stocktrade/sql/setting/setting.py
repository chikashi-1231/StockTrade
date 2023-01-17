import logging
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from batch_config import Config

logger = logging.getLogger()

conf = Config("develop")
connectionStr = f"{conf.load('database')}://{conf.load('user')}:{conf.load('password')}" \
    f"@{conf.load('host')}:{conf.load('port')}/{conf.load('dbname')}"

# DB接続するためのEngineインスタンス
ENGINE = create_engine(connectionStr, echo=True)

# DBに対してORM操作するときに利用
# Sessionを通じて操作を行う
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

# 各modelで利用
# classとDBをMapping
Base = declarative_base()