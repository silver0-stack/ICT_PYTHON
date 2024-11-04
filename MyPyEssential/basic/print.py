a, b, c = 10, 20, 30
print(a, b, c, sep="|")  # 10|20|30
print(a, b, c, sep="|", end=" ::끝")  # 10|20|30 ::끝

print('\n')

# swapping
# 자바의 스와핑 공식 필요 없음
# swapping: a, b = b, a
a, b = 10, 20
print(a, b)  # 10 20
a, b = b, a
print(a, b)  # 20 10

# 몫과 나머지를 한꺼번에 구하려면 divmod() 함수 사용
# divmod = division and modulo
print(divmod(5, 3))  # (1, 2)

a = 5
a **= 3  # 5의 세제곱
print(a)  # 125

import math

# sqrt = square root (제곱근)
print(math.sqrt(25))  # 제곱근 -> 5
print(math.factorial(5))  # 5! = 120
print(math.pi)  # π (pi) -> 3.141592653589793
print(math.sin(math.radians(45)))  # sin(45°) -> 0.7071067811865476

# str slicing
'''
   0123456789
   ^   ^   ^   ^
   |   |   |   |
   |   |   |   - 1
   |   |   - 2
   |   - 3
   - 4
   
   
   - 콜론(:)의 역할
   슬라이싱에서 콜론(:)은 범위를 지정한다. 
   a[start:end] = a[start] ~ a[end-1]
   a[start:] = a[start] ~ a[n-1]
   a[:end]= a[0] ~ a[end-1]
   a[start:end:step] = a[start] ~ a[end-1] width step
   a[::step] = a[0] ~ a[n-1] with step 
'''
#  음수 인덱스: 문자열 끝에서부터 인덱스를 센다
# -1은 마지막 문자, -2는 두번째 마지막 문자를 의미함
a = '안녕하세요'
print(a[0])  # 안
print(a[1:3])  # 녕하
print(a[:3])  # 안녕하
print(a[-1])  # 요
print(a[-2:])  # 세요

print(a[::-1])  # 요세하녕안 (뒤에서부터 앞으로)

strip_str = '   Hello, World!   '
print(strip_str.strip()) # Hello, World!

tt = 'abcv-dfdf-ererfsdfd-bdfg'
print(tt.split('-')) # ['abcv', 'dfdf', 'ererfsdfd', 'bdfg']


tt2 = '''
python
java
javascript
'''
print(tt2)
# print(tt2.splitlines()) # ['python', 'java', 'javascript']

 # index() : 찾고자 하는 문자열의 index 위치를 반환한다
 # find(): index()와 동일하나 찾고자 하는 문자열이 없을 경우 -1을 반환한다
print(tt2.find('d')) # -1
# print(tt2.index('d')) # ValueError: substring not found

# 그럼 언제 index를 쓰고 언제 find를 써야할까?
# index() 메소드는 찾고자 하는 문자열이 반드시 존재한다고 확신할 때 사용해야 함
# 예를 들어, 이메일에서 @의 index 위치 반환

# find() 찾고자 하는 문자열이 존재하지 않을 가능성이 있는 상황에서 사용한다
# 예를 들어, 키워드로 텍스트 필터링할 때
# valueError 예외 처리하지 않고도 문자열의 존재 여부를 확인할 수 있다


# in 연산자
# 문자열의 포함 여부를 단순히 확인할 때는 in 연산자를 사용하는 것이 더 직관적
# in 연산자는 문자열이 포함되어 있는지 여부를 True/False 로 반환
# 단순히 포함 여부만 확인할 때 유용하다


print(len(dir(str))) # 81
print(dir(str))  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__']

# rindex(): find()와 index()의 차이점: rindex()는 찾고자 하는 문자열의 reverse index 위치를 반환한다













