# cx_Oracle 을 사용하여 오라클 데이터베이스에 연결
# 설치 실패 시 에러 메시지 확인해보면: Microsoft C++ Builder Tool 관련 메시지다 -> 다운로드하기
# 주의: 설치 시 왼쪽 위 항목 'c++를 사용한 데스크톱 개발' 반드시 체크함 > 다운로드 클릭
# Oracle Instant Client: cx_Oracle가 오라클에 연결하려면 Oracle Instant Client 라이브러리가 필요하다

# 패키지 설치 후에 추가 설치: 파이썬에서 오라클 서버에 접속하기 위한 클라이언트 도구 필요함
# 오라클 서버 버전에서 windows 64bit용 zip 다운받음
# 해당 경로 dept 얕게 하기 위해 D드라이브에 복사함
# D:\instantclient_18_5


# cx_Oracle을 사용하여 오라클 데이터베이스에 연결
import cx_Oracle
import os
# Oracle Instance Client 경로 설정
location = 'D:\\instantclient_18_5'


# 데이터베이스 연결 정보 설정
dbUser = 'c##scott'
dbPass='tiger'
dbHost='localhost' # 오라클 호스트 주소
dbPort=1521 # 오라클 기본 포트
dbService = 'xe' # 서비스 이름 (보통 xe 또는 서비스 식별자 사용)


def oracle_init():
    cx_Oracle.init_oracle_client(lib_dir=location)
    # Mac 에서는 필요없음
    # 1. 오라클 DB에 연결
    # dsn 구성: dsn(데이터 소스 이름) 생성
    dsn = cx_Oracle.makedsn(dbHost, dbPort, service_name=dbService)

# 오라클 데이터베이스에 연결
    try:
        conn = cx_Oracle.connect(user=dbUser, password=dbPass, dsn=dsn, encoding="UTF-8")
        print("DB 연결 성공")
    except cx_Oracle.Error as e:
        print("DB 연결 실패: ", e)
        conn = None


        # 연결이 설공했을 때만 조회 수행
        if conn:
             try:
                # 커서 객체 생성
                cursor = conn.cursor()

                # SQL 쿼리 실횅 (EMPLOYEE 테이블 조회)
                cursor.execute("SELECT * FROM EMPLOYEE")

                 # 모든 결과 가져오기
                results = cursor.fetchall()
                for row in results:
                     print(row) # 각 행 출력
                    # conn.commit() // 조회할 때는 커밋 필요 없음
            except cx_Oracle.Error as e:
                    print("쿼리 실행 오류: ", e)
            finally:
                # 커서 및 연결 종료
                cursor.close()
                conn.close()
                print("DB 연결 종료")



