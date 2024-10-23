"""

# chap02_input.py

# 파이썬에서 실행 시 키보드로 값 입력받기: input() 함수 사용함
# 변수 = input("입력을 위한 메시지 문장: ")

num = input("숫자를 입력하세요: ")
print('num: ', num, type(num))

# 파이썬의 input() 함수로 입력 들어오는 값은 모두 문자형(str)이다.
# print('더하기: ', num + 10)  # Error: unsupported operand type(s) for +: 'int' and'str'

# 숫자형으로 바꾸고자 한다면
# 정수는 int('정수문자'), 실수는 float('실수문자')로 변환
inum = int(num)
print('num: ', inum, type(inum)) # num:  10 <class 'int'>
print('더하기: ', inum + 10) # 더하기: 20


# 입력 예:
# 정수 2개를 각각 입력 받아서 , 사칙연산 결과 출력
first = int(input('첫번째 수: '))
second = int(input('두번째 수: '))
print('합: ', first + second)

# f-string: 3.7 이상에서만 지원
print(f'합: {first + second}')
print(f'{first} 더하기 {second} 는 {first + second} 입니다.')


# f-string: 3.6 이하에서는 format() 함수를 사용
# format() 함수와 순번을 적용할 수도 있음
print('{} * {} = {}'.format(first, second, first * second))  # format() 함수를 사용 # 순번를 적용할 수도 있음
print('{1} / {0} = {2:.2f}'.format(second, first, first / second))

print('합: {}'.format(first + second))    # format() 함수를 사용
"""

# 입력엽습 1
print(' **** 입력연습 ****')

'''
신상 정보를 입력받아, 각 변수에 저장하세요. 변수이름은 임의대로.
이름(str), 나이 (int), 성별(str, 남|여), 키(float), 몸무게(float)
각 변수의 값을 아래의 형식으로 출력하는 코드를 작성하시오
홍길동으 27세 남자이고, 키는 178.5cm, 몸무게는 72.0kg 입니다.
'''
name = input('이름: ')
age = int(input('나이: '))
gender = input('성별: ')
height = float(input('키: '))
weight = float(input('몸무게: '))

print(f'{name}은 {age}세 {gender}이고, 키는 {height}cm, 몸무게는 {weight}kg 입니다.')

# 입력연습2
print(' **** 입력연습2 ****')

'''
키보드로 값을 입력받아 요구 조건대로 처리하고 출력되게 코드를 작성하시오
기본값을 가진 변수 생성 할당해 둠:
    total_point = 12500
입력내용:
    고객 이름: 황지니 (custom_name: str)
    결제 금액: 3000000 (price: int)
처리내용:
    결제금액의 5%를 포인트(point: float)로 처리
    계산된 포인트를 누적포인트(total_point: int)에 증가 연산 처리함
출력내용:
    황지니 고객님의 사용금액은 300000원, 발생 포인트는 15000
    현재 이용하실 수 있는 누적포인트는 162500점입니다.

'''

total_point = 12500
custom_name = input('고객 이름: ')
price = int(input('결제 금액: '))
point = price * 0.05
total_point += point
print(f'황지니 고객님의 사용금액은 {price}원, 발생 포인트는 {int(point)}\n'
      f'현재 이용하실 수 있는 누적포인트는 {int(total_point)}점입니다.')
