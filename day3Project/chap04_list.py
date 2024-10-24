# chap03_list.py
# list 자료형 : mutable(변경 가능)
# 파이썬이 제공하는 군집 자료형
# 자바의 List 와 같은 자료형임

# 개념: 여러 종류의 데이터들을 순차적으로 저장하는 자료형임
# 저장 용량에 제한이 없음
# AI데이터, 빅데이터 처리에 군집 자료형이 쓰이는 거임
# 저장되는 데이터의 종류에도 제한이 없음
# 저장 순서에 대한 순번 (인덱스, index)가 있음

# 리스트 생성 방법
#  1. list() 함수 사용
list_1 = list()
print(list_1, type(list_1))  # [] <class 'list'>



#  2. [] 대괄호 사용
list_2 = []
print(list_2, type(list_2))  # [] <class 'list'>


# list 자료형 특징 1: 문자열(str)과 같이 인덱싱, 슬라이싱 연산이 가능
# index (순번, 저장 순서, 0부터 시작함)
# 인덱싱 표현: 리스트변수[순번]
list_3 = ['apple', 'banana', 'cherry', [1, -1, 5, 6], 3.45, 0, True]
print(list_3[0])  # apple
print(list_3[1:4])# ['banana', 'cherry', [1, -1, 5, 6]]
print(list_3[-1]) # True
print(list_3[3][2]) # 5














