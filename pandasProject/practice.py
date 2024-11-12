"""
Pandas의 DataFrame은 2차원 테이블 형태의 데이터 구조로, 엑셀 스프레드시트와 비슷하다.
행(row)와 열(column)로 구성되며, 각 열은 서로 다른 데이터 타입을 가질 수 있다/
분석, 필터링, 집계 등에 자주 사용된다
"""
# DataFrame 생성
# 딕셔너리로 생성
import pandas as pd

print('\n======== 딕셔너리로 생성 ==========')
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

df.info()
print(df.head()) #기본 5개 행 출력

print('\n======== 리스트로 생성 ==========')
data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

columns = ["Name", "Age", "City"]

df = pd.DataFrame(data, columns=columns)
print(df)

print("\n =========== Numpy 배열로 생성 =========")
import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(data, columns =["A", "B"])
print(df)



