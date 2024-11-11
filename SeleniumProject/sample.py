"""
https://github.com/GoogleChromeLabs/chrome-for-testing/blob/main/data/latest-versions-per-milestone-with-downloads.json
위의 주소 접속 후 본인의 크롬 버전과 맞는 버전을 참고 본인의 운영체제(win64)에 맞는 url을 복사한다
그런 다음 주소창에 붙여넣기 해서 이동하면 자동으로 크롬드라이버가 다운로드된다.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 웹 드라이버 경로 설정 (ChromDriver의 실제 경로로 수정)
# chrome_driver_path = 'D:\\chromedriver-win64'


# Chrome 옵셜 설정 (브라우저 창을 보이제 않게 실행하려면 options 추가)
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # 브라우저 창을 표시하지 않음

# 웹 드라이버 서비스 생성
service = Service()

# 웹 드라이버 객체 생성
driver = webdriver.Chrome(service=service, options=options)

try:
    # 접속할 URL
    url = 'https://www.naver.com/'
    driver.get(url)

    # 페이지가 완전히 로드될 때까지 대기 (필요에 따라 조정)
    time.sleep(5) #예: 5초 대기

    # 특정 요소 찾기(예: 페이지의 특정 테스트)
    element = driver.find_element(By.XPATH, '//h1') # XPATH를 사용하여 요소 찾기
    print(element.text)

    # 페이지의 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup과 함꼐 서용하여 추가적인 파싱 가능
    # from bs4 import BeautifulSoup
    # soup = BeautifulSoup(page_source, 'html.parser')
    # 원하는 데이터 추출

finally:
    # 브라우저 닫기
    driver.quit()