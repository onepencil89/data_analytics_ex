#1. 라이브러리 로딩
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request as req
import csv, os

url = 'https://news.ycombinator.com/'
html = req.urlopen(url)

# soup 객체 만들기
soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

boxes = soup.select('table tr.athing.submission')


# print(box)

for box in boxes:
    title = box.select_one('td.title a').get_text()
    print(title)