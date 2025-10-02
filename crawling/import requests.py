# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import time

# url = 'https://chargeinfo.ksga.org/front/statistics/evCar'
# # 웹 드라이버를 자동으로 설치하고 최신버전을 유지
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# # 사이트 접속
# driver.get(url)
# # driver.maximize_window() # 전체 화면으로 실행  옵션
# print('사이트 접속했습니다.')
# # 사이트가 로드될때까지 기다린다.
# time.sleep(3)

# # BeautifulSoup으로 현재 페이지 파싱
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # 테이블 선택
# table = soup.select_one("table.datatable")

# # 테이블 행 가져오기 (thead 제외하고 tbody만)
# rows = table.select("tbody tr")

# # 각 행의 열(td) 데이터 추출
# for row in rows:
#     cols = [col.get_text(strip=True) for col in row.select("td")]
#     print(cols)

# # 크롬 드라이버 종료
# driver.quit()

# # 가상환경 키고 pip install selenium webdriver-manager beautifulsoup4 lxml 이후에 사용

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome()

# 사이트 접속
driver.get("https://chargeinfo.ksga.org/front/statistics/evCar")
time.sleep(3)  # 페이지 로딩 대기

# 헤더(th) 가져오기
headers = driver.find_elements(By.CSS_SELECTOR, "table thead tr th")
header_names = [h.text.strip() for h in headers]

# 표 데이터 가져오기
rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

data = []
for row in rows:
    cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
    if cols:
        data.append(cols)

driver.quit()

# DataFrame 생성 (헤더 포함)
df = pd.DataFrame(data, columns=header_names)

# 확인
print(df.head())

# CSV 저장
df.to_csv("ev_car_stats_full_with_header.csv", index=False, encoding="utf-8-sig")
print("CSV 파일 저장 완료: ev_car_stats_full_with_header.csv")