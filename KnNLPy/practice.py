"""
KoNLPy(한국어 자연어 처리 라이브러리)
Korean Natural Language Processing
KoNLPy는 Python을 기반으로 한 한국어 자연어 처리(NLP) 라이브러리입니다.
KoNLPy는 형태소 분석, 품사 태깅, 어휘 추출과 같은 한국어 텍스트 분석 작업을 수행하는 데 사용된다.
특히 한국어에 특화된 여러 형태소 분석기(Morpheme Analyzer)를 지원하여,
한국어 처리가 필요한 다양한 데이터 분석 및 텍스트 마이닝 작업에 매우 유용하다.
"""
"""
1. KoNLPy의 주요 특징
- 한국어 형태소 분석기 지원:
  - Hannanum
  - Kkma
  - Komoran
  - Mecab(Linux/macOS에서 기본적으로 사용 가능)
  - Okt(Open Korean Text)
- 텍스트 토큰화 (단어 분리)
- 품사 태깅
- 명사 추출
- 키워드 분석
"""

# Okt(Open Korean Text)
# 가장 많이 사용되는 분석기로, 간단한 형태소 분석과 감정 분석에 적합하다.
from konlpy.tag import Okt

okt=Okt()

text = "KoNLPy는 한국어 처리를 위한 라이브러리입니다."

# 형태소 분석
morphs = okt.morphs(text)
print("형태소 분석:", morphs)

# 품사 태깅
pos = okt.pos(text)
print("품사 태깅:",pos)

# 명사 추출
nouns = okt.nouns(text)
print("명사 추출:",nouns)

# 어간 추출
stem=okt.morphs(text, stem=True)
print("어간 추출:",stem)

"""
Mecab은 빠르고 정확하며, 대량의 텍스트 처리에 적합하다.
"""

from konlpy.tag import Mecab

mecab = Mecab()

text = "Mecab은 성능이 뛰어난 형태소 분석가입니다."

# 형태소 분석
morphs = mecab.morphs(text)
print("형태소 분석:", morphs)

# 품사 태깅
pos = mecab.pos(text)
print("품사 태깅:", pos)

# 명사 추출
nouns = mecab.nouns(text)
print("명사 추출:",nouns)

"""
Kkma(꼬꼬마)는 문장 분리와 세밀한 품사 태깅에 유용하다.
"""
from konlpy.tag import Kkma

kkma = Kkma()

text="꼬꼬마 형태소 분석기는 문장 단위로 분석을 수행한다."

# 문장 분리
sentences = kkma.sentences(text)
print("문장 분리:",sentences)

# 형태소 분석
morphs=kkma.morphs(text)
print("형태소 분석:", morphs)

# 품사 태깅
pos = kkma.pos(text)
print("품사 태깅:",pos)