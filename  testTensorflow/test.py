# 텐서는 N차원의 배열이다.
# 스칼라(0차원), 백터(1차원), 행렬(2차원), 다차원 배열(3차원 이상)
# 모든 데이터는 텐서로 표현된다.

import tensorflow as tf

# 1차원 텐서
a = tf.constant([1, 2, 3])
print(a)

# 그래프와 세션(Tensorflow 1.x VS Tensorflow 2.x)
#  - Tensorflow 1.x
#  - Tensorflow 2.x
# 즉시 실행(Eager Execution) 방식 도입
# 파이썬 코드 실행처럼 간단히 작성 가능

# 간단한 덧셈 연산
a = tf.constant(2)
b = tf.constant(3)
c = a + b
print(c) # tf.Tensor(5, shape=(), dtype=int32)
