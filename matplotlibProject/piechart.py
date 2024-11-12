import matplotlib.pyplot as plt

labels = ['A','B','C','D','E','F']
sizes = [15, 20, 35, 25, 10, 5]
colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, labels=labels,colors=colors,autopct='%1.1f%%')
plt.title("Pie Chart")
plt.axis('equal')
plt.show()