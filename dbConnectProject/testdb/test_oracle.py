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
def setup_oracle_client(location = 'D:\\instantclient_18_5'):
    """
    Oracle Instance Client를 설정하고 초기화한다.
    Args:
      location: Oracle Instant Client 경로
    """

    # 환경변수 Path에 Instance Client 경로 추가
    os.environ['PATH'] = location + ';'+ os.environ['PATH']

    # Oracle 클라이언트 초기화 (한 번만 실행)
    try:
        cx_Oracle.init_oracle_client(lib_dir=location)
        print("Oracle 클라이언트 초기화 성공")
    except cx_Oracle.Error as e:
        print("Oracle 클라이언트 초기화 실패: ", e)



def connect_to_db(user, password, host='localhost', port=1521, service_name='xe'):
    """
    Oracle 데이터베이스에 연결하고 연결 객체를 반환한다.
    Args:
    :param user: 데이터베이스 사용자명
    :param password: 데이터베이스 비밀번호
    :param host: 오라클 호스트 주소
    :param port: 오라클 기본 포트
    :param service_name: 서비스 이름
    :return:
        cx_Oracle.Connection: 데이터베이스 연결 객체 또는 None.
    """
    try:
        # DSN(데이터 소스 이름) 생성
        dsn = cx_Oracle.makedsn(host, port, service_name = service_name)

        # 데이터베이스에 연결
        conn=cx_Oracle.connect(user=user, password =password, dsn=dsn, encoding="UTF-8")
        print("DB 연결 성공")
        return conn
    except cx_Oracle.Error as e:
        print("DB 연결 실패:", e)
        return None


# 데이터 조회 함수
def fetch_employees(conn):
    """
    employee 테이블의 모든 데이터를 조회하여 출력한다.
    Args:
    :param conn(cx_Oracle.Connection: 데이터베이스 연결 객체
    :return:
    """

    global cursor
    try:
        # 커서 객체 생성
        cursor = conn.cursor()

        # SQL 쿼리 실행(EMPLOYEE 테이블 조회)
        cursor.execute("SELECT * FROM EMPLOYEE")

        # 모든 결과 가져오기
        results = cursor.fetchall()
        for row in results:
            print(row) # 각 행 출력
    except cx_Oracle.Error as e:
        print("쿼리 실행 오류: ", e)
    finally:
        # 커서 종료
        cursor.close()
        print("쿼리 수행 완료 ")



# 데이터 추가 함수
def add_employees(conn):
    """
    employee 테이블에 새로운 직원을 추가한다

    Args:
    :param conn(cx_Oracle.Connection): 데이터베이스 연결 객체.
    :return:
    """
    try:
        cursor = conn.cursor()

        # 사용자로부터 입력받기
        emp_id = input("사번: ")
        emp_name = input("이름: ")
        emp_no = input("주민번호(14자리): ")
        email = input("email: ")
        phone = input("전화번호('-' 제외): ")
        hire_date = input("입사일 (YYYY-MM-DD): ")
        job_id = input("직급코드(2자리): ")
        salary = input("급여: ")
        bonus_pct = input("보너스 지급율: ")
        marriage = input("결혼 여부 (Y/N): ")
        mgr_id = input("관리자 사번(3자리, 없으면 엔터): ")
        dept_id = input("부서 코드(2자리, 없으면 엔터): ")

        # SQL 쿼리 작성
        sql="""
        INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME, EMP_NO, EMAIL, PHONE, HIRE_DATE, JOB_ID, SALARY, BONUS_PCT, MARRIAGE, MGR_ID, DEPT_ID)
        VALUES (:1, :2, :3, :4, :5, TO_DATE(:6, 'YYYY-MM-DD'), :7, :8, :9, :10, :11, :12)
        """

        # 데이터 바인딩
        data = (
            emp_id,
            emp_name,
            emp_no,
            email if email else None,
            phone if phone else None,
            hire_date,
            job_id if job_id else None,
            float(salary) if salary else None,
            float(bonus_pct) if salary else None,
            marriage if marriage else None,
            mgr_id if mgr_id else None,
            dept_id if dept_id else None
        )

        # 쿼리 실행
        cursor.execute(sql, data)

        # 변경사항 커밋
        conn.commit()
        print("(●'◡'●)직원 추가 성공(●'◡'●)")
    except cx_Oracle.Error as e:
        print("（；´д｀）ゞ직원 추가 오류（；´д｀）ゞ : ",e)
    finally:
        cursor.close()



#  데이터 수정 함수
def update_employee(conn):
    """
    employee 테이블에서 기존 직원을 수정한다.
    Args:
    :param conn(cx_Oracle.Connection): 데이터베이스 연결 객체.
    :return:
    """

    try:
        cursor = conn.cursor()

        # 수정할 직원 사번 입력
        emp_id = input("수정할 사번(3자리): ")

        # 존재 여부 확인
        cursor.execute("SELECT * FROM EMPLOYEE WHERE EMP_ID = :1", (emp_id,))
        result = cursor.fetchone()
        if not result:
            print("해당 사번의 직원이 존재하지 않습니다.")
            return

        # 수정할 필드 선택
        print("수정할 필드를 선택하세요:")
        print("1. 이름")
        print("2. 이메일")
        print("3. 전화번호")
        print("4. 급여")
        print("5. 보너스 지급율")
        print("6. 결혼 여부")
        print("7. 관리자 사번")
        print("8. 부서 코드")
        field = input("번호 선택: ")

        fields = {
            '1': 'EMP_NAME',
            '2': 'EMAIL',
            '3': 'PHONE',
            '4': 'SALARY',
            '5': 'BONUS_PCT',
            '6': 'MARRIAGE',
            '7': 'MGR_ID',
            '8': 'DEPT_ID'
        }

        if field not in fields:
            print("잘못된 선택입니다.")
            return

        new_value = input(f"새로운 {fields[field]} 값: ")
        if new_value == '':
            new_value=None

        # SQL 쿼리 작성
        sql = f"UPDATE EMPLOYEE SET {fields[field]} = :1 WHERE EMP_ID = :2"

        # 쿼리 실행
        cursor.execute(sql, (new_value, emp_id))

        # 변경사항 커밋
        conn.commit()
        print("(●'◡'●)직원 수정 성공(●'◡'●)")
    except cx_Oracle.Error as e:
        print("（；´д｀）ゞ직원 수정 오류（；´д｀）ゞ: ", e)
    finally:
        cursor.close()




# 데이터 삭제 함수
def delete_employee(conn):
    """
    employee 테이블에서 직원을 삭제한다.
    Args:
    :param conn: 데이터베이스 연결 객체
    :return:
    """
    try:
        cursor = conn.cursor()

        # 삭제할 직원 사번 입력
        emp_id =input("삭제할 사번(3자리): ")

        # 존재 여부 확인
        cursor.execute("select * from employee where emp_id = :1", (emp_id,))
        result = cursor.fetchone()
        if not result:
            print("해당 사번의 직원이 존재하지 않습니다.")
            return

        # sql 쿼리 작성
        sql = "delete from employee where emp_id = :1"

        # 쿼리 실행
        cursor.execute(sql, (emp_id,))

        # 변경사항 커밋
        conn.commit()
        print("(●'◡'●)직원 삭제 성공(●'◡'●)")
    except cx_Oracle.Error as e:
        print("(┬┬﹏┬┬)직원 삭제 오류(┬┬﹏┬┬): ", e)
    finally:
        cursor.close()

def main():
    """
    프로그램의 메인 함수.
    오라클 클라잉너트 설정, 데이터베이스 연결, 데이터 조회 및 연결 종료를 수행한다
    """
    # 오라클 클라이언트 설정 및 초기화
    setup_oracle_client()


    # 데이터베이스 연결 정보 설정
    db_user = 'c##scott'
    db_pass = 'tiger'
    db_host = 'localhost'    # 오라클 호스트 주소
    db_port = 1521           # 오라클 기본 포트
    db_service = 'xe'         # 서비스 이름


    # 오라클 데이터베이스에 연결
    conn = connect_to_db(user=db_user, password=db_pass, host=db_host, port=db_port, service_name=db_service)

    # 연결이 설공했을 때만 조회 수행
    if conn:
        while True:
            print("\n=== Employee 관리 시스템 ===")
            print("1. 직원 조회")
            print("2. 직원 추가")
            print("3. 직원 수정")
            print("4. 직원 삭제")
            print("5. 종료")
            choice = input("원하는 작업의 번호를 입력하세요: ")

            if choice == '1':
                fetch_employees(conn)
            elif choice == '2':
                add_employees(conn)
            elif choice == '3':
                update_employee(conn)
            elif choice == '4':
                delete_employee(conn)
            elif choice == '5':
                print(":D프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")

        # 연결 종료
        conn.close()
        print("DB 연결 종료")

if __name__ == "__main__":
    main()



