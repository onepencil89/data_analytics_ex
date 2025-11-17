from bs4 import BeautifulSoup
import datetime
import urllib.request as req

# 
url = 'https://finance.naver.com/marketindex/'
html = req.urlopen(url)

# html 파싱하기
soup = BeautifulSoup(html, 'html.parser')

#원하는 데이터 추출
# 'div.head_info > span.value'  > 자식표시
# 'div.head_info  span.value'  > 자손
price = soup.select_one('div.head_info > span.value').string
print('usd/krw', price)


price = price.replace(',','')

# 현재 날짜/시간 가져오기
t = datetime.datetime.today()

print(' date :', t)
base_path = 'dollar_date'
import os
os.makedirs(base_path, exist_ok=True)


#date, 시간 포맷
getdate = t.strftime('%Y-%m-%d-%H')

fname = f"{base_path}/{getdate}.csv"
with open(fname, 'a', encoding='utf-8') as f:
    f.write(getdate + ',' +price + '\n')

# 환율 계산기
# 사용자로부터 원화 입력 -> 달러로 변환
won = input("원화를 입력하세요 :${price}원 -> ")
won = float(won)
dollar = won / float(price)
print(f"${won}원은  ${dollar:.2f}달러입니다.")