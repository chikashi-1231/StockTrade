from pyquery import PyQuery
import time
import sqlite3


def get_brand(code):
    url = 'https://kabutan.jp/stock/?code={}'.format(code)

    q = PyQuery(url)

    if len(q.find('.stock_st_table')) == 0:
        return None

    try:
        name = q.find('')