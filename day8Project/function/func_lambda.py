# path: function\\func_lambda
# module: function.func_lambda


'''
 람다함수는 이름이 없는 단일 표현식 함수이다.
 lambda 키워드드를 사용하여 정의하며, 주로 한 번만 사용되거나 간단한 표현식을 수행할 때 유용함

 람다 함수의 특징
 - 익명 함수: 이름이 없기에 일회성
 - 단일 표현식: 단 하나의 표현식만을 포함할 수 있으며, 여러 줄의 코드 포함할 수 X
 - 간결성: 짧고 간단한 함수 정의에 적합
 - 일급 객체: 다른 함수의인자로 전달되거나, 함수에서 반환될 수 있음

 기본 문법
 lambda 인자1, 인자2, ...: 표현식
'''


def add(a, b):
    return a + b


result = add(10, 20)
print(result)  # 30

add = lambda a, b: a + b
print(add(10, 20))  # 30

'''
람다 함수의 사용 사례
 1. 단순한 함수가 필요한 경우
 2. 고차 함수(map, filter, sorted)와 함께 사용할 때
 3. 일회성으로 사용할 함수가 필요할 때
 
 map(실행할 함수, iterable 객체): iterable 객체의 모든 요소에 lambda 함수를 적용
'''

# 예제1) map() 함수와 람다함수
# map() 함수는 주어진 함수를 반복 가능한 객체(iterable)의 모든 요소에 적응하여 새로운 반복 간으한 객체를 반환한다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# 일반 함수
def square(x):
    return x ** 2


squared = map(square, numbers)
print(list(squared))  # [1, 4, 9, 16, 25, 36, 49, 64]

#  람다함수 사용
squared_lambda = map(lambda x: x ** 2, numbers)
print(list(squared_lambda))  # [1, 4, 9, 16, 25, 36, 49, 64]

# 예제2) filter() 함수와 람다함수
# filter() 함수는 주어진 함수의 반환값이 True인 요소만을 걸러내어 새로운 반복 가능한 객체를 반환한다
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# 짝수만 필터링 (일반 함수 사용)
def is_even(x):
    return x % 2 == 0


evens = filter(is_even, numbers)
print(list(evens))  # [2, 4, 6, 8]

# 짝수만 필터링 (람다함수 사용)
evens_lambda = filter(lambda x: x % 2 == 0, numbers)
print(list(evens_lambda))  # [2, 4, 6, 8]

# sorted() 함수와 람다 함수
# sorted() 함수는 주어진 반복 가능한 객체를 정렬하여 새로운 리스트로 반환한다.
# key 매개변수를 사용하여 정렬 기준을 지정할 수 있다


data = [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (4, 'date'), (5, 'elderberry')]


# 두 번째 요소를 기준으로 정렬(일반 함수 사용)
def sort_key(item):
    return item[1]


sorted_data = sorted(data, key=sort_key)
print(sorted_data)  # [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (4, 'date'), (5, 'elderberry')]

# 두 번쨰 요소를 기준으로 정렬 (람다 함수 사용)
sorted_data_lambda = sorted(data, key=lambda item: item[1])
print(sorted_data_lambda)  # [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (4, 'date'), (5, 'elderberry')]

# 조건부 표현식 사용
# 짝수면 '짝수', 홀수면 '홀수'를 반환하는 함수
even_or_odd = lambda x: '짝수' if x % 2 == 0 else '홀수'
print(even_or_odd(10))  # 짝수
print(even_or_odd(9))  # 홀수

# 리스트 컴프리헨션 대신 map()과 람다 함수 사용하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

'''
리스트 컴프리헨션(list comprehension)은 쉽게 말해 리스트를 쉽게, 짧게 한 줄로 만들 수 있는 파이썬의 문법이다

'''

# 리스트 컴프리헨션
squared = [x ** 2 for x in numbers]
print(squared)

# map() + 람다 함수
squared_map = list(map(lambda x: x**2, numbers))
print(squared_map)


# 딕셔너리의 값 변환에 map()과 람다 함수 사용하기
students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88
}

# 모든 점수를 5 점 추가
updated_scores = dict(map(lambda item: (item[0], item[1] + 5), students.items()))
print(updated_scores)  # {'Alice': 90, 'Bob': 97, 'Charlie': 83, 'David': 93})



# 중첩된 람다 함수 사용하기
# 두 개의 람다 함수를 중첩하여 사용
multiply = lambda x: lambda y: x * y

double = multiply(2)
triple = multiply(3)

print(double(5))  # 10
print(triple(5))  # 15







'''
람다함수의 장점
 1. 간결성
 2. 일회성 사용
 3. 고차 함수와의 통합: map(), filter(), sorted()
 
 람다함수의 단점
  1. 복잡한 로직 구현 제한
  2. 가독성 저하
  3. 디버깅 어려움: 익명 함수이므로 디버깅 시 함수 이름을 통해 식별하기 어렵다
'''
