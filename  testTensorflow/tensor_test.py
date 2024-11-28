import tensorflow as tf
# MNIST(손글씨 숫자(0~9) 이미지 데이터셋) 데이터를 사용한 DNN 학습 예

# 손글씨 숫자 이미지 분류하기
# MNIST 손글씨 데이터 가져오기
# import tensorflow.keras # MNIST 관련 에러 발생 시에 추가함
mnist = tf.keras.datasets.mnist

# MNIST 4분할 데이터로 나누기 처리
(X_train, Y_train), (X_test, Y_test) = mnist.load_data() # (X_train, Y_train), (X_test, Y_test)
print('학습용 입력 데이터 모양: ', X_train.shape) # (60000, 28, 28)
print('학습용 출력 데이터 모양: ', Y_train.shape) # (60000,)
print('테스트용 입력 데이터 모양: ', X_test.shape) # (10000, 28, 28)
print('테스트용 출력 데이터 모양: ', Y_test.shape) # (10000,)

import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap='Greys')
plt.show()