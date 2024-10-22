# chapter02.py

# 식별자: 개발자가 지어주는 이름
# 변수(variable): 프로그램 구동 시 메모리(RAM)에 값 기록하는 공간(방)
# 함수(function): 반복 사용되는 코드를 분리 작성해서 이름 붙여준 것 (코드의 조각 코드 묶음)
# 모듈(module): 하나 이상의 함수, 변수, 클래스를 모아서 하나의 파일(Python 파일)로 만든 것
# 클래스(class): 파이썬은 객체지향형 스크립트 언어임

# 파이썬의 이름 작성 규칙 (식별자 조건: Naming Rule)
#  1. 대소문자 구분함: name 과 Name 은 다른 이름임
NAME = '홍길동'
Name = '황진이'
name = '하하하'
print(NAME, Name, name)  # 홍길동, 황진이, 하하하

# 2. 변수의 첫 글자에 숫자 사용 못 함

#  3. 이름의 첫 글자는 문자 또는 _(underscore)만 가능
_score = 100.0
print(_score)

# 4. _를 제외한 기호문자, 공백 사용 못 함
# $menu, all*, one num: 에러
# num& = 12 # SyntaxError: invalid syntax
# print(num&)

# 5. 이름의 중간 위치나 끝에 숫자 사용할 수 있음: num1, first1_num
num1 = 10
first1_num = 20
print(num1 > first1_num)  # True

# 6. 예약어 (프로그램 언어가 사용하기 위해서 별도로 정해놓은 단어들)는 이름으로 사용할 수 없음
# True = 1 # Error: invalid syntax
true = 1
print(true)

# 파이썬이 제공하는 35개 예약어
import keyword

print(keyword.kwlist)  # 35개 예약어

# 파이썬이 제공하는 내장 함수 (Built-in Function)
# print(), len(), type(), input(), range(), list(), dict(), set(), tuple(), bool(), str(), int(), float(), complex(), abs(), sum(), round(),...

# type(값 또는 변수): 길이(저장된 값의 갯수) 리턴

# len(값 또는 변수): 값의 갯수
a = 'abcd'
b = [1, 2, 3, 4]
print(len(a))  # 4
print(len(b))  # 4

# max(값 또는 변수): 가장 큰 값 리턴, min(값 또는 변수): 가장 작은 값
print(max('abcd'))  # d
print(min('abcd'))  # a
print(max([1, 2, 3, 4]))  # 4
print(min([1, 2, 3, 4]))  # 1

# range(값 또는 변수): 파이썬이 제공하는 함수
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(2, 5)))  # [2, 3, 4]
print(list(range(2, 5, 2)))  # [2, 4]   # step 2

print(abs(-3))  # 3

# 파이썬에서는 변수가 반드시 값을 가져야 생성됨
# num # name 'num' is not defined
num = 12
print(num)  # 12

# 파이썬에서는 변수에 기록할 값을 종류(data type: 자료형)을 정하지 않음
# 변수명에 기록되는 값에 따라 자료형이 정해짐(동적 할당)

value = 100
print(value, type(value))  # 100 <class 'int'>

value = 'hello'
print(value, type(value))  # hello <class 'str'>

value = True
print(value, type(value))  # True <class 'bool'>

value = 3.12
print(value, type(value))  # 3.12 <class 'float'>

# 변수 제거: del 변수명
del value
# print(value)  # name 'value' is not defined   # Error: name 'value' is not defined


# 주석 (comment)
# 한 줄 주석: #으로 시작
# 여러 줄 주석: '''...'''

# 파이썬이 제공하는 내장 클래스 (Built-in Class)
# str, list, dict, set, tuple, bool, int, float, complex, range, open(), file(), ...

# 파이썬이 제공하는 내장 모듈 (Built-in Module)
# math, random, os, sys, ...
