#1. 라이브러리 로딩
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request as req
import csv, os

# htlm문서 가져오기

url = 'https://news.naver.com/section/101'
html = req.urlopen(url)

# soup 객체 만들기
soup = BeautifulSoup(html, 'html.parser')

# 뉴스 목록 추출
data_list = []

trs = soup.select('ul.sa_list > li')

for tr in trs:
    title = tr.select_one('strong.sa_text_strong').get_text()
    press = tr.select_one('div.sa_text_press').get_text()
    # print(press)
    data_list.append([title, press])

# print(len(data_list))

# 파일 저장
os.makedirs('naver_news', exist_ok=True)
file_path = f"naver_news/{datetime.today().strftime('%Y-%m-%d.csv')}"

with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['타이틀', '언론사'])  # 헤더 (선택)
    writer.writerows(data_list)            # 데이터

print(f"✅ 완료: {file_path}")
