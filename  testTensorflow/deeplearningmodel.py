import tensorflow_hub as hub
import tensorflow as tf
import numpy as np

# 모델 로드
model = hub.load('https://tfhub.dev/google/imagenet/resnet_v2_50/classification/5')

# 랜덤 텐서 생성 (이미지 입력 모의)
image = tf.random.uniform([1, 224, 224, 3])  # 배치 크기 1, 224x224 이미지, RGB 채널

# 모델 예측
logits = model(image)
predictions = tf.nn.softmax(logits)

print("예측 완료:", predictions.numpy())
