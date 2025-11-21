# 1. 라이브러리 로딩

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time  
import save_lib


# 2. 크롬 브라우저 옵션 정의
options = webdriver.ChromeOptions()             # 옵션 설정 객체 생성
options.add_argument("window-size=1000,1000")   # 브라우저 크기 설정(가로 x 세로)
options.add_argument("--no-sandbox")              # 샌드박스 사용 안하겠다. 텝별로 분리하겠다. 
options.add_argument("--disable-dev-shm-usage")  # 메모리 부족 방지
options.add_argument("headless")              # 크롬 창을 안뜨게함.
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 3-1. 크롬 웹 드라이브를 통한 크로브라우저 객체 생성(자동)  
# ChromeDriver 경로를 지정하는 Service 객체 생성
# service = Service(ChromeDriverManager().install())


# 3-2. 방법 1이 작동하지 않을때 수동설치 하는 방법
# 로컬에 다운로드한 chromedriver.exe 경로 지정
# https://googlechromelabs.github.io/chrome-for-testing/
service = Service('chromedriver_142/chromedriver.exe')

# 4. 크롬 브라우저 객체 생성 이후, 식별자 생성
chrome = webdriver.Chrome(service=service, options=options) 

# 5. 테이터 수집할 url
url = "https://www.kobis.or.kr/kobis/business/stat/boxs/findRealTicketList.do"


chrome.get(url)

time.sleep(1)

# 지정한 요소가 브라우저에 로딩될때까지 기다림, 최대 10초
wait = WebDriverWait(chrome, 10) 
def find(wait, css_selector):
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

# 초기화: 예외가 발생해도 함수 하단에서 변수 접근시 NameError 방지
movie_lists = []

try:
    # 6. 데이터 수집할 부분에 대한 검색 액션 수행
    ## 한국 영화만 선택, 해외 체크박스 해제 액션 지정
    # 셀렉터 지정방법 

    # ul.list_idx li input#repNationNoKor 
    # 또는
    # label[for='repNationNoKor']

    # find(wait, '셀렉터')

    # 지정 셀렉터 요소가 로딩될떄까지 기다리고, 로딩됨녀 요소 리턴
    # ul.list_idx li label[for='repNationNoKor']
    # ele = find(wait, 'ul.list_idx li input#repNationNoKor')

    ele = find(wait, "label[for='repNationNoKor']")
    # 로딩된 요소 클릭

    ele.click()

    time.sleep(1)


    # 조회버튼 로딩되면 클릭하기
    btn = find(wait, ".wrap_btn button.btn_blue")
    
    #임의 오류 발생하면....
    # btn = find(wait, ".wrap_btn button.btn_blue_A")
    btn.click()

    # 조회된 데이터에서 필요한 데이터 수집
    # 각 영화데이터를 LIST로 추출(tbody tr을 목록으로 추출)

    time.sleep(2)  # 로딩 될때까지 기다리는 시간
    items = chrome.find_elements(By.CSS_SELECTOR, "table.tbl_comm tbody tr")
    
    # print(items)     잘 되는지 확인.
    movie_lists = []
    # print('순서 : 영화제목 | 개봉일자 | 애매매출액 | 예매관객수')
    for item in items:
       title = item.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text.strip()
       open_date = item.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip()
       sales_price = item.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text.strip().replace('"','')
       sales_attendance = item.find_element(By.CSS_SELECTOR, "td:nth-child(7)").text.strip()

       if not open_date:
          open_date = 'None'

       movie_lists.append([title, open_date, sales_price, sales_attendance])
    #    print(f'{title} | {open_date} | {sales_price} | {sales_attendance}')
    #    print(movie_lists)

# time.sleep(2)

# print("-"*30)

except Exception as e:
    print('오류', e)

# 저장 함수 정의부


# 매번 바뀌는 값을 찾기


# file로 저장하기(csv)
data_keyword = 'movie'
head = ['영화제목', '개봉일자' , '애매매출액' , '예매관객수']

# 파일 저장 함수 호출
save_lib.save_datas(movie_lists, head, data_keyword)
print('-'*30)
chrome.close() # tab 모두 종료
chrome.quit() # tab 모두 종료
