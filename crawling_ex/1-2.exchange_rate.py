from bs4 import BeautifulSoup
import datetime
import urllib.request as req

# 
url = 'https://finance.naver.com/marketindex/exchangeList.naver'
html = req.urlopen(url)

# html 파싱하기
soup = BeautifulSoup(html, 'html.parser')


# tbody tr td-1, td-2

trs = soup.select('tbody > tr')
exchange_list = []
for tr in trs:
    title = tr.select_one('td.tit').get_text().strip()
    sale = tr.select_one('td.sale').get_text().strip()
    # print(f"{title} - {sale}")
    # print("-"*30)
    #list에 저장
    exchange_list.append(f"{title} , {sale} \n")

# 파일에 저장하기
t = datetime.datetime.today()

base_path = 'exchange_date'
import os
os.makedirs(base_path, exist_ok=True)

getdate = t.strftime('%Y-%m-%d-%H')

fname = f"{base_path}/{getdate}.csv"
with open(fname, 'a', encoding='utf-8') as f:
    f.write(str(exchange_list))