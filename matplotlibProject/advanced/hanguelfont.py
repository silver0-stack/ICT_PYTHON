import matplotlib.pyplot as plt
from matplotlib import rc

# 한글 폰트 설정
rc('font', family='Malgun Gothic')  # Windows의 경우 맑은 고딕 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 한글 출력 테스트
plt.title("한글 그래프")
plt.plot([1, 2, 3, ], [1, 4, 9])
plt.show()
