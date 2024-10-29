'''
키보드로 정수 2개를 입력받아서, 두 정수가 모두 양수일때만
합, 차, 곱, 몫(int), 나머지 를 계산해서 출력하시오.
입력 내용 :
 첫번째 정수 : 12 (num1 : int)
 두번째 정수 : 5 (num2 : int)
처리 내용 :
 조건 : 두 수 모두 양수이냐? (양수의 조건 : 값 > 0)
 양수가 맞을때만 사칙연산 계산해서 출력함
 둘 다 또는 하나만 0, 음수이면 처리할 내용이 없음
'''


def practice1():
    num1 = int(input('첫번째 정수 : '))
    num2 = int(input('두번째 정수 : '))
    if num1 > 0 and num2 > 0:
        print('합: ', num1 + num2)
        print('차: ', num1 - num2)
        print('곱: ', num1 * num2)
        print('몫: ', num1 // num2)  # int division
        print('나머지: ', num1 % num2)
    else:
        print('양수만 입력하세요.')


# if else 실습문제
'''
키보드로 나눌값과 나누기할 수를 입력받아 계산해서 출력하시오.
입력 내용 :
 나눌 값 : 25 (value : int)
 나누기할 수 : 0 (div_num : int)
처리 내용 :
 조건 처리 : 나누기할 수가 0 이 아니면 계산해서 몫과 나머지 출력함
          나누기할 수가 0이면 '0으로 나눌 수 없습니다.' 출력
마지막 출력구문 : if 문과 별개의 구문
 프로그램이 종료되었습니다.
'''


def practice2():
    value = int(input('나눌 값: '))
    div_num = int(input('나누기할 수: '))
    if div_num != 0:
        quotient = value // div_num  # int division
        remainder = value % div_num  # 나머지
        print('정수 몫: ', quotient)
        print('나머지: ', remainder)
    else:
        print('0으로 나눌 수 없습니다.')


# if else 실습문제
'''
키보드로 값을 입력받아 조건에 따라 처리하고 결과 출력하시오.
입력 내용 :
  수험번호 : 220602033 (tno : str)
  데이터베이스 : 90 (database : int)
  프로그래밍언어 : 98 (program : int)
  소프트웨어공학 : 60 (software : int)
처리 내용 :
  3과목의 총점(tot : int)과 평균(avg : int)을 계산함
  조건 처리 : 3과목 모두 40점이상이고, 평균이 60점이상이면
            수험번호 : 220602033 합격입니다. 출력
        아니면,
            수험번호 : 220602033 불합격입니다. 출력
'''


def practice3():
    tno = int(input('수험 번호: '))
    database = int(input('데이터베이스: '))
    program = int(input('프로그래밍 언어: '))
    software = int(input('소프트웨어공학: '))

    tot = database + program + software
    avg = tot // 3  # int division
    if database >= 40 and program >= 40 and software >= 40 and avg >= 60:
        print(f'수험번호: {tno} 합격입니다.')
    else:
        print(f'수험번호: {tno} 불합격입니다.')
