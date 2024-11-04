# path: function\\func_sample2.py
# module: function.func_sample2
# 파이썬의 함수 정의(definition, 만들기)와 호출(call) 연습 스크립트


# call by Value
# call By Address


def tmax(a, b):
    '두 개의 값을 전달받아서, 둘 중 큰 값을 리턴하는 함수이다'
    print(f'a: {a}, b: {b}, type: {type(a)}, {type(b)}')
    return a if a > b else b


# 파이썬에서는 군집자료형을 전달받는 매개변수는 주소를 받는다
def list_in_max(plist):
    '리스트 객체를 전달받아서, 리스트 안의 값들 중 가장 큰 값을 찾아내서 리턴하는 함수'

'''
map 함수는 주어진 함수와 반복 가능한(iterable) 자료형(list, tuple, dict, set, str) 등을 인자로 받아, 
각 요소에 함수를 적용한 결과를 반환하는 함수이다. 
주로 데이터 변환, 툭종 연산 반복적으로 적용할 때

map(함수, 반복가능한자료형)
- 함수: 각 요소에 적용할 함수
- 반복가능한자료형: list, tuple, str etc ..
'''


#  예제1) 리스트의 모든 요소를 제곱하기
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
# map() returns a map object (which is an iterator), not a list so, you need to convert it to a list using list() function
squared = map(square, numbers)


#  예제2) 람다 함수를 사용하여 리스트의 모든 요소를 제곱하기
numbers = [1, 2, 3, 4, 5]
squared_lambda = map(lambda x: x **2 , numbers) # you can do same thing as above but with lambda function, more readable
# print(squared_lambda) # <map object at 0x00000242E47B9820>
# so wee need to convert it to a list

"""
    sorted 함수란?
    주어진 반복 가능한(iterable) 자료형(list, tuple, dict, set)의 요소들을 정렬하여 새로운 리스트로 반환하는 함수이다
    원본 객체는 변경되지 않는다(sort()와의 차이점)
 
    sorted(iterable, key=None, reverse=False)
    - iterable: 정렬할 반복 가능한 객체
    - key: 정렬 기준이 되는 함수
    - reverse: 정렬 순서를 뒤집을지 여부 (기본값: False)
"""


# 예제 3) 숫자 리스트 정렬
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)

'''
    key 매개변수와 람다 함수
    key 매개변수는 각 요소를 정렬할 때 기준이 되는 값을 지정할 수 있는 매개변수이다.
    보통 람다함수를 사용하여 특정 속성을 기준으로 정렬할 때 많이 사용된다.
'''

# 예제 4) 튜플 리스트를 두 번째 요소를 기준으로 정렬하기
data = [('apple', 200), ('banana', 0), ('cherry', 10)]
# data 리스트의 각 튜플에서 두 번째 요소(x[1])을 기준(key)으로 정렬한다
# 결과적으로 두 번째 요소인 숫자를 기준으로 정렬된다
sorted_data = sorted(data, key = lambda x: x[1])  # [('banana', 0), ('cherry', 10), ('apple', 200)]
sorted_reverse_data = sorted(data, key = lambda x: x[1], reverse = True)  # [('apple', 200), ('cherry', 10), ('banana', 0)]



'''
sorted 함수와 map 함수 함께 사용하기
map 함수를 사용하여 리스트의 요소를 변환한 후, sorted 함수를 사용하여 정렬할 수 있다.
'''


# 예제 5) 문자열 리스트를 정수로 변환한 후 정렬하기
string_numbers= ['10', '2', '8', '1', '3']
int_numbers = list(map(int, string_numbers))
sorted_int_numbers = sorted(int_numbers)  # [1, 2, 3, 8, 10]
reverse_sorted_int_numbers = sorted(int_numbers, reverse=True)  # [10, 8, 3, 2, 1]




if __name__ == '__main__':
    # print(tmax(10, 20))
    # print(square(10))
    # print(square) # <function square at 0x00000242E47BB880>
    # print(list(squared)) # [1, 4, 9, 16, 25]
    # print(list(squared_lambda))  # [1, 4, 9, 16, 25]

    print(numbers)  # [5, 2, 8, 1, 3] .. 원본 리스트는 변경되지 않음 (sorted() 함수는 새로운 리스트를 반환)
    print(sorted_numbers)  # [1, 2, 3, 5, 8]
    print(sorted_data)  # [('banana', 0), ('cherry', 10), ('apple', 200)]
    print(sorted_reverse_data)  # [('banana', 0), ('cherry', 10), ('apple', 200)]
    print(sorted_int_numbers)  # [1, 2, 3, 8, 10]
    print(reverse_sorted_int_numbers)  # [10, 8, 3, 2, 1]







