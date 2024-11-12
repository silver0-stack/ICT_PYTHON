from konlpy.tag import Okt

okt = Okt()

text = "이 영화는 정말 재미있다!"
tokens = okt.morphs(text)  # 형태소 분리
print("토큰:", tokens)

positive_words = ["재미있다", "좋다"]
negative_words = ["싫다", "별로다"]

positive_score = len([word for word in tokens if word in positive_words])
negative_score = len([word for word in tokens if word in negative_words])

# 긍정 점수: 1, 부정 점수: 0
print(f"긍정 점수: {positive_score}, 부정 점수: {negative_score}")

"""
워드 클라우드 생성
KoNLPy와 WordCloud를 결합하여 데이터 시각화를 수행할 수 있다
KoNLPy의 활용분야
- 감정 분석
- 텍스트 요약
- 키워드 추출
- 문서 분류
- 뉴스 기사 분석
- 한국어 기본 챗봇
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt

text = "KoNLPy를 사용하여 데이터 마이닝과 자연어 처리를 할 수 있습니다."
okt = Okt()

# 명사 추출
nouns = okt.nouns(text)
words = " ".join(nouns)

# 워드 클라우드 생성
wordcloud = WordCloud(
    font_path='C:/Users/ict01_27/Downloads/D2Coding-Ver1.3.2-20180524/D2Coding/d2coding.ttc',
    background_color='white'
).generate(words)


# 시각화
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show( )