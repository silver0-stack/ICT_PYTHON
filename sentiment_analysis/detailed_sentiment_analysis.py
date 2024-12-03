from transformers import AuthTokenizer, TFAutoModelForSequenceClassification
from tensorflow.keras.optimizers import Adam
from skleran.model_selection import train_test_split
import tensroflow as tf

# 1. 데이터 준비
sentences = [
    "이 제품은 정말 좋아요!",  # 기쁨
    "완전 최악이에요. 다시는 사용하지 않을 겁니다.",  # 분노
    "아무 느낌도 없어요. 그냥 그래요.",  # 중립
    "오늘 너무 슬퍼요.",  # 슬픔
    "이 일은 좀 무섭네요."  # 두려움
]
labels = [0, 1, 2, 3, 4]  # 0: 기쁨, 1: 분노, 2: 중립, 3: 슬픔, 4: 두려움

# 데이터셋 분리
train_texts, val_texts, train_labels, val_labels = train_test_split(sentences, labels, test_size=0.2)

# 2. 토크나이저와 모델 로드
model_name