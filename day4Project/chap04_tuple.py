# chap04_tuple.py
# 튜플(tuple) 자료형: 리스트와 저장 방식은 같음
#  여러 종류의 데이터들을 순차적으로 저장하는 집합자료형임
#  리스트와 다른 점은 저장된 엘리먼트를 변경할 수 없음 -> immutable

#  튜플 정의 방법 1: 소괄호 ()로 정의
tp_1 = ()
print(tp_1, type(tp_1))  # <class 'tuple'>

# 튜플 정의 방법 2: tuple() 함수 사용
tp_2 = tuple()
print(tp_2, type(tp_2))  # <class 'tuple'>

#  튜플도 리스트와 같이 인덱싱, 슬라이싱 연산 가능
lst = [10, 20, 30, 40, 50]
tpl = (10, 20, 30, 40, 50)
print(lst, type(lst))  # <class 'list'>
print(tpl, type(tpl))  # <class 'tuple'>

print('0번째 값: {}, {}'.format(lst[0], tpl[0]))
print('0번째 부터 1번째 까지의 값들: {}. {}'.format(lst[0:2], tpl[0:2]))
print('0번째 부터 1번째 까지의 값들: {}, {}'.format(lst[:2], tpl[:2]))
print('리스트 합치기: {}'.format(lst + [60, 70, 80]))
print('튜플 합치기: {}'.format(tpl + (60, 70, 80)))

# 튜플과 리스트의 차이점: 튜플은 값 변경 못함 (immutable)
lst[0] = 100
# tpl[0] = 100  # TypeError: 'tuple' object does not support item assignment


# 주의사항:
# 튜플 생성 시에 한 개의 데이터만 저장할 때는 반드시 값 뒤에 콤마(,)가 와야 한다
tp_3 = (10)
print(tp_3, type(tp_3))  # 10 <class 'int'>

tp_4 = (10,)
print(tp_4, type(tp_4))  # (10,) <class 'tuple'>

#  튜플 생성 시 저장 데이터가 1개일 때는 소괄호 생략해도 됨
tp_5 = 10,
print(tp_5, type(tp_5))  # (10,) <class 'tuple'>




# 튜플 내장함수
# count(): 찾는 값의 갯수 조회
# 튜플변수.count(찾는값)
number_count = tpl.count(10)

print('tpl에 10의 갯수: {}'.format(number_count))  # tpl에 10의 갯수: 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                      수: {}'.format(

#  튜플변수.index(찾는값)
print('tpl에서 10의 index: {}'.format(tpl.index(10)))

#  len(튜플변수): 튜플에 저장된 엘리멘트의 갯수 리턴
print('tpl에 저장된 element 개수: {}'.format(len(tpl)))

# 참고사항: () 없이 하나의 변수에 값 나열 대입하면 자동 튜플이 됨
x = 1, 2, 3
print(x, type(x))  # (1, 2, 3) <class 'tuple'>



# 참고사항:
# 프로그래밍 언어의 언칙: return 문은 한개만 반환할 수 있음 (value or address)
# return value : 또는 return reference variable: 또는 return variable
# 파이썬에서는 여러 개의 값을 리턴할 수 있음  -> 자동 튜플이 됨
#  return 값, 값, 값..


# 샘플 함수 정의 --------------------------------
def f_test():
    return (3, 5)

# 함수 사용(호출, call)
# 함수가 리턴하는 값이 여러개인 경우에는 반드시 값 받아줄 변수도 갯수 맞춰서 준비함
x, y= f_test()
print(x,y,type(x), type(y))  # 3 5 <class 'int'> <class 'int'>
























