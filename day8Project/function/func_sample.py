# pyth: function/function_sample.py
# module: function.func_sample
# 파이썬에서 함수 만들어 사용하기 테스트 스크립트
'''

함수란, 반복 사용되는 소스 코드를 별도로 분리 작성해서 이름 붙인 것
 - 파이썬 함수 만들기
 def 함수명(매개변수): => 매개변수: 0 ~ n개
      "함수에 대한 설명 문구"   =>   help(함수명): 함수에 대한 docstring 확인 가능
      함수가 실행할 코드 구문들

- 함수의 사용: 함수 호출(function call)이라고 함
      함수가 만들어진 형태(signature)에 맞춰서 사용해야 함
      => 함수이름 틀리지 않아야 함 (대소문자 주의._ 갯수 확인)
      => 매개변수의 갯수는 일치되게 전달인자(argument) 사용해야 함
      => return 여부도 확인해야 함
      =>반환값 있는 함수는 함수(반환값 있는 함수 중첩사용())
         [반환값 받을 변수 =] 함수명()
'''


# 아무런 기능이 없는 (처리할 코드가 준비 중인) 빈 함수를 만들 때는 pass 사용함
def func():
    pass


# 함수 이름 아래에 함수 설명(docstring)을 적어둘 수 있음
def hello():
    '이 함수는 함수 작성 연습용입니다.'
    print('Hello, world!')
    print('함수명에 공백, 예약어 사용 못 함, 대소문자 구분함, _만 허용(snake_case), 숫자로 시작 못 함')
    return  # 반환값 없는 리턴은 생략해도 됨 (쓰지 않을 뿐, 자동 컴파일 할 때 실제로는 항상 존재함)


# 정석적인 함수 작성
# def add(a, b):
#     return a + b


# lamda expression
add = lambda a, b: a + b

# 변수 생성과 사용 영역 (지역, 스코프: scope)
# global, local
y = 15


def test_scope():
    x = 10
    # y = 5  # SyntaxError: name 'y' is assigned to before global declaration
    print(x)
    # print(y) # 5
    global y
    y = 20


test_scope()
# print(x) # NameError: name 'x' is not defined
print(y)


# 가변 매개변수 사용 시 주의사항
# *args: 가변 개수의 non-keyword arguments,
#  **kwargs: 가변 개수의 keyword arguments
# * args는 위치 인자를,
#  **kwargs는 키워드 인자를 받을 때
def sum_all(*args, **kwargs):
    total = 0
    for num in args:
        total += num
    for key, value in kwargs.items():
        total += value
    return total

    # lamda function
    # 익명 함수로 한 줄에 간단하게 정의할 수 있다. 주로 간단한 함수가 필요할 때 사용한다

    # 함수의 인자로 전달할 때


'''
map에 대해 배워야 함
list와 map은 짝궁?

*** func_sample2.py에 to be continued ...

'''
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

# 정렬 기준으로 람다함수를 사용할 때
data = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
sorted_data = sorted(data, key=lambda x: x[1])  # [(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# 함수 실행
if __name__ == '__main__':
    # hello()
    # help(hello())
    # print(add(10, 20))
    # print(sum_all(1, 2, 3, 4, 5, a=1, b=2, c=3)) # 21
    # print(sum_all("aa", a="kiwi", b="gg", c="ee")) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    # print(squares)
    print(sorted_data)  # 20\print(sorted_data)
