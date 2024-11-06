# path: testdb\\test_mysql.py

# 파이썬 외부 모듈(패키지) 설치와 사용
# 파이썬 외부 모듈은
# 1. 프로젝트에 직접 설치해서 사용하는 방법 (venv)
# 2. Anaconda에 별도로 콘다가상환경을 만들고, 필요한 패키지를 설치한 다음에 프로젝트에 콘다가상환경을 연결 사용

# 프로젝트에 직접 설치하는 방법
# 파이참 툴 왼쪽 하단에 'Python Packages' 탭을 클릭 > 뷰가 아래 쪽에 보여짐
# 뷰의 왼쪽에 검색창에 설치할 패키지명을 입력
# 검색되면 패키지명을 왼쪽에서 클릭하면 오른쪽에 패키지 정보가 출력됨
# 오른쪽 패키지 정보 위에 'Install Packages' 버튼 클릭함
# 설치가 완료되면 버전숫자 표시됨
# 만약, 설치가 실패하면 오류 메세지에서 에러 이유를 찾아내서 해결해야 됨

# 두번째 방법:
# 모든 파이썬 개발툴에서 공통으로 사용하는 방법임
# Terminal (터미널) 탭(왼쪽 아래)
# 프롬프트 표시됨: (가상환경종류) 터미널 종류
# 프롬프트에 설치 명령어를 직접 입력해서 패키지 설치함
# pip install 설치할패키지명
# 주의사항: pip 버전을 먼저 upgrade 해야 되는 경우가 있음
# ...>python -m pip install --upgrade pip
# ...> pip --version
# 패키지 설치와 pip 업그레이드 동시에 수행할 수도 있음
#  ...> python -m pip install --upgrade [패키지명]

# 데이터베이스 연결에 필요한 파이썬 패키지
# mysql db (maria db): pymysql
# oracle db: cx-Oracle => 에러 발생 시 선행 조치 내용 확인하고 해결함
# SQLite: 파이썬 내장 라이브러리임(설치 필요없음), 파일 기반의 경량 데이터베이스임
# PostgreSQL: psycopg2 | pg8000
# mongoDB: pymongo
# MS SQL Server: pyodbc | pymssql
# Redis: redis-py
# mongoDB: pymongo
# casandra: cassandra-driver
# maraiDB: mariadb


# 1. 연결할 DB에 대한 패키지를 설치한 다음에 import 선언하고 사용함
import pymysql

# 2. 해당 데이터베이스에 연결하기 위한 코드 작성
# db 서버의 ip주소(url), port 번호, 사용자 계정과 암호
dbURL = 'localhost'
dbPort = 3306
dbUser = 'root'
dbPASS = '1234'


# 3. pymysql.connect() 함수를 사용해서 MySQL DB에 접속
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, password=dbPASS, db='testdb',\
                       charset='utf8', use_unicode=True)


# 연결 여부 확인
if conn is None:
    print("db 연결 실패")
else:
    print("db 연결 성공")


# 4. DB 연결이 성공하면 cursor 객체 생성해서 Cursor object를 반환
cursor = conn.cursor()

# 5. SQL query를 작성하여 실행(테이블 생성)
cursor.execute("""
SELECT * FROM employee
)
""")

# 조회된 모든 결과를 받음. 반환 자료형은 tuple임
cursor.fetchall()
# 이후 결과 매핑 처리: 반복문으로 각 행의 컬럼값들을 vo(dto)클래스 객체의 필드(proeprty)에 저장 처리

# 쿼리문이 dml이면 트랜잭션 처리가 필수임
# 변경사항 커밋
conn.commit()

# 연결 종료
cursor.close()
conn.close()

print("DB 연결 종료")























