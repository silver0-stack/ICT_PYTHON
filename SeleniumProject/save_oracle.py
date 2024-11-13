import cx_Oracle
import pandas as pd
import traceback
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import logging
import os
from dotenv import load_dotenv
import sys

# 환경 변수 로드
load_dotenv()

# 로깅 설정: 파일과 콘솔 모두에 출력 (UTF-8 인코딩)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 파일 핸들러 설정 (UTF-8 인코딩)
file_handler = logging.FileHandler('save_oracle.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# 콘솔 핸들러 설정 (UTF-8 인코딩)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# 핸들러 추가
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def clean_data(df):
    """
    데이터프레임을 클렌징하는 함수
    - 중복 제거
    - 결측치 제거
    - 대소문자 통일
    - 특수문자 제거
    """
    # 'Link' 컬럼의 중복 제거
    df = df.drop_duplicates(subset=['Link'])
    logging.info(f"중복 제거 후 데이터 수: {len(df)}")

    # 결측치 제거: 제목이나 링크가 비어 있는 경우 제거
    df = df.dropna(subset=['Title', 'Link'])
    logging.info(f"결측치 제거 후 데이터 수: {len(df)}")

    # 대소문자 통일
    df['Title'] = df['Title'].str.title()

    # 특수문자 제거
    df['Title'] = df['Title'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

    return df


def analyze_and_visualize(df, show_plot=False):
    """
    데이터 분석 및 시각화를 수행하는 함수
    - 단어 빈도수 분석
    - 워드 클라우드 생성
    """
    # 한글 글꼴 설정 (맑은 고딕)
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

    # 단어 빈도수 분석
    words = ' '.join(df['Title']).split()
    word_counts = Counter(words)

    common_words = word_counts.most_common(20)
    words, counts = zip(*common_words)

    plt.figure(figsize=(10, 8))
    plt.bar(words, counts, color='skyblue')
    plt.xticks(rotation=45)
    plt.title("뉴스 제목의 Top 20 단어")
    plt.tight_layout()
    plt.savefig('top_words.png')  # 그래프를 이미지로 저장
    plt.close()
    logging.info("단어 빈도수 분석 및 시각화 완료. 'top_words.png'로 저장되었습니다.")

    # 워드 클라우드 생성 (맑은 고딕 글꼴 사용)
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=400,
                          background_color='white').generate(' '.join(df['Title']))

    plt.figure(figsize=(15, 7.5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("뉴스 제목 워드 클라우드")
    plt.tight_layout()
    plt.savefig('wordcloud.png')  # 워드 클라우드를 이미지로 저장
    plt.close()
    logging.info("워드 클라우드 생성 완료. 'wordcloud.png'로 저장되었습니다.")

    if show_plot:
        # 시각화를 콘솔에 표시 (테스트 용도)
        plt.figure(figsize=(10, 8))
        plt.bar(words, counts, color='skyblue')
        plt.xticks(rotation=45)
        plt.title("뉴스 제목의 Top 20 단어")
        plt.tight_layout()
        plt.show()

        wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=400,
                              background_color='white').generate(' '.join(df['Title']))
        plt.figure(figsize=(15, 7.5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("뉴스 제목 워드 클라우드")
        plt.tight_layout()
        plt.show()


def insert_into_oracle(df):
    """
    오라클 데이터베이스에 데이터를 삽입하는 함수
    - 중복 삽입 방지를 위해 MERGE 문 사용
    """
    # 오라클 데이터베이스 연결 정보
    dsn_tns = cx_Oracle.makedsn(
        os.getenv('ORACLE_HOST'),
        os.getenv('ORACLE_PORT'),
        service_name=os.getenv('ORACLE_SERVICE_NAME')
    )
    username = os.getenv('ORACLE_USERNAME')
    password = os.getenv('ORACLE_PASSWORD')

    connection = None
    cursor = None

    try:
        # 데이터베이스 연결
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)
        cursor = connection.cursor()
        logging.info("오라클 데이터베이스에 성공적으로 연결되었습니다.")

        # MERGE 문을 사용하여 중복된 링크를 무시하고 새 레코드만 삽입
        merge_query = """
        MERGE INTO navernews n
        USING (SELECT :1 AS title, :2 AS link FROM dual) src
        ON (n.link = src.link)
        WHEN NOT MATCHED THEN
            INSERT (title, link) VALUES (src.title, src.link)
        """

        # 데이터를 리스트로 변환
        data_to_insert = list(df[['Title', 'Link']].itertuples(index=False, name=None))

        # 대량 삽입
        cursor.executemany(merge_query, data_to_insert)
        connection.commit()
        logging.info(f"{cursor.rowcount}개의 레코드가 성공적으로 삽입되었습니다.")

        # 삽입된 데이터 확인 (디버깅용)
        cursor.execute("SELECT COUNT(*) FROM navernews")
        count = cursor.fetchone()[0]
        logging.info(f"현재 navernews 테이블의 레코드 수: {count}")

    except cx_Oracle.IntegrityError as e:
        error, = e.args
        if error.code == 1:
            logging.error("중복된 링크가 존재하여 삽입에 실패했습니다.")
        else:
            logging.error(f"오류 발생: {e}")
            traceback.print_exc()
    except Exception as e:
        logging.error(f"오류 발생: {e}")
        traceback.print_exc()
    finally:
        # 리소스 정리: cursor와 connection이 None이 아닌 경우에만 닫기
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            logging.info("오라클 데이터베이스 연결이 종료되었습니다.")


def scrape_and_save(show_plot=False):
    """
    네이버 뉴스 IT/과학 섹션을 크롤링하고 데이터를 저장하는 함수
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager

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
        wait = WebDriverWait(driver, 15)  # 최대 15초 대기

        # 최신 뉴스 제목 요소가 로드될 때까지 대기
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.sa_text_title._NLOG_IMPRESSION')))

        # 뉴스 제목 요소 가져오기
        news_elements = driver.find_elements(By.CSS_SELECTOR, 'a.sa_text_title._NLOG_IMPRESSION')

        # 디버깅: 요소가 제대로 선택되었는지 확인
        logging.info(f"찾은 뉴스 요소 수: {len(news_elements)}")

        if len(news_elements) == 0:
            # 스크린샷 저장 (디버깅 용도)
            driver.save_screenshot('screenshot.png')
            # 페이지 소스 저장 (디버깅 용도)
            with open('page_source.html', 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
            logging.warning("뉴스 요소를 찾지 못했습니다. 스크린샷과 페이지 소스를 확인하세요.")
        else:
            data = []
            for news in news_elements:
                try:
                    title = news.text.strip()
                    link = news.get_attribute('href').strip()
                    logging.info(f"제목: {title}\n링크: {link}\n")  # 링크 확인을 위한 출력
                    if title and link:
                        data.append({
                            'Title': title,
                            'Link': link
                        })
                except Exception as e:
                    logging.error(f"개별 뉴스 항목 처리 중 오류: {e}")
                    traceback.print_exc()
                    continue

            # 데이터프레임으로 변환 및 클렌징
            df = pd.DataFrame(data)
            df = clean_data(df)

            # 데이터 분석 및 시각화
            analyze_and_visualize(df, show_plot=show_plot)

            # CSV 파일로 저장
            try:
                csv_path = os.path.join(os.path.dirname(__file__), 'naver_news_title.csv')
                df.to_csv(csv_path, index=False, encoding='utf-8-sig')
                logging.info(f"CSV 파일로 저장 완료: {csv_path}")
            except PermissionError as e:
                logging.error(f"CSV 파일 저장 중 권한 오류 발생: {e}")
            except Exception as e:
                logging.error(f"CSV 파일 저장 중 오류 발생: {e}")

            # 데이터베이스에 삽입
            insert_into_oracle(df)

    except Exception as e:
        logging.error(f"오류 발생: {e}")
        traceback.print_exc()
    finally:
        # 브라우저 닫기
        driver.quit()
        logging.info("웹 드라이버가 종료되었습니다.")


def job():
    """
    정기적으로 실행할 작업 정의
    """
    logging.info("크롤링 작업 시작.")
    scrape_and_save(show_plot=True)  # 테스트 시
    logging.info("크롤링 작업 완료.")


if __name__ == "__main__":
    # 스케줄 설정: 매일 오전 8시에 실행
    # 테스트 용도로 주석 처리하고 즉시 실행
    # schedule.every().day.at("08:00").do(job)
    # logging.info("크롤링 스케줄이 설정되었습니다. 프로그램을 실행합니다.")

    # 테스트를 위해 즉시 실행
    scrape_and_save(show_plot=True)

    # 스케줄링을 원할 경우 아래 코드 사용
    # schedule.every().day.at("08:00").do(job)
    # logging.info("크롤링 스케줄이 설정되었습니다. 프로그램을 실행합니다.")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
