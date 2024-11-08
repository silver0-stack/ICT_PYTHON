import json
import cx_Oracle
from datetime import datetime
import logging
import os
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# 로깅 설정
logging.basicConfig(filename='weather_insert.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def get_kma_weather():
    """
    한국 기상청(KMA)의 중기예보 RSS 피드에서 날씨 데이터를 가져와서 구조화된 형태로 반환하는 함수.

    Returns:
        weather_data (list): 각 지역별로 구조화된 날씨 정보가 담긴 딕셔너리의 리스트.
    """
    url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'  # 중기예보 RSS 피드 URL
    weather_data = []  # 날씨 데이터를 저장할 빈 리스트

    try:
        # 웹 페이지에 GET 요청을 보내고 응답을 받음
        response = requests.get(url)
        response.raise_for_status()  # 요청이 성공했는지 확인 (상태 코드 200)
    except RequestException as e:
        # 요청 중 오류가 발생하면 오류 메시지를 출력하고 빈 리스트 반환
        print(f"요청 오류 발생: {e}")
        logging.error(f"요청 오류 발생: {e}")
        return weather_data

    try:
        # 응답 내용을 XML 형식으로 파싱
        soup = BeautifulSoup(response.content, 'xml')

        # 모든 <item> 태그를 찾음 (각 <item>은 하나의 지역 그룹을 나타냄)
        items = soup.find_all('item')

        # 각 <item> 태그에 대해 반복 처리
        for item in items:
            title = item.title.text.strip()  # 지역 그룹 이름 (예: 서울ㆍ인천ㆍ경기도)
            description = item.description.text.strip()  # 지역 그룹에 대한 상세 날씨 정보

            # <description> 내용을 다시 HTML로 파싱하여 데이터 추출
            desc_soup = BeautifulSoup(description, 'html.parser')

            # <description> 내의 텍스트를 줄 단위로 분리
            desc_text = desc_soup.get_text(separator='\n')
            lines = desc_text.split('\n')  # 줄 단위로 리스트로 변환

            current_region_group = ''  # 현재 지역 그룹을 저장할 변수
            current_region = ''  # 현재 지역을 저장할 변수

            i = 0  # 줄을 순회할 인덱스 초기화
            while i < len(lines):
                line = lines[i].strip()  # 현재 줄의 텍스트를 가져와 공백 제거
                if not line:
                    i += 1  # 빈 줄이면 다음 줄로 이동
                    continue

                # 지역 그룹을 나타내는 줄인지 확인 (예: 서울ㆍ인천ㆍ경기도)
                if 'ㆍ' in line:
                    regions = line.split('ㆍ')  # 'ㆍ'를 기준으로 지역 그룹을 분리
                    current_region_group = regions[-1].strip()  # 마지막 지역 그룹을 현재 그룹으로 설정
                    i += 1  # 다음 줄로 이동
                    continue

                # 개별 지역 이름을 가져옴 (예: 서울)
                if i < len(lines):
                    current_region = line
                    i += 1  # 다음 줄로 이동
                else:
                    break  # 더 이상 줄이 없으면 종료

                # 다음 6줄이 예보 데이터임을 확인
                if i + 5 < len(lines):
                    forecast_type = lines[i].strip()  # 예보 타입 (예: A02)
                    date_time = lines[i + 1].strip()  # 예보 날짜 및 시간 (예: 2024-11-11 00:00)
                    sky = lines[i + 2].strip()  # 하늘 상태 (예: 구름많음)
                    temp_min = lines[i + 3].strip()  # 최저 기온 (예: 10)
                    temp_max = lines[i + 4].strip()  # 최고 기온 (예: 19)
                    precipitation = lines[i + 5].strip()  # 강수 확률 (예: 20)

                    # 데이터 추가
                    weather_data.append({
                        '지역 그룹': current_region_group,
                        '지역': current_region,
                        '예보 타입': forecast_type,
                        '날짜 및 시간': date_time,
                        '하늘 상태': sky,
                        '최저 기온': temp_min,
                        '최고 기온': temp_max,
                        '강수 확률': precipitation
                    })

                    i += 6  # 다음 예보 데이터로 이동
                else:
                    break  # 예보 데이터가 부족하면 종료

    except Exception as parse_err:
        # 파싱 중 오류가 발생하면 오류 메시지를 출력
        print(f"오류 발생: {parse_err}")
        logging.error(f"오류 발생: {parse_err}")

    return weather_data  # 구조화된 날씨 데이터 반환

def clean_weather_data(weather_data):
    """
    날씨 데이터에서 유효한 항목만 추출하는 함수.

    Args:
        weather_data (list): 원본 날씨 데이터.

    Returns:
        list: 정제된 날씨 데이터.
    """
    cleaned_data = []
    for entry in weather_data:
        # '지역' 필드가 실제 지역인지 확인
        if not entry['지역 그룹'] and entry['지역'] == "전국 육상중기예보":
            # 메타데이터 항목은 건너뜁니다.
            continue
        # 필수 필드가 존재하는지 확인
        if entry['지역'] and entry['날짜 및 시간']:
            # 예보 타입이 'A01' 또는 'A02'인 경우에만 처리
            if entry['예보 타입'] in ['A01', 'A02']:
                # 날짜 및 시간 형식 변환
                try:
                    date_time = datetime.strptime(entry['날짜 및 시간'], '%Y-%m-%d %H:%M')
                except ValueError:
                    # 날짜 형식이 올바르지 않으면 문자열로 유지
                    date_time = entry['날짜 및 시간']

                # 강수 확률을 숫자로 변환
                try:
                    precipitation = int(entry['강수 확률'])
                except (ValueError, TypeError):
                    precipitation = None

                # 최저 기온, 최고 기온을 숫자로 변환
                try:
                    temp_min = float(entry['최저 기온'])
                except (ValueError, TypeError):
                    temp_min = None
                try:
                    temp_max = float(entry['최고 기온'])
                except (ValueError, TypeError):
                    temp_max = None

                # 정제된 데이터를 리스트에 추가
                cleaned_data.append({
                    'region_group': entry['지역 그룹'],
                    'region': entry['지역'],
                    'forecast_type': entry['예보 타입'],
                    'date_time': date_time,
                    'sky_condition': entry['하늘 상태'],
                    'temp_min': temp_min,
                    'temp_max': temp_max,
                    'precipitation': precipitation
                })
    return cleaned_data

def insert_into_oracle(cleaned_data, dsn, user, password):
    """
    오라클 데이터베이스에 정제된 데이터를 삽입하는 함수.

    Args:
        cleaned_data (list): 정제된 날씨 데이터.
        dsn (str): 오라클 데이터베이스 DSN 문자열.
        user (str): 데이터베이스 사용자 이름.
        password (str): 데이터베이스 사용자 비밀번호.
    """
    connection = None
    cursor = None
    try:
        # 오라클 데이터베이스에 연결
        connection = cx_Oracle.connect(user, password, dsn)
        cursor = connection.cursor()

        # 삽입할 SQL 문
        insert_sql = """
            INSERT INTO kma_weather (
                region_group, region, forecast_type, date_time, sky_condition, temp_min, temp_max, precipitation
            ) VALUES (
                :region_group, :region, :forecast_type, :date_time, :sky_condition, :temp_min, :temp_max, :precipitation
            )
        """

        # 삽입할 데이터 리스트 생성
        data_to_insert = []
        for data in cleaned_data:
            data_to_insert.append(data)

        if len(data_to_insert) > 0:
            # 대량 삽입
            cursor.executemany(insert_sql, data_to_insert)
            # 변경사항 커밋
            connection.commit()
            print("데이터가 성공적으로 삽입되었습니다.")
        else:
            print("삽입할 데이터가 없습니다.")

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"데이터베이스 오류: {error.message}")
        logging.error(f"데이터베이스 오류: {error.message}")
    except Exception as e:
        print(f"예기치 않은 오류: {e}")
        logging.error(f"예기치 않은 오류: {e}")
    finally:
        # 커서와 연결 종료 (존재할 경우에만)
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def main():
    # 데이터 가져오기
    weather_data = get_kma_weather()

    # 데이터 정제
    cleaned_data = clean_weather_data(weather_data)

    # 정제된 데이터 확인
    print(f"정제된 데이터 개수: {len(cleaned_data)}")
    if len(cleaned_data) > 0:
        print("첫 번째 데이터 항목:", cleaned_data[0])

    # 예보 타입이 'A01' 또는 'A02'인 항목만 필터링 (이미 `clean_weather_data`에서 필터링됨)
    cleaned_data_filtered = cleaned_data  # 이미 필터링된 데이터
    print(f"예보 타입 필터링 후 데이터 개수: {len(cleaned_data_filtered)}")
    if len(cleaned_data_filtered) > 0:
        print("첫 번째 필터링된 데이터 항목:", cleaned_data_filtered[0])

    # 오라클 데이터베이스 연결 정보 설정
    dsn = 'localhost:1521/xe'  # 실제 환경에 맞게 수정
    user = 'c##scott'           # 데이터베이스 사용자 이름
    password = 'tiger'          # 데이터베이스 사용자 비밀번호

    # 데이터베이스에 데이터 삽입 (필터링된 데이터 사용)
    insert_into_oracle(cleaned_data_filtered, dsn, user, password)

if __name__ == "__main__":
    main()
