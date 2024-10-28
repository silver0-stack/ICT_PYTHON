# test_set/set_sample.py
# test_set.set_sample

# 집합(set) 자료형
#  교집합(&), 합집합(|), 차집합(-) 연산이 가능한 자료형
# 저장 방식은 자바의 Set 과 같음: 같은 값 중복 저장 안 함 , 저장 순서 X

# set 정의 방법 1: {} 중괄호 사용, 단 빈 {}는 무조건 빈 딕셔너리를 생성하므로,
# 빈 집합을 만들고자 할 때는 set() 함수를 사용해야 함
# set으로 사용하려면 중괄호 안에 초기값 지정할 것
def test1():
    print({1,2,3,4,5}, type({1,2,3,4,5})) # {1, 2, 3, 4, 5} <class 'set'>

    # set 정의 방법2: set() 함수 사용
    set2 = set()
    print(set2, type(set2)) # set() <class 'set'>

    # 초기 데이터와 함께 생성
    fruits = {'apple', 'banana', 'cherry'}
    print(fruits, type(fruits)) # {'apple', 'banana', 'cherry'} <class 'set'>

    #  값 중복 안 됨
    fruits.add('apple')
    print(fruits, type(fruits)) # {'apple', 'banana', 'cherry'} <class 'set'>

    #  여러 원소 추가
    # 리스트로 추가 불가능함
    # 왜? set은 immutable(변경할 수 없는) 자료형이기 때문에 숫자, 문자열, 튜플 등 변경 불가능한 원소만 추가 가능
    # fruits.add(["grape", "orange"]) #TypeError: unhashable type: 'list'

    fruits.add(('grape', 'orange', 'kiwi'))  #{('grape', 'orange', 'kiwi'), 'cherry', 'apple', 'banana'}]
    print(fruits)

    fruits.add('melon')
    print(fruits)

    #  값 여러 개 추가 : update([value1, value2,...])
    fruits.update(['melon', 'watermelon', 'peach'])
    print(fruits)

    # fruits.remove('melon') # KeyError: 'melon' (존재하지 않는 원소를 제거하려고 했으니 KeyError 발생)
    fruits.remove(('grape', 'orange', 'kiwi'))
    print(fruits)

    # list의 값 중복을 제거할 때 set을 주로 이용함
    list1 = [1,1,1,2,2,3,3,4,4,5,5,6,6,7]
    set2 = set(list1)
    print( set2) # {1, 2, 3, 4, 5, 6, 7}

    list1 = [set2]
    print(list1, type(list1)) # [{1, 2, 3, 4, 5, 6, 7}] <class 'list'>
