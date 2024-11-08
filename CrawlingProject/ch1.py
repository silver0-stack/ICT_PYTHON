import requests # 웹 페이지에 HTTP 요청을 보내기 위해 사용된다
from bs4 import BeautifulSoup # HTML을 파싱하고 원하는 데이터를 추출하기 위해 사용된다

def crawl_titles(url):
    try:
        # 웹 페이지 요청
        response = requests.get(url) # 지정된 URL에 GET 요청을 보냄
        response.raise_for_status() #  요청이 성공했는지 확인하고, 실패 시 예외를 발생시킴

        # BeautifulSoup 객체를 생성해서 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser') # 응답 받은 HTML 텍스트를 파싱함

        # 원하는 요소 찾기 (예: 모든 h2 태그)
        titles = soup.find_all('h2') # 모든 <h2> 태그를 찾는다. (원하는 태그로 변경 가능), 각 제목의 텍스트 추출 및 출력

        print("f:URL: {url} 에서 추출한 제목들: ")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text(strip=True)}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 오류 발생: {http_err}")
    except Exception as err:
        print(f"기타 오류 발생: {err}")

if __name__  == "__main__":
    target_url= 'https://www.python.org/downloads/release/python-3910/'  # 예시 URL, 크롤링할 웹 페이지의 url을 지정한다
    crawl_titles(target_url) # 함수를 호출하여 크롤링을 수행한다
