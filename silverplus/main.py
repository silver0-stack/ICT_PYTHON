from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import tensorflow as tf

# 1. 모델과 토크나이저 로드
model_name = "beomi/kcbert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 2. 감정 분석 파이프라인 생성
sentiment_analyzer = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# 3. 테스트 문장
korean_sentences = [
    "이 제품은 정말 좋아요!",
    "완전 최악이에요. 다시는 사용하지 않을 겁니다.",
    "그냥 그런 것 같아요. 별로 특별하지 않네요."
]

#  레이블 이름 매핑
label_map = {
    "LABEL_0": "부정",
    "LABEL_1": "긍정"
}
# 4. 감정 분석 실행
for sentence in korean_sentences:
    result = sentiment_analyzer(sentence)
    label = label_map[result[0]['label']] # 레이블 매핑
    score = result[0]['score']
    print(f"문장: {sentence}")
    print(f"감정: {label}, 확신도: {score:.2f}")
