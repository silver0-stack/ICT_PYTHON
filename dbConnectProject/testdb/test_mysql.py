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
