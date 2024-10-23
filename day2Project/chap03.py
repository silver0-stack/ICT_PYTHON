# chapt03.py

'''
파이썬에서의 변수 공간에 값 기록하는 메모리 할당 (memory allocation)
    파이썬에서의 변수 할당은 동적 할당임
    동적(Runtime 시: 실행시) 메모리(RAM)에 값(data)을 저장하는 공간
    변수명 = 계산식
    변수명 = 리턴값이 있는 함수명 (전달값)
  주의사항:
    변수명 ( = 값이 없으면 에러임)


'''

num = 1+ 2
print('num 변수가 가진 값: ', num) # num 변수가 가진 값:  3

# 변수 할당 시 = (대입연산자) 사용함
# 대입연산자는 반드시 왼쪽에 변수, 오른쪽에 값 또는 계산식 위치함( 변수 <- 값)
# 값 = 변수 # 에러
# 100 = a

# 한번에 여러 개의 변수에 값을 할당할 수 있음
# a, b, c = 10, 20, 30
# print('a, b, c:', a, b, c)  # a, b, c: 10 20 30
a, b, c = 10, 20, 30
print(a, b, c, sep = ' | ')  # a, b, c: 10 | 20 | 30 # sep: separator (구분자), 출력값들을 구분할 기호

# 한 개의 값을 여러 변수에 할당할 수도 있음
k = m = n = 10
print(k, m, n)  # 10, 10, 10
print(k, m, n, sep = ', ')  # 10, 10, 10



# swap 공식 사용 필요 없음!
# swapping: a, b = b, a
print('***swapping***')
a, b = 10, 20
print(a, b)  # 10, 20
a, b = b, a
print(a, b)  # 20, 10





# """ """ 큰 따옴표 3개는 띄어쓰기나 줄바꿈 등이 입력한 그대로 출력됨
#  5 //3 = 1  -> 나눗셈 몫을 정수형으로 표현하고 싶으면 슬래쉬를 두번 작성하면 됨
# 몫과 나머지를 동시에 구하려면, divmod() 함수를 사용
print(divmod(5, 3))  # (1, 2)
# 5 ** 3 = 125 -> 5의 3제곱
print(5 ** 3)  # 125
print(pow(5, 3))  # 125


#  = (순수대입연산자)
# 복합대입연산자 : 산술대입연산자가 주로 사용됨
# 파이썬의 산술연산자: +, -, *, /, //, %, **
# +=, -=, *=, /=, //=, %=, **=
a = 5
a **= 3
print(a)  # 125

print('***복합대입연산자***')
value = 100
print('value: ', value) # value:  100
value += 100
print('value: ', value) # value:  200
value -= 100
print('value: ', value) # value:  100
value *= 100
print('value: ', value) # value:  10000
value /= 100
print('value: ', value) # value:  100.0
value //= 100
print('value: ', value) # value: 1.0 # 나눈 몫이 정수가 되게 하고 싶으면 // 쓰기
# value %= 100
# print('value: ', value)
value **= 100
print('value: ', value) # value: 1.0

# math 모듈
import math

print(math.sqrt(25))  # 제곱근 # 5.0
print(math.factorial(5))  # 5! # 120
print(math.pi)  # 3.141592653589793
print(math.sin(math.radians(90)))  # sin(90°) # 1.0


# 파이썬 코드 문장은 한 줄 작성이 원칙
# 문장이 길어서 한 줄 작성이 불편할 경우에는 여러 줄로 나눌 수는 있음
# 단, 문장이 끊어지는 부분에 반드시 백슬러시(\)를 표시해야 함
print('ringo the best\n' * 3)

# str slicing
a = '안녕하세요'
print(a[::1]) # 안녕하세요 # 변화없음
print(a[0])  # 안
print(a[-1])  # 요
print(a[1:3])  # 녕하
print(a[::2])  # 안하요 # step 2 # a[0:5:2] 와 같음
print(a[::-1])  # 요세하녕안 # step -1 # a[::-1] 역순으로 탐색
print(a[0:5:2])  # 안하요 # 변수[시작(이상):끝(미만):스텝]
