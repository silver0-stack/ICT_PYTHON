# chap03_str.py
# 파이썬에서 문자열 다루기

# 파이썬에서 문자열(str)은 시퀀스(sequence, 순차자료형)로 취급됨
# 순차자료형은 값의 순번(인덱스, index)가 매겨짐. 0부터 시작됨

# 문자 선택 연산자(인덱싱): 문자변수[인덱스순번]

ss='Hi,   Python!'
print(ss[0]) # H
print(ss[1]) # i
print(ss[2]) # ,
print(ss[3]) # 공백
print(ss[4]) # 공백
print(ss[5]) # 공백
print(ss[6]) # P
print(ss[7]) # y
print(ss[8]) # t
print(ss[9]) # h
print(ss[10]) # o
print(ss[11]) # n
print(ss[12]) # !
print(ss[-1]) # 뒤에서 첫번째

# 문자열 범위 선택 연산자 (슬라이싱): 문자열 값 부분 추출 시 사용
# 문자변수[시작인덱스:끝인덱스] : 시작인덱스 <= 인덱스 < 끝인덱스 범위가 됨

print(ss[0:5]) # Hi, Py
print(ss[6:12]) # Python
print(ss[6:]) # Python!
print(ss[:5]) # Hi, Py
print(ss[:]) # Hi, Python!


# 문자 처리 내장함수
# upper(), lowert(), title(), isupper(), islower(), isalpha(), isdigit(), isspace(), isalnum(), isidentifier()

print(ss.upper()) # HI, PYTHON!
print(ss.lower()) # hi, python!
print(ss.title()) # Hi, Python!
print(ss.isupper()) # False
print(ss.islower()) # False

# 파이썬에서도 자바와 동일하게 메모리에 기록된 문자값은 변경할 수 없음 (immutable)
# ss[1] = 'p' # TypeError: 'str' object does not support item assignment
# SOL) 제공되는 고나련 함수를 사용하면 됨
print(ss.upper()) # 변경된 문자열은 메모리에 새로 기록됨

ss2 = 'BANANA'
print(ss2.lower()) # banana

# swapcase(), capitalize(), count(), find(), index(), replace(), split(), join()
ss3 = 'tEsT cAsE'
print(ss3.swapcase()) #TeSt CaSe # 소문자 -> 대문자, 대문자 -> 소문자
print(ss3.capitalize()) # 첫 글자만 대문자

# title(): 함수: 문자열의 첫글자만 대문자, 나머지는 소문자로 변환
print(ss.title()) # Hi, Python!

print('////////////////////////////')
# strip(), lstrip(), rstrip(): 함수: whitespace(공��, tab, newline) 제거
ss4 = '      Hello,      World!     '
print('|', ss4, '|', sep= '')
print('|', ss4.strip(), '|', sep= '')
print('|', ss4.lstrip(), '|', sep= '')
print('|', ss4.rstrip(), '|', sep= '')
print('|', ss4.replace(' ', ''), '|', sep='') # 앞뒤 중간 모든 공백을 제거하려면 replace()메소드를 사용한다

# split(), splitlines()
tt5 = 'abc-def-ghi-j'
print(tt5.split('-')) # ['abc', 'def', 'ghi', 'j']

# splitlines(): 함수: newline(\n)을 기준으로 문자열을 split()
tt6 = '''
python
java
javascript
'''

print(tt6)
print(tt6.splitlines())

# index(), find(): 글자 위치 (인덱스: 순번) 조회
print(tt6.index('y')) # 2
print(tt6.find('y')) # 2
print(tt6.find('z')) # -1: -1은 문자열이 존재하지 않을 경우 -1 반환
# print(tt6.index('z')) # -1: -1은 문자열이 존재하지 않을 경우 -1 반환 # ValueError: substring not found
print(tt6.rindex('y')) # 2 # rindex()는 right-to-left로 찾음


print('\n')
# 이 외의 문자 관련 다른 함수들 조회하려면
print(len(dir(str)))# str.__doc__, str.__new__(), str.__init__(), str.__str__(), str.__bytes__(), str.__format__(), str.__len__
print(dir(str))

# 문자열에 포맷(format)을 적용해서 코드 작성하는 방법
# 문자열 값 사이에 다른 종류의 값이나 변수를 적용하려고 할 때 이용함
print('\n')
amount=int(input('개수 입력: '))
re='사과를 %d개 주문함' % amount
print(re)

# 정수 10진수 (decimal) -> 2진수 (binary)
# 문자열(string): %s
# 실수형 숫자(float): %f
# 정수형 숫자(int): %d

print('\n')
product_name=input('주문할 상품명: ')
price=int(input('제품의 단가: '))
str2= '상품명은 %s, 단가는 %d원' % (product_name, price)
print(str2)
