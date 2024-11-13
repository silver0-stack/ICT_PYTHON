# import는 모듈 전체
# from [모듈명] import
# 모듈에서 특정 함수, 클래스, 또는 변수를 직접 가져온다. 가져온 이름 바로 사용 가능
# from [모듈명] import *
# 모듈 내 모든 내용 가져옴 (비권장)
from dotenv import load_dotenv
import logging




class NaverNewsScraper:
    def __init__(self):
         """
        초기화 메소드: 환경 변수 로드 및 로깅 설정
        """
         self.logger = None
         load_dotenv() # .env 파일에서 환경 변수 로드
         self.setup_logging() # 로깅 설정

    def setup_logging(self):
        """
        로깅 설정: 로그를 파일 및 콘솔에 출력
        :return:
        """
        self.logger=logging.getLogger() # 로거 객체 생성
        self.logger.setLevel(logging.INFO) # 로그 레벨 설정 (INFO 이상 로그 출력)

        # 로그를 파일에 저장 (UTF-8)
        file_handler = logging.FileHandler('save_oracle.log', encoding='utf-8')
        """
        asctime() - 시간을 문자 스트링으로 변환
        levelname - 로그레벨
        message - 로그메시지
        """
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s '))

        # 로그를 콘솔에 출력
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

        # 핸들러 추가
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def scrape_news(self):
        """
        네이버 IT/과학 뉴스 크롤링
        - Selenium을 이용하여 최신 뉴스 제목과 링크를 가져온다.
        """
        chrome_options = Options()



