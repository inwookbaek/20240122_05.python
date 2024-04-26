from bs4 import BeautifulSoup as bs
import urllib.request as req
import datetime

url = 'http://finance.naver.com/marketindex'
res = req.urlopen(url)
soup = bs(res, 'html.parser')

ex_currency = soup.select_one('#exchangeList > li.on > a.head.usd > h3 > span')
ex_rate = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# print(f'{ex_currency.string} = {ex_rate.string}')

# 파일저장
t = datetime.date.today()
fname = 'd:/lec/05.python/data/web/' + t.strftime("%Y_%m_%d") + ".txt"

with open(fname, 'w', encoding='utf-8') as f:
    f.write(f'{ex_currency.string} = {ex_rate.string}')
