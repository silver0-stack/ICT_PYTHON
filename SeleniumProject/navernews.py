from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import traceback
import cx_Oracle

# Chrome 옵션 설정
chrome_options = Options()
# 디버깅을 위해 헤드리스 모드 비활성화 (브라우저 창을 직접 확인할 수 있습니다)
# chrome_options.add_argument('--headless')  # 헤드리스 모드 활성화
chrome_options.add_argument('--disable-gpu')  # GPU 사용 안함
chrome_options.add_argument('--no-sandbox')  # 권한 관련 문제 방지
chrome_options.add_argument('--disable-dev-shm-usage')  # 리소스 문제 방지

# 웹 드라이버 서비스 생성 및 드라이버 자동 관리
service = Service(ChromeDriverManager().install())

# 웹 드라이버 객체 생성
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 네이버 뉴스 IT/과학 섹션 주소
    driver.get('https://news.naver.com/section/105')

    # 페이지가 완전히 로드될 때까지 대기
    wait = WebDriverWait(driver, 15)  # 최대 10초 대기

    # 최신 뉴스 제목 요소가 로드될 때까지 대기
    # CSS Selector 예시: 'a.sa_text_title._NLOG_IMPRESSION'
    # 클래스가 sa_text_title과 _NLOG_IMPRESSION인 <a> 태그를 정확히 선택한다.
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.sa_text_title._NLOG_IMPRESSION')))

    # 뉴스 제목 요소 가져오기
    news_elements = driver.find_elements(By.CSS_SELECTOR, 'a.sa_text_title._NLOG_IMPRESSION')

    # 디버깅: 요소가 제대로 선택되었는지 확인
    print(f"찾은 뉴스 요소 수: {len(news_elements)}")  # 디버깅용 출력

    if len(news_elements) == 0:
        # 스크린샷 저장 (디버깅 용도)
        driver.save_screenshot('screenshot.png')
        # 페이지 소스 저장 (디버깅 용도)
        with open('page_source.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        print("뉴스 요소를 찾지 못했습니다. 스크린샷과 페이지 소스를 확인하세요.")
    else:
        data = []
        for news in news_elements:
            try:
                title = news.text.strip()
                link = news.get_attribute('href').strip()
                print(f"제목: {title}\n링크: {link}\n")  # 링크 확인을 위한 출력
                if title and link:
                    data.append({
                        'Title': title,
                        'Link': link
                    })
            except Exception as e:
                print(f"개별 뉴스 항목 처리 중 오류: {e}")
                traceback.print_exc()
                continue

        # 데이터프레임으로 변환
        # 뉴스 링크의 긴 링크를 잘리지 않고 콘솔에 출력시키기 위해서 옵션 조정
        pd.set_option('display.max_colwidth', None)
        df = pd.DataFrame(data)
        print(df)

        # CSV 파일로 저장
        df.to_csv('naver_news_title.csv', index=False, encoding='utf-8-sig')

except Exception as e:
    print(f"오류 발생: {e}")
    traceback.print_exc()
finally:
    # 브라우저 닫기
    driver.quit()
