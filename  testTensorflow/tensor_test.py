# 환경 변수 설정: KMP_DUPLICATE_LIB_OK 설정을 통해 OpenMP 라이브러리 충돌 방지
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Tensorflow와 Matplotlib 임포트
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib import rc

# 한글 폰트 설정: Matplotlib에서 한글 텍스트를 지원하도록 폰트 설정
rc('font', family='Malgun Gothic')  # Windows 환경에서 '맑은 고딕' 폰트 사용
plt.rcParams['axes.unicode_minus'] = False # 그래프에서 마이너스(-) 기호 깨짐 방지

# MNIST 데이터셋 로드: 손글씨 숫자 데이터 (0~9)
# (X_train, Y_train): 학습용 데이터와 레이블
# (X_test, Y_test): 테스트용 데이터와 레이블
mnist = tf.keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 데이터 정규화: 픽셀 값을 0~1 범위로 변환 (255로 나누기)
X_train = X_train / 255.0
X_test = X_test / 255.0

# 학습 데이터 구조 확인
print('학습용 입력 데이터 모양:', X_train.shape) # 예 : (60000, 28, 28)
print('학습용 출력 데이터 모양:', Y_train.shape) # 예: (60000,)

# 첫 번째 데이터 시각화
plt.imshow(X_train[0], cmap='Greys')
plt.title(f"레이블: {Y_train[0]}")
plt.show()

# 신경망 모델 설계
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 인공신경망 요약
model.summary()

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 설계된 모델을 가지고 인공신경망 학습(Training): 학습횟수 (epoch)
model.fit(X_train, Y_train, epochs=5, batch_size=32) # 5번 학습시킴

# 모델 평가
test_loss, test_accuracy = model.evaluate(X_test, Y_test, verbose=2)
print(f"테스트 데이터 손실: {test_loss}")
print(f"테스트 데이터 정확도: {test_accuracy}")

# 예측
predictions = model.predict(X_test)
print("첫 번째 테스트 데이터 예측:", predictions[0])
print("가장 높은 확률로 예측된 클래스:", tf.argmax(predictions[0]).numpy())

# 첫 번째 테스트 데이터 시각화
plt.imshow(X_test[0], cmap='Greys')
plt.title(f"예측된 값: {tf.argmax(predictions[0]).numpy()}")
plt.show()
