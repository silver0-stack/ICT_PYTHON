# dnn_gan.py
# GAN 신경망 활용 손글씨 흉내내기

# GAN(Generative Adversarial Network)
# 딥러닝 모델 중 이미지 생성에 널리 쓰이는 모델임
# 데이터셋과 유사한 이미지를 만들도록 하는 것임

# 파이썬 패키지 임포트
import matplotlib.pyplot as plt
import numpy as np
from time import time
import os
import glob  # 파일들의 리스트를 뽑을 때 사용함
# glob('*.확장자') : 해당 패턴의 파일 리스트를 지정 디렉토리에 읽어와서 리턴함
# 파일 관련 모듈 : pickle, glob, os.path

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Flatten, Reshape
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.models import Sequential
import os
import tensorflow as tf
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 하이퍼 파라미터
M_GEN = 128
M_DIS = 128
M_NOISE = 100

M_SHAPE = (28, 28, 1)
M_EPOCH = 5000
M_BATCH = 128

# 출력 이미지 폴더 생성
M_FOLDER = 'output/'
os.makedirs(M_FOLDER, exist_ok=True)

# 만약, output/ 폴더가 이미 존재한다면, 폴더 안의 모든 파일을 삭제함
# glob() : 파일 형식을 이용해서 파일을 선택하는 함수임. 리스트로 리턴
for f in glob.glob(M_FOLDER + '*'):
    os.remove(f)

# 함수 단위로 작성하고 실행 테스트하는 구조로 작성할 것임
### 데이터 준비 ###

def read_data():
    # 학습용 입력값만 사용 (GAN 은 비지도 학습)
    (X_train, _), (_, _) = mnist.load_data()

    print('데이터 모양 : ', X_train.shape)
    plt.imshow(X_train[0], cmap='gray')
    plt.show()

    # 데이터 스케일링 [-1, 1]
    X_train = X_train / 127.5 - 1.0

    # 채널 정보 추가
    X_train = np.expand_dims(X_train, axis=3)
    print('데이터 모양 : ', X_train.shape)

    return X_train
# -------------------------------------------------

### 인공 신경망 구현 ###

# 생성자 설계 구현 : 가짜 이미지 생성하는 학습 모델
def build_generator():
    model = Sequential()

    # 입력층 + 은닉층 1
    model.add(Dense(M_GEN, input_dim=M_NOISE))
    model.add(LeakyReLU(alpha=0.01))
    # 은닉층의  활성화 함수는 입력값이 작으면 작은 값을 출력하고,
    # 입력값이 크면 큰 값을 출력하는 함수를 사용함
    # 은닉층에서 활성화함수로 sigmoid 함수를 사용하면,
    # 경사 소실 문제가 발생하기 때문에 다른 활성화함수를 사용해서
    # 경사 소실 문제를 해결해야 함

    # LeakyReLU 함수(LReLU 라고도 함)
    # ReLU 함수를 개량한 함수로 알파값을 0.01 을 곱하는 함수

    # 은닉층 2
    model.add(Dense(M_GEN))
    model.add(LeakyReLU(alpha=0.01))

    # 은닉층 3 + 출력층
    # tanh 활성화는 [-1, 1] 스케일링 때문에 사용함
    model.add(Dense(28 * 28 * 1, activation='tanh'))
    model.add(Reshape(M_SHAPE))

    print('\n생성자 요약')
    model.summary()

    return model
# ----------------------------------------------

# 감별자 설계 구현 : 가짜 이미지 판별하는 학습 모델
def build_descriminator():
    model = Sequential()

    # 입력층
    model.add(Flatten(input_shape=M_SHAPE))

    # 은닉층 1
    model.add(Dense(M_DIS))
    model.add(LeakyReLU(alpha=0.01))

    # 출력층
    model.add(Dense(1, activation='sigmoid'))

    print('\n감별자 요약')
    model.summary()

    return model
# -------------------------------------

# DNN-GAN 학습 모델 설계 구현
def build_GAN():
    model = Sequential()

    # 생성자 구현
    genarator = build_generator()

    # 감별자 구현
    # 생성자 학습시 감별자 고정
    descriminator = build_descriminator()

    descriminator.compile(optimizer='adam', loss='binary_crossentropy',
                          metrics=['acc'])

    descriminator.trainable = False  # 감별자 학습 안되게 설정

    # GAN 모델 구현 : 생성자 먼저 추가, 그 다음에 감별자 추가
    model.add(genarator)
    model.add(descriminator)

    # GAN 모델에서는 정확도 무의미
    model.compile(optimizer='adam', loss='binary_crossentropy')

    print('\nGAN 요약')
    model.summary()

    return descriminator, genarator, model
# ----------------------------------------------------------


######################################
### 설계된 인공 신경망 학습(교육) 시키기 ###

# 감별자 학습 방법
@tf.function
def train_discriminator():
    # 진짜 이미지 임의로 하나의 batch 추출
    total = X_train.shape[0]  # 6만개
    pick = np.random.randint(0, total, M_BATCH)  # 0 ~ 6만 사이의 3백개 추출
    image = X_train[pick] # 임의로 추출된 인덱스 위치의 이미지 추출

    # 손글씨 숫자 1 이미지를 하나의 batch 로 지정
    all_1 = np.ones((M_BATCH, 1))

    # 진짜 이미지로 감별자 한번 학습
    d_loss_real = disciminator.train_on_batch(image, all_1)

    # 생성자를 이용해서 가짜 이미지 생성
    # 노이즈 벡터는 표준 정규 분포를 적용함
    noise = np.random.normal(0, 1, (M_BATCH, M_NOISE))
    fake = genarator.predict(noise)

    # 손글씨 숫자 0 이미지에 대한 하나의 batch 생성
    all_0 = np.zeros((M_BATCH, 1))

    # 가짜 이미지로 감별자 한번 학습
    d_loss_fake = disciminator.train_on_batch(fake, all_0)

    # 평균 손실과 정확도 계산
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

    return d_loss
# -------------------------------------------------------


# 생성자 학습 방법
@tf.function
def train_generator():
    # 노이즈 벡터는 표준 정규 분포를 사용
    noise = np.random.normal(0, 1, (M_BATCH, M_NOISE))

    # 손글씨 숫자 1 이미지에 대한 하나의 batch로 생성
    all_1 = np.ones((M_BATCH, 1))

    # 가짜 이미지로 생성자 한 번 학습
    g_loss = gan.train_on_batch(noise, all_1)

    return g_loss
# -------------------------------------------------------

# 샘플(결과) 이미지 NxN 출력 (output/ 폴더에 png 이미지 파일로 저장)
def sample(epoch):
    row = col = 4

    # 노이즈 벡터 생성
    noise = np.random.normal(0, 1, (row * col, M_NOISE))

    # 생성자 모델 이용 가짜 이미지 생성
    fake = genarator.predict(noise)

    # 채널 정보 삭제
    fake = np.squeeze(fake)

    # 캔버스 만들기
    fig, spot = plt.subplots(row, col)

    # i 행 j열에 가짜 이미지 추가
    cnt = 0
    for i in range(row):
        for j in range(col):
            spot[i, j].imshow(fake[cnt], cmap='gray')
            spot[i, j].axis('off')
            cnt += 1

    # 이미지를 png 파일로 저장
    path = os.path.join(M_FOLDER, 'img_{}'.format(epoch))
    plt.savefig(path)  # 파일로 생성됨
    plt.close()
# --------------------------------------------------------


# GAN 학습
def train_GAN():
    begin = time()
    print('\nGAN 학습 시작')

    # 지정된 epoch 만큼 반복 학습시킴
    for epoch in range(M_EPOCH + 1):
        d_loss = train_discriminator()
        g_loss = train_generator()

        # 매 50번 학습때마다 결과와 샘플 이미지 생성
        if epoch % 50 == 0:
            print('에포크 : ', epoch,
                  '생성자 손실 : {:.3f}'.format(g_loss),
                  '감별자 손실 : {:.3f}'.format(d_loss[0]),
                  '감별자 정확도 : {:.1f}%'.format(d_loss[1] * 100))
            sample(epoch)

    end = time()
    print('최종 학습 시간 : {:.1f}초'.format(end - begin))


######################################
### 컨트롤 타워 : 위에 작성된 함수 실행하는 부분임 ###

# 데이터 준비
X_train = read_data()

# GAN 구현
disciminator, genarator, gan = build_GAN()

# GAN 학습
train_GAN()
