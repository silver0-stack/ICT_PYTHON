# path: loop/forSample.py or loop\\forSample.py
# module: loop.forSample
# 파이썬에서의 for 문 사용 테스트 스크립트

'''
for 문 작성형식 1:
for 변수 in 리스트 | 튜플 | 딕셔너리 | 집합 | 문자열: (콜론주의)
    반복 실행할 구문들 작성 (들여쓰기 중요)
주의사항: in 오른쪽에는 값 하나(리터럴) 사용 못 함 (TypeError)
`
for 문 작성형식 2:
'''


def test_for1():
    print('\n --list--')
    # list 사용
    for i in [1, 2, 3, 4, 5]:
        print(i)

    # for k in 10:
    #     print(k)  # TypeError: 'int' object is not iterable

    print('\n --tuple--')
    # tuple 사용
    for t in (10, 15, 20, 25):
        print(f'{t} is even' if t % 2 == 0 else f'{t} is odd')

    print('\n --set--')
    # set 사용
    for s in {10, 20, 30, 40, 50}:
        print(f'{s} is even' if s % 2 == 0 else f'{s} is odd')
        '''
        40 is even
        10 is even
        50 is even
        20 is even
        30 is even
        '''

    print('\n --str--')
    # str 사용
    for str in 'Hello, world!':
        print(f'{str} 문자의 유니코드는 {ord(str)} 이다.')

    print('\n --dict--')
    # dict 사용
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key, value in my_dict.items():
        print(f'{key}: value')

    '''
    for문 작성형식2: range() 함수 사용
    range(start, stop, step) : start <= i < stop (step = ?)
    start 생략 시, 0
    stop (미만, 포함 안됨), 생략 불가
    step 생략 시, 1
    
    for 변수 in range(start, stop:)
    for i in range(1, 10):
        print(i)
    '''

    # 1부터 100까지 정수들의 합계를 구해서 출력


def for_sum():
    sum_ = 0
    for i in range(1, 101):
        sum_ += i
    print(f'1부터 100까지의 정수의 합계: {sum_}')  # 5050


print('\n -----------------------------------')

# import collections.iterable # deprecated: 버전업하면서 사용 중지됨
import collections.abc as abc


def test_for2():
    # iterable object: 리스트처럼 순차적으로 값을 나열해서 저장한 객체를 말함
    # isinstance() 함수를 이용해서 iterable object 종류를 확인할 수 있음 (자바의 instanceOf() 연산자와 같음)

    '''
    주어진 코드에서 리스트 [1, 2, 3, 4]는 Iterable 객체입니다. 하지만 for 루프는 리스트의 각 요소를 순회합니다.
    이 경우 각 요소는 정수(int)이므로, isinstance(i, abc.Iterable)은 False를 반환하게 됩니다.
    '''

    for i in [1, 2, 3, 4]:
        print(f'{i} is iterable: {isinstance(i, abc.Iterable)}')  # False

    my_list = [1, 2, 3, 4]
    print(f'my_list is iterable: {isinstance(my_list, abc.Iterable)}')  # True


def test_range():
    print(range(10))  # range(0, 10)

    lst = list(range(10))
    print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f' lst is iterable: {isinstance(lst, abc.Iterable)}')  # lst is iterable: True


# for 문 작성형식 3: range(len(군집자료형변수)) - 연속된 값을 인덱스로 처리
def for_indexin():
    my_list = ['apple', 90, [1, 2, 3], ('A', 'B', 'C')]
    for i in range(len(my_list)):  # range(0, 4) : 0, 1, 2, 3
        print(f'{i + 1}. {my_list[i]}')
        # 1. apple
        # 2. 90
        # 3. [1, 2, 3]
        # 4. ('A', 'B', 'C')


# 키보드로 구구단의 단 수를 입력받아서 해당 단의 구구단 출력
def print_gugudan():
    dan = int(input('구구단의 단수를 입력하세요: '))
    for i in range(1, 10): # 1 ~ 9
        print(f'{dan} x {i}  = {dan * i}')
