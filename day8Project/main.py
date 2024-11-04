# 모듈 임포트
import module.sample_module as sm
# 모듈 전체를 임포트하지 않고 특정 함수나 클래스만 임포트할 수도 있다
from module.sample_module import Calculator

# 모듈의 변수 사용
print(sm.greeting)  # 안녕하세요! 저는 모듈입니다.

# 모듈의 함수 사용
result_add = sm.add(3, 5)
print(f' 3 + 5 = {result_add}')  # 3 + 5 = 8

result_subtract = sm.substract(7, 2)
print(f' 7 - 2 = {result_subtract}')  # 7 - 2 = 5

# 모듈의 클래스 사용
calc = sm.Calculator()
result_multiply = calc.multiply(2, 3)
print(f' 2 * 3 = {result_multiply}')  # 2 * 3 = 6

result_divide = calc.divide(10, 2)
print(f' 10 / 2 = {result_divide}')  # 10 / 2 = 5

result_divide_zero = calc.divide(10, 0)
print(f' 10 / 0 = {result_divide_zero}')  # 0으로 나눌 수 없습니다.

