from pyquery import PyQuery

q = PyQuery('https://kabutan.jp/stock/?code=7203')
sector = q.find('title')[0].text
print(sector)