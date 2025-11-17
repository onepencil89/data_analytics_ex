from bs4 import BeautifulSoup
import datetime
import urllib.request as req
import csv

# Step 1~2: URL 가져오기 및 파싱
url = 'https://finance.naver.com/marketindex/exchangeList.naver'
html = req.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# Step 3: 데이터 추출 (리스트의 리스트 형태)
trs = soup.select('tbody > tr')
exchange_list = []

for tr in trs:
    title = tr.select_one('td.tit').get_text().strip()
    sale = tr.select_one('td.sale').get_text().strip()
    
    # 리스트 형태로 저장
    exchange_list.append([title, sale])

# Step 4: 파일명 생성
t = datetime.datetime.today()
base_path = 'exchange_date'

import os
os.makedirs(base_path, exist_ok=True)

getdate = t.strftime('%Y-%m-%d-%H')
fname = f"{base_path}/{getdate}.csv"

# Step 5: CSV writer로 저장
with open(fname, 'w', newline='', encoding='utf-8-sig') as f:
    # csv.writer 사용 (딕셔너리가 아닌 리스트용)
    writer = csv.writer(f)
    
    # 헤더 직접 작성
    writer.writerow(['국가명', '환율'])
    
    # 모든 데이터 한 번에 작성
    writer.writerows(exchange_list)  # writerows (복수형) 주의!

print(f"✅ CSV 파일 저장 완료: {fname}")