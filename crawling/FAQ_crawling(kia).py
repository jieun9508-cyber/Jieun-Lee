# kia_ev_faq_print.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

URL = "https://www.kia.com/kr/vehicles/kia-ev/guide/faq"

def clean(s): 
    return " ".join((s or "").split())

# 1) 헤드리스 크롬 준비 (창 안 뜨게)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1280,2400")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 2) 페이지 열기
    driver.get(URL)
    time.sleep(2)  # 로딩 대기(간단히)

    # 3) 질문 버튼들 찾기 (접근성 속성 활용)
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button[aria-controls]')

    count = 0
    for btn in buttons:
        q = clean(btn.text)
        if not q:
            continue

        # 닫혀 있으면 클릭해서 열기
        if btn.get_attribute("aria-expanded") == "false":
            try:
                btn.click()
                time.sleep(0.2)
            except Exception:
                pass

        # 답변 영역 찾기 (aria-controls가 가리키는 id)
        panel_id = btn.get_attribute("aria-controls")
        if not panel_id:
            continue

        try:
            panel = driver.find_element(By.ID, panel_id)
            a = clean(panel.text)
        except Exception:
            a = ""

        if a:
            count += 1
            print(f"[{count}] Q: {q}")
            print(f"    A: {a}\n")

    if count == 0:
        print("추출된 FAQ가 없습니다. (동적 로딩/구조 변경 가능성)")

finally:
    driver.quit()
