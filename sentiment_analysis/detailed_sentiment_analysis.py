from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from sklearn.model_selection import train_test_split
import tensorflow as tf
import pandas as pd

# 1. 데이터 로드
file_path = './ratings_test.txt'  # 경로 수정 필요 시 변경
data = pd.read_csv(file_path, sep='\t')

# 데이터 확인
print(data.head())


# 비어있는 텍스트 제거
data = data.dropna(subset=['document'])  # document 열에서 NaN 제거
data = data[data['document'].str.strip() != '']  # 빈 문자열 제거

# 텍스트와 라벨 분리
texts = data['document'].tolist()
labels = data['label'].tolist()

# 데이터셋 분리
train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2)


print(type(train_texts), type(val_texts))  # 타입 확인
print(train_texts[:5])  # 샘플 데이터 확인



# 2. 토크나이저와 모델 로드
model_name = "beomi/kcbert-base"  # 감정 분석 모델
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)  # 긍정/부정 라벨링

# 3. 입력 데이터 토크나이징
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=128, return_tensors="tf")
val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=128, return_tensors="tf")

# 4. 데이터셋 준비
train_dataset = tf.data.Dataset.from_tensor_slices((
    {"input_ids": train_encodings["input_ids"], "attention_mask": train_encodings["attention_mask"]},
    tf.convert_to_tensor(train_labels)
))

val_dataset = tf.data.Dataset.from_tensor_slices((
    {"input_ids": val_encodings["input_ids"], "attention_mask": val_encodings["attention_mask"]},
    tf.convert_to_tensor(val_labels)
))

# 5. 모델 학습 설정
optimizer = Adam(learning_rate=5e-5)
loss = SparseCategoricalCrossentropy(from_logits=True)  # 손실 함수 설정
model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

# 6. 모델 학습
print("모델 학습 시작...")
model.fit(train_dataset.shuffle(16).batch(8), validation_data=val_dataset.batch(8), epochs=3)

# 7. 사용자 입력 테스트
def predict_sentiment(sentence):
    encoding = tokenizer(sentence, truncation=True, padding=True, max_length=128, return_tensors="tf")
    prediction = model(encoding)
    predicted_class = tf.argmax(prediction.logits, axis=-1).numpy()[0]
    sentiment_map = {0: "부정", 1: "긍정"}
    return sentiment_map[predicted_class]

# 테스트 예제
while True:
    user_input = input("감정을 분석할 문장을 입력하세요 (종료하려면 'exit' 입력): ")
    if user_input.lower() == "exit":
        print("감정 분석을 종료합니다.")
        break
    sentiment = predict_sentiment(user_input)
    print(f"문장: {user_input}")
    print(f"예측 감정: {sentiment}")
