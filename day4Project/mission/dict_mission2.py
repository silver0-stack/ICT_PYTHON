# 사전 자료형 복습문제 2
'''     키보드로 값을 입력받고 요구대로 처리한 다음 출력 확인하시오.
입력내용 :
    번호 : 12 (sno : int)
    이름 : 황지니 (sname : str)
    국어 : 85 (kor : int)
    영어 : 85 (eng : int)
    수학 : 85 (mat : int)
처리내용 :
    입력받은 값들을 사전(sungjuk_dict)에 저장하시오.      키는 위의 변수이름을 문자형으로 사용하시오.
    3과목의 총점 (tot : int) 과 3과목의 평균 (avg : float)을 사전에 추가하시오.
출력내용 :
    12번 황지니의 총점은 255 점, 평균은 85.0 점.
    국어 : 85 점, 영어 : 85 점, 수학 : 85 점입니다.
'''


'''
# dict 저장 방식을 변경해 보시오.   # 학생번호를 키로 사용하고, 나머지 학생정보를 리스트로 만들어서
# 번호 : [이름, 국어, 영어, 수학, 총점, 평균]  # sungjuk_dict 에 저장한 다음 출력하시오.
def dictfunc2():

'''


# 사전 자료형 복습문제 2 - dict 저장 방식을 변경

def dictfunc2():
    # 학생 정보 입력받기
    sno = int(input("번호 : "))
    sname = input("이름: ")
    kor = int(input("국어: "))
    eng = int(input("영어: "))
    mat = int(input("수학: "))

    # 총점과 평균 계산
    tot = kor + eng + mat
    avg = tot / 3

    # 사전 생성: 번호를 키로, 나머지 정보를 리스트로 저장
    sungjuk_dict = {
        sno: [sname, kor, eng, mat, tot, avg]
    }

    # 결과 출력
    print(f"{sno}번 {sname}의 총점은 {tot} 점, 평균은 {avg:.1f} 점.")
    print(f"국어 : {kor} 점, 영어 : {eng} 점, 수학 : {mat} 점입니다.")


# 함수 호출
dictfunc2()