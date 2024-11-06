# cx_Oracle 을 사용하여 오라클 데이터베이스에 연결
# 설치 실패 시 에러 메시지 확인해보면: Microsoft C++ Builder Tool 관련 메시지다 -> 다운로드하기
# 주의: 설치 시 왼쪽 위 항목 'c++를 사용한 데스크톱 개발' 반드시 체크함 > 다운로드 클릭
# Oracle Instant Client: cx_Oracle가 오라클에 연결하려면 Oracle Instant Client 라이브러리가 필요하다

# 패키지 설치 후에 추가 설치: 파이썬에서 오라클 서버에 접속하기 위한 클라이언트 도구 필요함
# 오라클 서버 버전에서 windows 64bit용 zip 다운받음
# 해당 경로 dept 얕게 하기 위해 D드라이브에 복사함
# D:\instantclient_18_5\bin\nt64\instantclient_18_5.dll -> cx_Oracle.dll

location = 'D:\\instantclient_18_5'

import cx_Oracle

# 데이터베이스 연결 설정
dbUser = 'c##scott'
dbPass='tiger'
dbHost='localhost' # 오라클 호스트 주소
dbPort=1521 # 오라클 기본 포트
dbService = 'xe' # 서비스 이름 (보통 xe 또는 서비스 식별자 사용)

# 1. 오라클 DB에 연결
# dsn 구성: dsn(데이터 소스 이름)을 사용하여 연결 정보 지정
dsn = cx_Oracle.makedsn(dbHost, dbPort, service_name=dbService)
conn = cx_Oracle.connect(user=dbUser, password=dbPass,dsn=dsn,encoding="UTF-8" )

# 연결 여부 확인
if conn is None:
    print("DB 연결 실패")
else:
    print("DB 연결 성공")

# 2. cursor 객체 생성
cursor=conn.cursor()

# 3. SQL 쿼리 실행 (예: employee 테이블 조회)
cursor.execute("select * from employee")

# 4. 조회된 모든 결과 받기
results = cursor.fetchall()
for row in results:
    print(row) # 각 행의 데이터를 출력하거나 원하는 방식으로 처리


# 변경사항 커밋 (조회 작업에서는 필요 없음)
# conn.commit()


# 5. 연결 종료
cursor.close()
conn.close()
print("DB 연결 종료")
