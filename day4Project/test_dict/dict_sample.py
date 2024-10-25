# test_dict\\dict_sample.py
# 모듈로 표현:
# 모듈(module): 함수들을 따로 모아서 저장해 놓은 소스 파일
# 모듈 사용: 다른 파일에서 필요 시 import해서 사용함
# dict 에서 key는 변겨오디지 않는 값이어야 함 (키는 불변) -> 키에 튜플 사용 가넝
# dict에 저장하는 value는 모든 자료형 데이터 가능함
# json, xml 로 변환할 때 많이 사용됨



def test1():
    print('\ntest1 START!!')
    # 방법 1: dict()함수
    dict_1 = dict()
    print('1. dict() 함수:', dict_1, type(dict_1))  # {} <class 'dict'>

    # 방법 2: {} 중괄호
    dict_2 = {}
    print('2. {} 중괄호:', dict_2, type(dict_2))  # {} <class 'dict'>



# list나 tuple처럼 인덱스를 사용할 수 없음: 인덱스 없음
# key를 이용해서 값 조회, 변경, 추가할 수 있음: 사전변수[키]
# dict에 값 저장 방식: (키:값) 쌍으로 지정함
def test2():
    print('\ntest2 START!!')
    dict_3 = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    print('3. dict_3:', dict_3)  # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

    # 3-1. key로 value 조회
    print('3-1. dict_3["apple"]:', dict_3['apple'])  # red

    # 3-2. key로 value 변경
    dict_3['apple'] = 'green'
    print('3-2. dict_3["apple"]:', dict_3['apple'])  # green

    # 3-3. key로 value 추가
    dict_3['orange'] = 'orange'
    print('3-3. dict_3:', dict_3)  # {'apple': 'green', 'banana': 'yellow', 'cherry': 'red', 'orange

    # 3-4. key로 value 삭제
    del dict_3['banana']
    print('3-4. dict_3:', dict_3)  # {'apple': 'green', 'cherry': 'red', 'orange'}

    # 3-5. key 존재 여부
    print('3-5. "apple" in dict_3:', 'apple' in dict_3)  # True
    print('3-5. "melon" in dict_3:', 'melon' in dict_3)  # False

    # 3-6. dict_3.keys(): key만 list로
    print('3-6. dict_3.keys():', dict_3.keys())  # dict_keys(['apple', 'cherry', 'orange'])

    # 3-7. dict_3.values(): value만 list로
    print('3-7. dict_3.values():', dict_3.values())  # dict_values(['green', 'red', 'orange'])

    # 3-8. dict_3.items(): key-value ��� list로
    print('3-8. dict_3.items():', dict_3.items())  # dict_items([('apple', 'green'), ('cherry', 'red'), ('orange', 'orange')])

    # 3-9. dict_3.clear(): value 전체 삭제(저장 아이템 전체 삭제)
    dict_3.clear()
    print('3-9. dict_3:', dict_3)  # {}

    # 3-10. key-value ���을 dict_3 에서 pop()
    dict_3['apple'] = 'red'
    dict_3['banana'] = 'yellow'
    dict_3['cherry'] = 'red'
    dict_3['orange'] = 'orange'
    print('3-10. dict_3:', dict_3)  # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'orange': 'orange'}
    print('3-10. dict_3.pop("apple"):', dict_3.pop("apple"))  # red

    # 3-11. key-value ���을 dict_3 에서 popitem()
    print('3-11. dict_3.popitem():', dict_3.popitem())  # ('orange', 'orange')
    print('3-11. dict_3:', dict_3)  # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

    # 3-12. key-value ���을 dict_3 에서 update()
    dict_3.update({'apple': 'green', 'melon': 'yellow'})
    print('3-12. dict_3:', dict_3)  # {'apple': 'green', 'banana': 'yellow', 'cherry': 'red', 'melon': 'yellow'}




#  dict 내장함수 활용
def test3():
    print('\ntest3 START!!')
    # dict() 또는 {} 중괄호
    dict_4 = dict(apple='red', banana='yellow', cherry='red')
    print('4. {} 중괄호:', dict_4)

    # 키에 대한 리스트 만들기: keys()
    print('4-1. dict_4.keys():', dict_4.keys())  # dict_keys(['apple', 'banana', 'cherry'])

    # value에 대한 리스트 만들기: values()
    print('4-2. dict_4.values():', dict_4.values())  # dict_values(['red', 'yellow', 'red'])

    # key-value 쌍으로 tuple list 만들기: items()
    print('4-3. dict_4.items():', dict_4.items())  # dict_items([('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red')])

    # dict_4 에서 key-value 쌍 pop(): 해당 키에 대한 값을 삭제
    dict_4.pop('apple')
    print('4-4. dict_4:', dict_4)  # {'banana': 'yellow', 'cherry': 'red'}

    # dict_4.pop() # TypeError: pop expected at least 1 argument, got 0
    # print('4-6. dict_4:', dict_4)  # {'banana': 'yellow', 'cherry': 'red'}

    dict_4['kukumelon'] = 'purple'
    print('4-5. dict_4:', dict_4)  # {'banana': 'yellow', 'cherry': 'red', 'kukumelon': 'purple'}






# 사전과 사전을 합치기: update() 함수 사용
# 사전1.update(사전2) -> 사전1이 변경되는 거
# 사전1과 사전2에 중복된 키가 있을 시에는, 사전1의 키 값이 변경됨
def test4():
    print('\ntest4 START!!')
    dict_5 = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    dict_6 = {'apple': 'green', 'melon': 'yellow'}
    dict_5.update(dict_6)
    print('5. dict_5.update(dict_6):', dict_5) # {'apple': 'green', 'banana': 'yellow', 'cherry': 'red','melon': 'yellow'}

    # copy() 함수: 사전 객체를 새로 만들고 아이템들을 복사함(shallow copy)
    print('dict_5 id: ', id(dict_5))
    dict_7 = dict_5.copy() # 2102195017088
    print('6. dict_7.copy():', dict_7) # {'apple': 'green', 'banana': 'yellow', 'cherry': 'red','melon': 'yellow'}
    print('dict_7 id: ', id(dict_7)) # 2102195019136 (다름, 왜? copy()함수는 다른 주소에서 og를 긁어온거니까)

    dict_8 = dict_5
    print('dict_8 id: ', id(dict_8)) # 2102195017088 (같음, 왜? 주소를 가리키는 거니까)



# dict 안에 키 또는 값이 존재하는지 확인: in 사용
def test5():
    print('\ntest5 START!!')
    dict_9 = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    print('7. "apple" in dict_9:', 'apple' in dict_9)  # True
    print('7-1. "melon" in dict_9:', 'melon' in dict_9)  # False

    # in operator: dict_9.keys() or dict_9.values()
    print('7-2. "red" in dict_9.values():', 'red' in dict_9.values())  # True
    print('7-3. "yellow" in dict_9.keys():', 'yellow' in dict_9.keys())  # False

