from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://www.kia.com/kr/vehicles/kia-ev/guide/faq"

def clean(s): 
    return " ".join((s or "").split())

driver = webdriver.Chrome()
driver.get(URL)

try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(1.0)

    rows = []

    # 1) 모든 질문 버튼(아코디언 토글) 찾기 — 접근성 속성 활용
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button[aria-controls]')
    for btn in buttons:
        q = clean(btn.text)
        if not q:
            continue

        # 2) 화면에 보이게 스크롤 + 클릭해서 펼치기(닫혀 있으면)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        time.sleep(0.2)
        if btn.get_attribute("aria-expanded") == "false":
            btn.click()
            time.sleep(0.3)

        # 3) 버튼의 aria-controls 값이 곧 답변 패널의 id
        panel_id = btn.get_attribute("aria-controls")
        if not panel_id:
            continue

        # 4) 해당 id의 패널 텍스트 추출(이렇게 해야 질문-답변이 1:1 매칭)
        panel = driver.find_element(By.ID, panel_id)
        a = clean(panel.text)

        if a:
            rows.append((q, a))

    # 5) 터미널에 출력
    if not rows:
        print("추출된 FAQ가 없습니다. (구조 변경/로딩 지연 가능성)")
    else:
        for i, (q, a) in enumerate(rows, 1):
            print(f"[{i}] Q: {q}")
            print(f"    A: {a}\n")

finally:
    driver.quit()
