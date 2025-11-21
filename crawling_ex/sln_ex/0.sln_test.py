from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import time

# 서비스 객체 생성
Service = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service = Service)
chrome.get("http://naver.com")   # page를 가져옴

# time.sleep(10)  # 3초 기다림
# chrome.implicitly_wait(3) 
#크롬드라이브와 통신하는 지점에서 delay
#지정 요소가 로딩 될 때까지 기다림 예시 : 최대 10 초 기다림
WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
"input[name=query]")))
chrome.close()