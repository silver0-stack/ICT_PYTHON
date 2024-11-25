# pandas_test1.py
from multiprocessing.connection import families

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# 데이터 분석을 위해서 Series와 DataFrame을 준비한다.
# Series: numpy의 1차원 배열 (백터) 또는 리스트 + 인덱스 라벨
# 배열과 비슷하지만 인덱스를 사용할 수 있다.
# 그 인덱스롤 통해 데이터에 라벨을 붙이거나 데이터를 빠르게 접근할 수 있다.

# 1. Series 객체 생성
# 예: 각 도시의 2023년도 인구 데이터를 시리즈로 만든다.
# pd.Series에 data, index를 전달해 각 도시의 이름과 인구데이터를 추가
# name 속성을 통해 시리즈의 이름을  설정
s = pd.Series([9904312, 3448737, 2890451, 2466052],  # 인구 데이터
              index=["서울", "부산", "인천", "대구"],  # 도시 이름
              name="2023년도 인구"  # 시리즈 이름
              )

print("=== Series 데이터 ===")
print(s)

# 2. Series 데이터 접근
# 인덱스 라벨을 사용해 개별 데이터나 여러 데이터를 선택가능
print("\n=== 개별 데이터 접근 ===")
print("서울의 인구:", s["서울"])  # 인덱스를 통해 접근
print("부산과 인천의 인구:\n", s[["부산", "인천"]])  # 여러 인덱스 선택

# 3. 데이터 연산
# mean()과 max() 같은 통계 메소드를 이용해 데이터 분석
print("\n=== 데이터 연산 ===")
print("전체 인구 평균:", s.mean())
print("최대 인구:", s.max())
# 조건 필터링을 통해 특정 조건에 맞는 데이터 선택 가능
print("인구 300만 이상의 도시:\n", s[s > 3000000])

# 4. Series 데이터 수정
s["서울"] += 1000000  # 서울의 인구 증가
print("\n=== 데이터 수정 후 ===")
print(s)

# 5. Series 데이터를 DataFrame으로 변환
#  reset_index()를 통해 Series를 DataFrame으로 변환
df = s.reset_index()
df.columns = ["도시", "인구"]  # 컬럼을 지정해 DataFrame 형태로 변경
print("\n=== DataFrame 데이터 ===")
print(df)






# 한글 폰트 설정 (Windows 기준)
plt.rc("font", family="Malgun Gothic") # 맑은 고딕 설정
plt.rc("axes", unicode_minus=True) # 마이너스 기호 깨짐 방지


# 데이터 준비
data = {
    "2019": [9904312, 3448737, 2890451, 2466052],
    "2020": [9631482, 3393191, 2632035, 2431774],
    "2021": [9762546, 3512547, 2517680, 2456016],
    "2022": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141],
}
df=pd.DataFrame(data, index=["서울", "부산", "인천", "대구"])


#  1. 연도별 인구 변화 시각화
plt.figure(figsize=(10, 6))
for city in df.index:
    plt.plot(["2019", "2020", "2021", "2022"], df.loc[city, ["2019", "2020", "2021", "2022"]], marker="o", label=city)
plt.title("2019-2022 연도별 인구 변화", fontsize=16)
plt.xlabel("연도", fontsize=12)
plt.ylabel("인구 수", fontsize=12)
plt.legend(title="도시", fontsize=10)
plt.grid()
plt.tight_layout()
plt.show()

#  2010-2015 증가율 시각화
plt.figure(figsize=(8, 6))
plt.bar(df.index, df["2010-2015 증가율"], color=["red", "green", "blue", "orange"])
plt.title()
plt.xlabel("도시", fontsize=12)
plt.ylabel("증가율", fontsize=12)
plt.tight_layout()
plt.show()
