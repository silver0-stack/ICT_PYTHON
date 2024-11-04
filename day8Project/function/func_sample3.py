# 재귀 함수란?
# 자기 자신을 호출하는 함수 (Recursive Function)
# 복잡한 문제를 더 작은 단위로 나누어 해결할 때 매우 효과적

'''
 1. 기본 사례 (base case): 재귀 호출을 멈추기 위한 조건이다.
 기본 사례가 없으면 무한호출되어 스택 오버플로우(Stack Overflow)가 발생할 수 있다.

 2. 재귀 단계(Recursive Step): 문제를 더 작은 단위로 분할하여 자기 자신을 호출하는 부분
 '''


# 예제 1) 팩토리얼 계산
#  n! = n * (n-1) * (n-2) * ... * 1
def factorial(n):
    if n ==0:
        return 1 # 기본 사례
    else:
        return n * factorial(n-1) # 재귀 단계


# 테스트
print(factorial(5)) # 120
print(factorial(0)) # 1