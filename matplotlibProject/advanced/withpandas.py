import matplotlib.pyplot as plt
import pandas as pd

# matplotlib은 pandas와 함께 데이터 시각화를 효율적으로 처리할 수 있다
data = {'x': [1,2,3,4], 'y':[10,20,25,30]}
df= pd.DataFrame(data)

plt.plot(df['x'], df['y'], marker='o')
plt.title('Line Plot with pandas')
plt.show()
