# test_bool\\operator_sample.py or test_bool/operator_sample.py
# module: test_bool.operator_sample
def func_bool():
    flag = True
    print('flag: ', flag, type(flag))  # flag:  True <class 'bool'>

    flag = False
    print('flag: ', flag, type(flag))  # flag:  False <class 'bool'>

    # 파이썬에서는 대소문자 구분함
    # True, False : boolean literal
    # flag = true # NameError: name 'true' is not defined

    # bool() 함수 사용: 값의 논리상태를 확인할 때 사용함
    print('result1: ', bool('abcd'))  # result1:  True
    print('result2: ', bool(''))  # result2:  False

    print('result3: ', bool(123))  # result3: True: 0을 제외한 모든 숫자는 True
    print('result4: ', bool(0))  # result4:  False

    # 값이 저장되어 있는지, 비어 있는지 확인하는 용도로 bool() 함수를 사용함
    # list, dict, set, str, bytes, tuple, range, file, None
    # None: False
    # bool() 함수: None => False
    # bool() 함수: 0, '', (), [], {} => False
    # bool() 함수: True, any other value => True
    print('result5: ', bool([]))  # result5:  False
    print('result6: ', bool({}))  # result6:  False
    print('result7: ', bool(''))  # result7:  False
    print('result8: ', bool(()))  # result8:  False
    print('result9: ', bool(None))  # result9:  False
    print('result10: ', bool(0))  # result10:  False
    print('result11: ', bool(123))  # result11:  True
    print('result12: ', bool('abcd'))  # result12: True

    # 비교(관계) 연산자
    # 2개 값을 가지고 크냐(>, 초과), 작으냐(<, 미만), 크거나 같음(>= , 이상), 작거나 같음(<=, 이하)
    # 같으냐(==), 같지않느냐(!=)
    # 이항 연산자: 값 1 연산자 값2
def func_compare():
    print('1 == 1 : ', 1 == 1) # True
    print('1 != 1 : ', 1 != 1) # False

def func_logical():
    print('True and True : ', True and True)  # True
    print('True and False : ', True and False)  # False
    print('False and True : ', False and True)  # False
    print('False and False : ', False and False)  # False

    print('True or True : ', True or True)  # True
    print('True or False : ', True or False)  # True
    print('False or True : ', False or True)  # True
    print('False or False : ', False or False)  # False

    print('not True : ', not True)  # False
    print('not False : ', not False)  # True

    # and, or, not: 2개의 boolean 값만을 받아서 boolean 값을 return
    # and: True, True => True, True, False => False
    # or: True, True => True, False, False => False
    # not