#  모듈: 함수를 가지고 있는 파이썬 파일
# 다른 파이썬  파일이 가진 함수를 사용하려면, import 하면 됨
# import 모듈명 [as 줄임말]
import test_set.set_sample as ss
import test_bool.operator_sample as sam
import conditional.ifSample as ifs

if __name__ == '__main__':
    # ss.test1()
    # sam.func_bool()
    # sam.func_logical()
    # ifs.test_if()
    # ifs.test_even()
    # ifs.test_square()
    ifs.test_in()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

