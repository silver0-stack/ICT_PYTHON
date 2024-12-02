import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



# CSV 데이터 로드
file_path = './data/housing.csv'  # housing.csv 파일 경로
housing_data = pd.read_csv(file_path)

# 입력 특성과 타겟 변수 분리
X = housing_data.drop('MEDV', axis=1)  # 입력 특성
y = housing_data['MEDV']  # 타겟 변수

# 데이터를 학습(70%), 테스트(30%) 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 특성 값 표준화 (평균 0, 표준편차 1로 변환)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# DNN 모델 설계
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),  # 입력층 및 첫 번째 은닉층
    Dense(64, activation='relu'),  # 두 번째 은닉층
    Dense(1)  # 출력층: 예측 집값 (회귀 문제이므로 노드 1개)
])

# 모델 컴파일
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 모델 학습
history = model.fit(X_train_scaled, y_train, validation_split=0.2, epochs=100, batch_size=32, verbose=1)

# 모델 요약 출력
model.summary()


# 테스트 데이터 평가
test_loss, test_mae = model.evaluate(X_test_scaled, y_test, verbose=2)
print(f"테스트 손실(MSE): {test_loss}, 테스트 MAE: {test_mae}")

# 예측값 확인
predictions = model.predict(X_test_scaled).flatten()

# 실제값과 예측값 비교 시각화
import matplotlib.pyplot as plt
from matplotlib import rc

# 한글 폰트 설정
rc('font', family='Malgun Gothic')  # Windows
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.7, label="예측값")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label="실제값")
plt.xlabel("실제 집값")
plt.ylabel("예측 집값")
plt.legend()
plt.title("집값 예측 결과")
plt.show()
