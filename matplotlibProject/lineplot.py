import matplotlib.pyplot as plt

# plot(플롯)이란 데이터 또는 정보를 나타내기 위해 다이어그램 또는 차트를
# 만드는 프로세스를 말한다.
# 데이터 정의
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11] # Prime Numbers(소수)

# 그래프 그리기
plt.plot(x, y, label="Prime Numbers")
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# plt.legend()는 범례를 표시하는 코드다.
# 범례는 그래프에 표시된 여러 선, 막대, 점 등의 데이터가 무엇을 나타내는지 설명한다.
plt.legend()
plt.grid(True)

# 그래프 출력
plt.show()