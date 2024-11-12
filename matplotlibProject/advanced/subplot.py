import matplotlib.pyplot as plt

x = range(1, 6)
y = [1, 4, 9, 16, 25]

plt.subplot(1,2,1) # 1행 2열의 첫 번째
plt.plot(x, y, 'r--')
plt.title('Left Plot')

plt.subplot(1, 2, 2) # 1행 2열의 두 번째
plt.bar(x, y)
plt.title('Right Plot')

plt.tight_layout()
plt.show()