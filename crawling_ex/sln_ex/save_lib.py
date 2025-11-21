import os
import csv
from datetime import datetime

def save_datas(movie_lists, head, data_keyword):
    folder = f'{data_keyword}_datas'
    os.makedirs(folder, exist_ok=True)
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d-%H_%M')
    filename = f'{folder}/movie_{timestamp}.csv'

    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(head)  # 헤더 (선택)
        writer.writerows(movie_lists)            # 데이터

        print('csv저장완료', filename)